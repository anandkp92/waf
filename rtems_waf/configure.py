from waflib.Logs import pprint
pprint.__doc__ = None # Make sure waf doesn't see this as a command.
from waflib.Utils import subprocess

# TODO
# __attribute__((weak) will not work on a cross compile.
#		__RTEMS_SIZEOF_VOID_P__


# XXX: BSP hacks that need to be addressed / resolved.
def bsp_hack(ctx, bsp):
	if bsp == "m68k/mvme167":
		# PowerPC unfortunatly uses macros to define this instead of an integer.
		# We need to choose one or the other.
		ctx.define('CONSOLE_MINOR', 1)
		ctx.define('PRINTK_MINOR', 1)

	# I have no idea why it was done this way.
	if bsp.startswith("arm/xilinx_zynq_") and ctx.env.ENABLE_SMP:
		ctx.env.ZYNQ_CPUS = 2



# general
def config_h(ctx):
	# Are these even needed?
	ctx.define_cond('ENABLE_DEBUG', ctx.env.ENABLE_DEBUG)
	ctx.define_cond('ENABLE_MP', ctx.env.ENABLE_MP)
	ctx.define_cond('ENABLE_MULTILIB', ctx.env.ENABLE_MULTILIB)
	ctx.define_cond('ENABLE_NETWORKING', ctx.env.ENABLE_NETWORKING)
	ctx.define_cond('ENABLE_NEWLIB', ctx.env.ENABLE_NEWLIB)
	ctx.define_cond('ENABLE_POSIX', ctx.env.ENABLE_POSIX)
	ctx.define_cond('ENABLE_PTHREADS', ctx.env.ENABLE_PTHREADS)
	ctx.define_cond('ENABLE_SERDB', ctx.env.ENABLE_SERDB)
	ctx.define_cond('ENABLE_SHELL', ctx.env.ENABLE_SHELL)
	ctx.define_cond('ENABLE_SMP', ctx.env.ENABLE_SMP)

	header = ["sys/types.h", "sys/stat.h", "stdlib.h", "memory.h", "string.h", "strings.h", "inttypes.h", "stdint.h", "unistd.h", "getopt.h", "libgen.h"]
	for file in header:
		ctx.check(header_name=file, features='c cprogram', mandatory=False)

	ctx.check_inline()
	ctx.check_cc(function_name='strerror', header_name="string.h", mandatory=True)
	ctx.check_cc(function_name='strtol', header_name=["stdlib.h", "limits.h"], mandatory=True)
	ctx.check_cc(function_name='basename', header_name="libgen.h", mandatory=True)


# cpukit/
def config_h_libcpu(ctx):
	# Mandated by POSIX, decls not present in some versions of newlib,
	# some versions stubbed in newlib's rtems crt0
	files = ["seteuid", "geteuid", "setegid", "getegid", "setuid", "getuid", "setgid", "getgid", "setsid", "getsid", "setpgid", "getpgid", "setpgrp", "getpgrp"]
	for f in files:
		ctx.check_cc(function_name=f, header_name="unistd.h", mandatory=False)

	# Mandated by POSIX, decls not present in some versions of newlib
	ctx.check_cc(function_name='flockfile', header_name="stdio.h", mandatory=False)
	ctx.check_cc(function_name='funlockfile', header_name="stdio.h", mandatory=False)
	ctx.check_cc(function_name='ftrylockfile', header_name="stdio.h", mandatory=False)

	# BSD-isms, used throughout the sources.
	func = ["strsep", "strcasecmp", "snprintf", "strdup", "strndup", "strncasecmp", "bcopy", "bcmp", "isascii", "fileno", "strlcpy", "strlcat", "sbrk"]

	# Check for functions supplied by newlib >= 1.17.0 Newlib's posix/ directory
	func += ["readdir_r", "isatty", "creat", "opendir", "closedir", "readdir", "rewinddir", "scandir", "seekdir", "sleep", "telldir", "usleep", "__assert", "execl", "execlp", "execle", "execv", "execvp", "execve", "regcomp", "regexec", "regerror", "regfree"]

	# Newlib's unix/ directory
	func += ["ttyname", "getcwd"]
	for f in func:
		ctx.check_func(f, mandatory=False)

	header = ["tar.h", "errno.h", "sched.h", "sys/cdefs.h", "sys/queue.h", "stdint.h", "inttypes.h", "pthread.h"]
	for file in header:
		ctx.check(header_name=file, features='c cprogram')

	ctx.check(header_name="pthread.h", features='c cprogram')
	ctx.check_cc(type_name='pthread_rwlock_t', header_name="pthread.h", mandatory=False)
	ctx.check_cc(type_name='pthread_barrier_t', header_name="pthread.h", mandatory=False)
	ctx.check_cc(type_name='pthread_spinlock_t', header_name="pthread.h", mandatory=False)
	# pthread-functions not declared in some versions of newlib.
	ctx.check_cc(function_name='pthread_attr_getguardsize', header_name="pthread.h", mandatory=False)
	ctx.check_cc(function_name='pthread_attr_setguardsize', header_name="pthread.h", mandatory=False)
	ctx.check_cc(function_name='pthread_attr_setstack', header_name="pthread.h", mandatory=False)
	ctx.check_cc(function_name='pthread_attr_getstack', header_name="pthread.h", mandatory=False)

	ctx.check(header_name="signal.h", features='c cprogram')
	ctx.check_cc(type_name='sighandler_t', header_name="signal.h", mandatory=False)

	# FIXME: Mandatory in SUSv4, optional in SUSv3.
	#   Not implemented in GCC/newlib, so far.
	ctx.check_define("WORD_BIT", "limits.h")
	ctx.check_define("LONG_BIT", "limits.h")

