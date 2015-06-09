from waflib.Logs import pprint
from os.path import exists, getmtime


def fatal(str):
	pprint('RED', str)
	exit(1)

def generate_rtems_config(ctx, file_in, file_out, devel=False):
	from os import fchmod
	from pprint import PrettyPrinter
	pp = PrettyPrinter(depth=4)
	bsps = {}


	for bsp in ctx.env.BSP:
		env = ctx.all_envs[bsp]
		bsps[bsp] = {
			"cflags":	env.CFLAGS + env.CONFIG_CFLAGS,
			"libs":		env.LIBS + ["-lrtemscpu -lrtemsbsp"] + env.CONFIG_LIBS,
			"ldflags":	env.LDFLAGS + env.CONFIG_LDFLAGS,
			"description": env.CONFIG_DESCRIPTION
		}

		if devel:
			srcnode = ctx.srcnode.abspath()
			path_bld = "%s/%s" % (ctx.bldnode.abspath(), bsp)

			include = []
			include.append("-I%s/include" % srcnode)
			include.append("-I%s/include" % path_bld)
			include.append("-I%s/include/rtems" % path_bld)
			bsps[bsp]["cflags"] = include + bsps[bsp]["cflags"]
#			bsps[bsp]["libs"] = ["%s/c/start.o" % path_bld] + bsps[bsp]["libs"]

			ldflags = []
			ldflags.append("-specs %s/gcc_spec" % path_bld)
			ldflags.append("-L%s/cpukit/" % path_bld)
			ldflags.append("-L%s/c/" % path_bld)
#			ldflags.append("-Wl,-T %s/c/linkcmds" % path_bld)
#			bsps[bsp]["ldflags"] = ldflags + bsps[bsp]["libs"]
			bsps[bsp]["ldflags"] += ldflags + ["-Wl,-start-group"] + bsps[bsp]["libs"] + ["-lc"] + ["-lgcc"] + ["-Wl,-end-group"]

		else:
			raise Exception("Doesn't work in install mode yet.")

	#XXX: file_in and file_out can be automatically calculated they don't need to be parms.
	with open(file_in, "r") as fp:
		config = fp.read()

	with open(file_out, "w") as fp:
		fp.write('#!%s\n'					% ctx.env.BIN_PYTHON[0]) # XXX: How does this work on Windows?
		fp.write('RTEMS_VERSION = "%s"\n'	% ctx.env.RTEMS_VERSION)
		fp.write('PREFIX="%s"\n'			% ctx.env.PREFIX)
		fp.write('BSP_LIST = %s\n'			% pp.pformat(bsps))
		fp.write(config)
		fchmod(fp.fileno(), 0o755)


def generate_gcc_spec_file(ctx, devel=False):
	path_bld = "%s/%s" % (ctx.bldnode.abspath(), ctx.variant)
	data = []

	def expand_flags(ctx, obj_list):
		path_bld = "%s/%s" % (ctx.bldnode.abspath(), ctx.variant)
		l = []
		for obj in obj_list:
			obj = obj.replace("${RTEMS}", "%s/c" % path_bld)
			if obj.endswith('.o'):
				fmt = '%s%%s'
			else:
				fmt = '%s'
			l.append(fmt % obj)
		return " ".join(l)

	data.append("*startfile:")
	data.append(expand_flags(ctx, ctx.env.LINK_START))
	data.append("")
	data.append("*endfile:")
	data.append(expand_flags(ctx, ctx.env.LINK_END))
	data.append("")
	data.append("*link:")
	data.append(expand_flags(ctx, ctx.env.LINK_LINK))

	with open("%s/gcc_spec" % path_bld, "w") as fp:
		for line in data:
			fp.write(line)
			fp.write("\n")

	ctx.env.append_value('cfg_files', "%s/gcc_spec" % path_bld)

	return "%s/%s/gcc_spec" % (ctx.bldnode, ctx.variant)



