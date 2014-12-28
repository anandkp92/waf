from waflib.Task import Task
from waflib.TaskGen import feature, before, after, extension, after_method
from waflib.Configure import conf
from waflib.Logs import pprint
#from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext
#from waflib import Build, Scripting
#from waflib.Tools import c_preproc
#from rtems_waf import gccdeps
#from waflib import Logs
#import ConfigParser


#################
# Handle .S Files
#################
class casm(Task):
#	run_str = '${CC} ${ARCH_ST:ARCH} ${CFLAGS} ${CPPFLAGS} ${CPPPATH_ST:INCPATHS} ${DEFINES_ST:DEFINES} ${CC_SRC_F}${SRC} ${CC_TGT_F}${TGT}'
	run_str = '${CC} -DASM ${ARCH_ST:ARCH} ${CFLAGS} ${CPPFLAGS} ${FRAMEWORKPATH_ST:FRAMEWORKPATH} ${CPPPATH_ST:INCPATHS} ${DEFINES_ST:DEFINES} ${CC_SRC_F}${SRC} ${CC_TGT_F}${TGT}'
	ext_in  = ['.h']
	ext_out  = ['.o']
	color = 'BLUE'

@extension('.S')
def asm_hook(self, node):
	return self.create_compiled_task('casm', node)


##########
# Features
##########
@feature('bld_include')
@after_method('apply_incpaths')
def insert_blddir(self):
	self.env.prepend_value('INCPATHS', ['include'])

@feature('src_include')
@after_method('apply_incpaths', 'insert_blddir')
def insert_srcdir(self):
	path = self.bld.srcnode.abspath()
	self.env.append_value('INCPATHS', "%s/include" % path)

	if self.env.ENABLE_SMP:
		self.env.append_value('INCPATHS', "%s/cpukit/score/include/" % path)
		self.env.append_value('INCPATHS', "%s/cpukit/rtems/include/" % path)

@feature('src_include_rtems')
@after_method('apply_incpaths', 'insert_blddir')
def insert_srcdir_rtems(self):
	self.env.append_value('INCPATHS', "%s/include/rtems" % self.bld.srcnode.abspath())

@feature('src_include_networking')
@after_method('apply_incpaths', 'insert_blddir')
def insert_srcdir_networking(self):
	self.env.append_value('INCPATHS', "%s/cpukit/libnetworking" % self.bld.srcnode.abspath())

@feature('src_include_bsp')
@after_method('apply_incpaths', 'insert_blddir')
def insert_srcdir_bsp(self):
	self.env.append_value('INCPATHS', "%s/include/bsp" % self.bld.srcnode.abspath())

@feature('src_include_libcpu')
@after_method('apply_incpaths', 'insert_blddir')
def insert_srcdir_libcpu(self):
	self.env.append_value('INCPATHS', "%s/include/libcpu" % self.bld.srcnode.abspath())

@feature('src_include_libchip')
@after_method('apply_incpaths', 'insert_blddir')
def insert_srcdir_libchip(self):
	self.env.append_value('INCPATHS', "%s/include/libchip" % self.bld.srcnode.abspath())


###########
# Shortcuts
###########
def rtems_build(cmd, ctx, target_name, source, **kwarg):
	feature = "c bld_include"
	if "features" in kwarg:
		feature = "%s %s" % (kwarg["features"], feature)
		del kwarg["features"]

	cmd(
		source   = source,
		target   = target_name,
		features = feature,
		install_path = ctx.env.LIBDIR,
		**kwarg)

# There's probably a better way to do this.
@conf
def rtems_lib(ctx, target_name, source, **kwarg):
	rtems_build(ctx.stlib, ctx, target_name, source, **kwarg)

@conf
def rtems_obj(ctx, target_name, source, **kwarg):
	rtems_build(ctx, ctx, target_name, source, **kwarg)

@conf
def rtems_program(ctx, target_name, source, **kwarg):
	rtems_build(ctx.program, ctx, target_name, source, **kwarg)


@conf
def copy(ctx, source, target, name):
	ctx(
		rule='cp ${SRC} ${TGT}', # XXX: Make something that works on windows.
		source=source,
		target=target,
		name=name
	)

#################
# Configure Steps
#################
@conf
def check_func(ctx, func, mandatory=False):
	ctx.check_cc(
		mandatory   = mandatory,
		fragment    = "char %s();\n int main() { return %s(); return 0; }" % (func, func),
		define_name = "HAVE_%s" % func.upper(),
		execute     = False,
		msg         = "Checking for C library function %s" % func
	)