#	ctx.check_define("CLOCK_PROCESS_CPUTIME_ID", "time.h")
#	ctx.check_define("CLOCK_THREAD_CPUTIME_ID", "time.h")

	types = [
		"uint8_t", "int8_t",
		"uint16_t", "int16_t",
		"uint32_t", "int32_t",
		"uint64_t", "int64_t",
		"uintmax_t", "intmax_t",
		"uintptr_t", "intptr_t"
	]
	for type in types:
		ctx.check_cc(type_name=type, header_name="stdint.h", mandatory=False)

#	ctx.check_size("mode_t")
#	ctx.define_cond('HAVE_MD5', True) # XXX: hack for cpukit/mghttpd/mongoose.c
	ctx.define('SIZEOF_MODE_T', 4) # XXX: This is a hack for cpukit/libfs/src/nfsclient/src/dirutils.c
	ctx.define('SIZEOF_VOID_P', 4)
	ctx.define('SIZEOF_OFF_T', 8)
	ctx.define('SIZEOF_TIME_T', 4) # XXX: hack for cpukit/libmisc/uuid/gen_uuid.c
	ctx.define('SIZEOF_BLKSIZE_T', 4) # XXX: hack for tests
#	ctx.check_size("off_t")
#	ctx.check_size("void *", define_name="SIZEOF_VOID_P")

	ctx.define('__RTEMS_HAVE_DECL_SIGALTSTACK__', 1)


def version_header_info(ctx, config):
	ctx.define('__RTEMS_MAJOR__', config["rtems_version_major"])
	ctx.define('__RTEMS_MINOR__', config["rtems_version_minor"])
	ctx.define('__RTEMS_REVISION__', config["rtems_version_revision"])
	ctx.define('RTEMS_VERSION', ctx.env.RTEMS_VERSION)
	ctx.define('RTEMS_BSP', ctx.env.RTEMS_BSP)


# c/
def config_h_libbsp(ctx):
	ctx.define('__RTEMS_SIZEOF_VOID_P__', 4)


def cpuopts_h(ctx):
	ctx.define_cond('__RTEMS_USE_TICKS_FOR_STATISTICS__', False) # disable nanosecond granularity for statistics
	ctx.define_cond('__RTEMS_USE_TICKS_CPU_USAGE_STATISTICS__', False) # disable nanosecond granularity for cpu usage statistics
	ctx.define_cond('__RTEMS_USE_TICKS_RATE_MONOTONIC_STATISTICS__', False) # disable nanosecond granularity for period statistics
	ctx.define_cond('__RTEMS_DO_NOT_INLINE_THREAD_ENABLE_DISPATCH__', False) # disable inlining _Thread_Enable_dispatch (This improves both the size and coverage analysis.)
	ctx.define_cond('__RTEMS_DO_NOT_INLINE_CORE_MUTEX_SEIZE__', False) # disable inlining _Thread_Enable_dispatch (This improves both the size and coverage analysis.)
	ctx.define_cond('__RTEMS_DO_NOT_UNROLL_THREADQ_ENQUEUE_PRIORITY__', False) # disable inlining _Thread_queue_Enqueue_priority (This improves both the size and coverage analysis.)
	ctx.define_cond('__RTEMS_STRICT_ORDER_MUTEX__', False) # disable strict order mutex (This gives the same behavior as 4.8 and older)
	ctx.define_cond('__RTEMS_ADA__', False) # ada/gnat bindings are built-in (Deactivate ada bindings)

	ctx.define_cond('RTEMS_DEBUG', ctx.env.ENABLE_DEBUG)
	ctx.define_cond('RTEMS_MULTIPROCESSING', ctx.env.ENABLE_MP)
	ctx.define_cond('RTEMS_NETWORKING', ctx.env.ENABLE_NETWORKING)
	ctx.define_cond('RTEMS_NEWLIB', ctx.env.ENABLE_NEWLIB)
	ctx.define_cond('RTEMS_POSIX_API', ctx.env.ENABLE_POSIX)
	ctx.define_cond('RTEMS_SMP', ctx.env.ENABLE_SMP)