# Get all the BSPs for a specific arch
def rtems_bsp_arch_all(arch):
	from .bsp import list_bsp
	if arch not in list_bsp:
		fatal("Incorrect arch for --bsp, must be in the form of arch or arch/name: \"%s\"" % arch)
	bsp_list = []
	for bsp in list_bsp[arch]:
		bsp_list += ['%s/%s' % (arch, bsp)]
	return bsp_list


# Get all the BSPs
def rtems_bsp_all():
	from .bsp import list_bsp
	bsp_list = []
	for arch in list_bsp:
		for bsp in list_bsp[arch]:
			bsp_list += ['%s/%s' % (arch, bsp)]
	return bsp_list


def rtems_bsp_wildcard(pattern):
	if '.' in pattern:
		pattern = pattern.replace('.', '\.')
	if '*' in pattern:
		pattern = pattern.replace('*', '.*')
	return '^' + pattern + '$'


def rtems_bsp_list(bsps):
	import re
	from .bsp import list_bsp

	bsp_list = [x.strip() for x in bsps.split(',')]

	verified_bsp_list = []

	for bsp in bsp_list:
		if '/' not in bsp:
			fatal("Incorrect value for --bsp must be in the form of arch/name: \"%s\"" % bsp)
		(arch, bsp) = bsp.split('/')
		pa = re.compile(rtems_bsp_wildcard(arch), re.IGNORECASE)
		pb = re.compile(rtems_bsp_wildcard(bsp), re.IGNORECASE)
		for arch in list_bsp:
			if pa.match(arch) is not None:
				for bsp in list_bsp[arch]:
					if pb.match(bsp) is not None:
						arch_bsp = '%s/%s' % (arch, bsp)
						verified_bsp_list += [arch_bsp]
	return sorted(verified_bsp_list)


def rtems_cmd_config(ctx):
	if ctx.options.list is True:
		from .bsp import list_bsp

		from py.config import BuildConfig
		cfg = BuildConfig()

		for arch in sorted(list_bsp):
			print(arch)
			for bsp in sorted(list_bsp[arch]):
				descr = cfg.bsp_get_detail(arch, bsp)
				print("  %-20s %s" % (bsp, descr))
			print("")
		return

	if ctx.options.force is False and exists("config.cfg"):
		ctx.fatal("Please delete config.cfg before creating a new one.")

	if not ctx.options.bsps:
		ctx.fatal("You must specify a single or comma separated list of BSPs using --bsp")

	bsp_list = rtems_bsp_list(ctx.options.bsps)
	if not bsp_list:
		ctx.fatal("You must specify a single or comma separated list of BSPs using --bsp")

	from py.config import BuildConfig
	cfg = BuildConfig(bsp_list)
	cfg.option_set("general", "PATH_TOOLS", ctx.options.path_tools or "")
	cfg.option_set("general", "PREFIX", ctx.options.prefix or "")
	cfg.save()

	pprint("YELLOW", "Wrote config.cfg")
	archs = {}
	for bsp in bsp_list:
		pprint("YELLOW", "  - %s" % bsp)
		arch = bsp.split('/')[0]
		if arch not in archs:
			archs[arch] = 0
		archs[arch] += 1

	pprint("YELLOW", "Configured BSPS:")
	pprint("YELLOW", " Total    : %d" % len(bsp_list))
	arch_list = sorted(archs.keys())
	for arch in arch_list:
		pprint("YELLOW", "  %-8s: %d" % (arch, archs[arch]))


def rtems_cmd_bsp(ctx):
	ctx.fatal("Not implemented.")
	print("List of available BSPs")
	print("List of DISABLED BSPs")


# Get file mtime.
def get_file_mtime(file):
	return getmtime(file)


from subprocess import Popen, PIPE

def run(cmd):
	p =  Popen(cmd, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	return stdout[:-1], stderr[:-1], p.returncode