@conf
def check_size(ctx, field, mandatory=False, define_name=None):
	if define_name is None:
		define_name = "SIZEOF_%s" % field.upper()

	ctx.check_cc(
		mandatory   = mandatory,
		fragment    = """
			#include <sys/types.h>
			#include <stdio.h>
			main() {
			  printf("%%d", sizeof(%s));
			  return 0;
			}
			""" % field,
		execute     = True,
		define_ret  = True,
		define_name = define_name,
		quote       = False,
		msg         = "Checking size of %s" % field
	)


# XXX: It prints "yes" even if it doesn't exist.
@conf
def check_define(ctx, define, header, mandatory=False):
	ctx.check(
		mandatory   = mandatory,
		fragment    = '''#include <%s>\n int main () {\n #ifdef %s\n return 0;\n #endif\n return 1; }\n''' % (header, define),
		define_name = "HAVE_%s" % define.upper(),
		features    = "c cprogram",
		execute     = True,
		msg         = "Checking for define %s in %s" % (define, header)
	)


#################################################
# This writes objects to a file if there are > 25
# objects to avoid commandline arg limits for ar.
#################################################
def rtems_stlib_command(self, *k, **kw):
	# Following block borrowed from waflib/Tools/msvc.py
	bld = self.generator.bld

	try:
		if not kw.get('cwd', None):
			kw['cwd'] = bld.cwd
	except AttributeError:
		bld.cwd = kw['cwd'] = bld.variant_dir

	# Put the objects on the commandline if there aren't enough to
	# warrant writing to a file.
	if len(self.inputs) < 25:
		return self.generator.bld.exec_command(*k, **kw)

	file_obj = "%s_files" % self.outputs[0].abspath()
	with open(file_obj, "w") as fp:
		for f in self.inputs:
			fp.write("%s\n" % f.bldpath())

	pprint("YELLOW", "Wrote %d objects to %s" % (len(self.inputs), file_obj))
	cmd = self.env.AR + ["rc", self.outputs[0].bldpath(), "@%s_files" % self.outputs[0].bldpath()]

	# Task information for JSON build output.
	if self.env.BUILD_JSON:
		kw["json_task_self"] = self

	return self.generator.bld.exec_command(cmd, **kw)



# Tests
@feature('test_include')
@after_method('apply_incpaths')
def insert_test_include(self):
	self.env.prepend_value('INCPATHS', "%s/testsuites/support/include" % self.bld.srcnode.abspath())


from waflib.Tools.c import cprogram
from waflib.Tools.ccroot import USELIB_VARS

USELIB_VARS['test_cprogram'] = set(['STLIB', 'STLIBPATH', 'LDFLAGS'])

#from StringIO import StringIO
from os import fdopen, pipe, read, close
class test_cprogram(cprogram):
	run_str = '${LINK_CC} ${LDFLAGS} ${CFLAGS} ${CCLNK_SRC_F}${SRC} ${CCLNK_TGT_F}${TGT[0].abspath()} -specs gcc_spec -Wl,-Bstatic -Lc -Lcpukit -Wl,-start-group -lc -lgcc ${STLIBPATH_ST:STLIBPATH} ${STLIB_ST:STLIB}  -Wl,-end-group'

	def exec_command(self, cmd, **kw):
		r, w = pipe()
		rfd = fdopen(r, "rb", 0)
		kw["stderr"] = fdopen(w, "wb", 0)
		ret = cprogram.exec_command(self, cmd, **kw)
		kw["stderr"].close()

		if ret == 1:
			data = rfd.readlines()
			if " ".join(data).find("will not fit in region") != -1:
				file = self.outputs[0].abspath()
				with open(file, "w") as fp:
					fp.write("Target does not meet test memory constraints.\n")
				pprint("RED", "Target \"%s\" does not meet test memory constraints." % file)
				rfd.close()
				return 0
			print("".join(data))

		rfd.close()
		return ret



@conf
def rtems_test(ctx, target_name, source_name, **kwarg):
	features_merged = "c test_cprogram bld_include src_include"
	if "features" in kwarg:
		features_merged = "%s %s" % (kwarg["features"], features_merged)
		del kwarg["features"]

	use_merged = "rtemsbsp rtemscpu"
	if "use" in kwarg:
		use_merged = "%s %s" % (kwarg["use"], use_merged)
		del kwarg["use"]

	ctx(
		source			= source_name,
		target			= "test_%s" % target_name,
		features		= features_merged,
		use				= use_merged,
		install_path	= ctx.env.TESTDIR,
		**kwarg
	)


@conf
def rtems_doc(ctx, section):
	pprint("YELLOW", "See http://docs.rtems.org/%s/user/#%s (Not activated yet!)" % (ctx.env.RTEMS_VERSION, section))


@conf
def rtems_fatal(ctx, message, section):
	pprint("RED", message)
	ctx.rtems_doc(section)
	ctx.fatal("Fatal error")


@conf
def rtems_warn(ctx, message, section):
	pprint("YELLOW", message)
	ctx.rtems_doc(section)