def depend_version(ctx):
	ctx.start_msg("Checking GCC version")
	ctx.get_cc_version(ctx.env.CC, gcc=True)
	ctx.end_msg(".".join(ctx.env.CC_VERSION))

	ctx.start_msg("Checking Binutils version")
	cmd = ctx.env.BIN_RTEMS_LD + ["-v"]
	ctx.env.LD_VERSION = ctx.cmd_and_log(cmd, quiet=0).strip().split(" ")[-1]
	ctx.end_msg(ctx.env.LD_VERSION)


def build_config(ctx):
	ctx.start_msg("DEVEL: Collecting compiler configuration")
	cmd = ctx.env.CC + ["-dM", "-E", "-"]
	p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=None)
	p.stdin.write("\n")
	gcc_config, stderr = p.communicate()
	ctx.end_msg("Done")

	ctx.start_msg("DEVEL: Getting revision")
	cmd = ["git", "log", "-1", "--format=%H"]
	p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=None)
	ctx.env.REVISION, stderr = p.communicate()
	ctx.env.REVISION = ctx.env.REVISION.replace("\n", "")
	ctx.end_msg(ctx.env.REVISION)

	with open("build/c4che/%s/%s_cache.py" % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_BSP), "r") as fp:
		cache_data = fp.read()

	ctx.start_msg("DEVEL: Writing build information")
	from json import JSONEncoder
	from time import strftime

	data = JSONEncoder(sort_keys=True).encode({
		"time": int(strftime("%s")), # There is no better way to get seconds across lal platforms?
		"revision": ctx.env.REVISION,
		"bsp": ctx.env.RTEMS_BSP,
		"architecture": ctx.env.RTEMS_ARCH,
		"version": {
			"gcc": ".".join(ctx.env.CC_VERSION),
			"binutils": ctx.env.LD_VERSION
		},
		"waf_cache": cache_data,
		"gcc_config": gcc_config
	})
	file = "build/c4che/%s/build_%s.json" % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_BSP)
	with open(file, "w") as fp:
		fp.write(data)
	ctx.end_msg(file)


def cmd_configure(ctx, config):
	ctx.load('waf', tooldir='rtems_waf')

	from rtems_waf.config import BuildConfig
	cfg = BuildConfig()


	# Misc funcs
	def yesno(val):
		return "Yes" if val else "No"

	def write_header(header):
		ctx.start_msg("Writing configuration header:")
		ctx.write_config_header(header)
		ctx.end_msg(header, "PINK")

	def msg(str):
		pprint("YELLOW", str)

	def msg_setting(name, val):
		pprint("NORMAL", "  %-30s: " % name, sep="")
		pprint("YELLOW", val)


	######
	# HOST
	######

	msg("")
	msg("--- General Settings ---")
	cfg.config_set(ctx, "general")

	ctx.env.RTEMS_VERSION = "%d.%d.%d" % (config["rtems_version_major"], config["rtems_version_minor"], config["rtems_version_revision"])
	ctx.env.RTEMS_VERSION_DATA = "%d.%d" % (config["rtems_version_major"], config["rtems_version_minor"])

	ctx.env.LIBDIR = "%s/lib" % ctx.env.PREFIX
	ctx.env.BINDIR = "%s/bin" % ctx.env.PREFIX



	msg("")
	msg("--- Host Settings ---")
	ctx.setenv('host', ctx.env.derive())
	ctx.load('compiler_c')
	ctx.load('compiler_cxx')


	if ctx.options.build_config:
		ctx.start_msg('BUILD: Gathering build platform details.')

		# General
		from socket import gethostname
		from waflib.Utils import unversioned_sys_platform
		import platform

		ctx.env.BUILD_HOSTNAME		= gethostname()
		ctx.env.BUILD_PLATFORM		= unversioned_sys_platform()
		ctx.env.BUILD_ARCHITECTURE	= platform.architecture()
		ctx.env.BUILD_MACHINE		= platform.machine()
		ctx.env.BUILD_PLATFORM		= platform.platform()
		ctx.env.BUILD_PYTHON_BUILD	= platform.python_build()
		ctx.env.BUILD_SYSTEM		= platform.system()

		# Unix
		ctx.env.BUILD_SIGNATURE = platform.uname()

		# Linux
		#platform.libc_ver()
		#platform.linux_distribution()

		# Windows
		#platform.win32_ver()

		ctx.end_msg("Done")


	ctx.check_library()
	ctx.check_cc(function_name='strerror', header_name="string.h", mandatory=True)
	ctx.check_cc(function_name='strtol', header_name=["stdlib.h", "limits.h"], mandatory=True)
	ctx.check_cc(function_name='basename', header_name="libgen.h", mandatory=True)

	files = ["getopt.h", "libgen.h"]
	for f in files:
		ctx.check(header_name=f, features='c cprogram')

	# Locate python binary for rtems-config
	ctx.find_program("python", var='BIN_PYTHON')

	# Debug
	if ctx.options.build_json:
		ctx.env.BUILD_JSON = True

	#XXX: TEMP!
	if ctx.options.enable_tests:
		ctx.env.ENABLE_TESTS = True

	cfg.config_set(ctx, "host")
	write_header("host/include/config.h")

	# Set general BSP options
	cfg.config_set(ctx, "bsp")

	# Set timetstamp of config.cfg to enforce re-running configure if it is changed.
	from .tools import get_file_mtime
	ctx.env.CONFIG_TIMESTAMP = get_file_mtime("config.cfg")

	# Always start with a pristeen env while looping.
	env_orig = ctx.env
	for bsp in ctx.env.BSP:

#		if ctx.env.ENABLE_SYSTEM_DEP:
#			from waflib.Tools import c_preproc
#			c_preproc.go_absolute=True

		msg("")
		msg("--- Configuring %s ---" % bsp)
		ctx.setenv(bsp, env_orig.derive())

		(ctx.env.RTEMS_ARCH, ctx.env.RTEMS_BSP) = bsp.split("/")

		if ctx.env.ENABLE_PTHREADS and not ctx.env.ENABLE_POSIX:
			ctx.fatal("Must be built with posix support (ENABLE_POSIX) when using pthreads (ENABLE_PTHREADS)")

		# XXX: Joel says this shouldn't be nessicary.
		if ctx.env.ENABLE_MP and not ctx.env.ENABLE_POSIX:
			ctx.fatal("Must be built with posix support (ENABLE_POSIX) when using MP (ENABLE_MP)")


		# Miscellanous setup.
		ctx.env.RTEMS_VERSION = "%d.%d.%d.%d" % (config["rtems_version_major"], config["rtems_version_minor"], config["rtems_version_revision"], config["rtems_version_patch"])
		ctx.env.RTEMS_VERSION_DATA = "%d.%d" % (config["rtems_version_major"], config["rtems_version_minor"])
		ctx.env.append_value('CFLAGS', '-DHAVE_CONFIG_H')
		ctx.env.append_value('CFLAGS', '-D__rtems_%s_%s__' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_BSP.replace("-", "_")))
		ctx.env.LIBDIR = "%s/lib/rtems/%s/%s-%s/" % (ctx.env.PREFIX, ctx.env.RTEMS_VERSION_DATA, ctx.env.RTEMS_ARCH, ctx.env.RTEMS_BSP)
		ctx.env.BINDIR = ctx.env.LIBDIR

#XXX: Re-add after things are fixed.
		# Enforce required values.
#		required = ["LINKCMDS", "LINK_START", "LINK_END"]
#		for value in required:
#			if not ctx.env[value]:
#				ctx.fatal("%s must be defined in [%s]" % (value, bsp))

		#XXX: ARM hack
		if ctx.env.RTEMS_ARCH == "arm":
			ctx.env.LDFLAGS = ctx.env.CFLAGS


		# Tools.
		ctx.find_program('%s-rtems%s-ar' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_AR', path_list=ctx.env.PATH_TOOLS)
		ctx.find_program('%s-rtems%s-as' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_AS', path_list=ctx.env.PATH_TOOLS)
		ctx.find_program('%s-rtems%s-g++' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_CPP', path_list=ctx.env.PATH_TOOLS, mandatory=False)
		ctx.find_program('%s-rtems%s-gcc' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_CC', path_list=ctx.env.PATH_TOOLS)
		ctx.find_program('%s-rtems%s-ld' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_LD', path_list=ctx.env.PATH_TOOLS)
		ctx.find_program('%s-rtems%s-nm' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_NM', path_list=ctx.env.PATH_TOOLS)
		ctx.find_program('%s-rtems%s-ranlib' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_RANLIB', path_list=ctx.env.PATH_TOOLS)
		ctx.find_program('%s-rtems%s-strip' % (ctx.env.RTEMS_ARCH, ctx.env.RTEMS_VERSION_DATA), var='BIN_RTEMS_STRIP', path_list=ctx.env.PATH_TOOLS)
		ctx.env.AR = ctx.env.BIN_RTEMS_AR
		ctx.env.AS = ctx.env.BIN_RTEMS_AS
		ctx.env.CC = ctx.env.BIN_RTEMS_CC
		ctx.env.CPP = ctx.env.BIN_RTEMS_CPP
		ctx.env.RANLIB = ctx.env.BIN_RTEMS_RANLIB
		ctx.env.STRIP = ctx.env.BIN_RTEMS_STRIP
		ctx.env.LD = ctx.env.BIN_RTEMS_LD
		ctx.env.LINK_CC = ctx.env.BIN_RTEMS_CC
		ctx.env.LINK_CXX = ctx.env.BIN_RTEMS_CCP

		# Config (config.h)
		config_h(ctx)
		config_h_libcpu(ctx)
		version_header_info(ctx, config)
		cpuopts_h(ctx) #XXX: duplicate info.
		write_header("%s/include/config.h" % bsp)

		# BSP options.
		cfg.config_set(ctx, ctx.env.RTEMS_BSP, ctx.env.RTEMS_ARCH)
		bsp_hack(ctx, bsp)
		write_header("%s/include/bspopts.h" % ctx.variant)
		config_h_libbsp(ctx) # Eventually there will be an option to exclude this and replace it with something custom.

		# CPU options.
		cpuopts_h(ctx)
		version_header_info(ctx, config)
		write_header("%s/include/rtems/score/cpuopts.h" % bsp)

		ctx.start_msg('Generating GCC spec file')
		from rtems_waf.tools import generate_gcc_spec_file
		spec_file = generate_gcc_spec_file(ctx, devel=True)
		ctx.end_msg(spec_file)


		depend_version(ctx)
		if ctx.options.build_config:
			build_config(ctx)


		msg("")
		msg("--- Settings for %s ---" % bsp)
		msg_setting("Enable Networking", yesno(ctx.env.ENABLE_NETWORKING))
		msg_setting("Enable Multiprocessing", yesno(ctx.env.ENABLE_MP))
		msg_setting("Enable Multilib", yesno(ctx.env.ENABLE_MULTILIB))
		msg_setting("Enable POSIX", yesno(ctx.env.ENABLE_POSIX))
		msg_setting("Enable SMP", yesno(ctx.env.ENABLE_SMP))
		msg_setting("Enable pthreads", "%s (Depends on POSIX)" % yesno(ctx.env.ENABLE_PTHREADS))
		msg("")
		msg("Build Options")
		msg_setting("CC", " ".join(ctx.env.CC))
		msg_setting("CFLAGS", " ".join(ctx.env.CFLAGS))
		msg_setting("LDFLAGS", " ".join(ctx.env.LDFLAGS))


	# Reset the env back to the original in order to print the proper settings below.
	ctx.setenv("host", env_orig.derive())

	msg("")
	ctx.start_msg('Generating rtems-config')
	from rtems_waf.tools import generate_rtems_config
	generate_rtems_config(ctx, "rtems_waf/rtems_config.py", "rtems-config", devel=True)
	ctx.end_msg("Done")


	msg("")
	msg("--- General Settings (applies to all) --- ")
	msg_setting("Enabled BSPs", ", ".join(ctx.env.BSP))
	msg_setting("Install Prefix", ctx.env.PREFIX)
	msg_setting("Tool Directory", ctx.env.PATH_TOOLS)
	msg("")
	msg("Build Options")
	msg_setting("CFLAGS", " ".join(ctx.env.CFLAGS))
	msg_setting("LDFLAGS", " ".join(ctx.env.LDFLAGS))
	msg_setting("Enable Debug", yesno(ctx.env.ENABLE_DEBUG))



