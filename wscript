#! /usr/bin/env python
# encoding: ascii

# RTEMS version, this is the only editable portion of this file.
config = {}
config["rtems_version_major"] = 5
config["rtems_version_minor"] = 0
config["rtems_version_revision"] = 0
config["rtems_version_patch"] = 0

config["rtems_tool_version"] = "4.11"

# --------- DO NOT EDIT BELOW THIS LINE -----------
from sys import argv
from waflib import Task, Scripting, Configure, Utils
from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext, StepContext, ListContext
from waflib.Context import Context
from waflib.Tools import c_preproc
from waflib.Logs import pprint
from rtems_waf.builder import libcpu, libbsp
from rtems_waf.switch import options
from rtems_waf.tools import get_file_mtime
from os.path import exists

# RTEMS Version for waf
VERSION='%d.%d' % (config["rtems_version_major"], config["rtems_version_minor"])
if config["rtems_version_revision"]:
	VERSION = "%s.%d" % (VERSION, config["rtems_version_revision"])
	if config["rtems_version_patch"]: # There can't be a patch version without a revision.
		VERSION = "%s.%d" % (VERSION, config["rtems_version_patch"])

APPNAME='rtems'
class Dist(Scripting.Dist):
	algo = 'tar.bz2' # tar.gz, tar.bz2, tar.xz or zip
	def get_excl(self):
		# do not ship config.cfg in the archive
		return Scripting.Dist.get_excl(self) + ' config.cfg'


pprint.__doc__ = None # Make sure waf doesn't see this as a command.

Configure.autoconfig = 'clobber' # Apply the original configure command-line arguments
Context.repeat_hack = False

top = '.'
out = 'build'
c_preproc.go_absolute = False # Disable dependencies on system headers.
config["variants"] = []

if exists("%s/build/c4che/host_cache.py" % top):
	from waflib.ConfigSet import ConfigSet
	cset = ConfigSet()
	cset.load("build/c4che/host_cache.py")
	config["variants"] = cset.BSP


# Init commands manually to iterate over the variants.
def init_handler(ctx):
	if ctx.cmd == "init_handler" or ctx.cmd == "build":
		context = BuildContext
	elif ctx.cmd == "install":
		context = InstallContext
	elif ctx.cmd == "clean":
		context = CleanContext
	elif ctx.cmd == "uninstall":
		ctx.fatal("This command is not available.")
	elif ctx.cmd == "list":
		context = ListContext
	elif ctx.cmd == "step":
		context = StepContext
	else:
		ctx.fatal("init_handler(): Internal error.")

	# By default we want to itterate over each variant.
	for v in ["host"] + config["variants"]:
		cls = type(context)(v, (context,), {'cmd': ctx.cmd, 'variant': v})
		bld = cls()
		if hasattr(ctx, 'targets'):
			bld.targets = ctx.targets
		pprint("YELLOW", "--- %sing %s ---" % (ctx.cmd, v))
		bld.execute()


# Add target-specific commands.
variant_cmd = (
	("build",	BuildContext),
	("clean",	CleanContext),
	("install",	InstallContext),
	("step",	StepContext),
	("list",	ListContext)
)

host = 1
for variant in ["host"] + config["variants"]:
	if host:
		v = "host"
		host = 0
	else:
		v = variant.split("/")[1]
	for cmd, cls in variant_cmd:
		class tmp(cls):
			__doc__ = "%s %s BSP" % (cmd, v)
			cmd = "%s_%s" % (cmd, v)
			variant = variant

# These will stay local functions to avoid importing the subcommands
# upon every invocation which will happen during regular development.
def cmd_config(ctx):
	from rtems_waf.tools import rtems_cmd_config
	rtems_cmd_config(ctx)

def cmd_docs(ctx):
	from rtems_waf.docs import rtems_cmd_docs
	rtems_cmd_docs(ctx)

def cmd_bsp(ctx):
	from rtems_waf.tools import rtems_cmd_bsp
	rtems_cmd_bsp(ctx)

def cmd_hello(ctx):
	from rtems_waf.hello import rtems_cmd_hello
	rtems_cmd_hello(ctx)

def cmd_info(ctx):
	from rtems_waf.info import rtems_cmd_info
	rtems_cmd_info(ctx)

# List of commands to override / add
commands = (
	("install",		"init_handler", None),
	("uninstall",	"init_handler", None),
	("build",		"init_handler", None),
	("clean",		"init_handler", None),
	("list",		"init_handler", None),
	("step",		"init_handler", None),
	("config",		"cmd_config",	"create config.cfg"),
	("docs",		"cmd_docs",		"build option documentation."),
	("bsp",			"cmd_bsp",		"BSP information."),
	("hello",		"cmd_hello",	"Test command: Build hello.c."),
	("info",		"cmd_info",		"Show build information / configuration.")
)

for command, func, descr in commands:
	class tmp(Context):
		if descr:
			__doc__ = descr
		cmd = command
		fun = func
		if command in 'install uninstall build clean list step docs bsp info':
			execute = Scripting.autoconfigure(Context.execute)


def buildlog(ctx):
	pass
buildlog.__doc__ = "Available only when --build-json and --build-config are used."


# Check sanity of default.cfg
def checkconfig(ctx):
	from rtems_waf.tools import rtems_check_config
	rtems_check_config(ctx)
checkconfig.__doc__ = None # Make sure waf doesn't see this as a command.


def configure(ctx):
	from rtems_waf.configure import cmd_configure
	node = ctx.path.find_node('config.cfg')
	if not node:
		ctx.fatal('Run "waf config" first, for example: waf config --bsp sparc/sis --path-tools ~/development/rtems/4.11/bin')
	# hash the config.cfg file too so that changes in the configure() function will trigger
	# a re-configuration with the original command-line
	ctx.files.append(node.abspath())
	ctx.hash = Utils.h_list((ctx.hash, node.read('rb')))
	# using the standard ctx.recurse() would add the dependency automatically
	node = ctx.path.find_node('rtems_waf/configure.py')
	ctx.files.append(node.abspath())
	ctx.hash = Utils.h_list((ctx.hash, node.read('rb')))
	cmd_configure(ctx, config)

def build(ctx):
	if ctx.env.ENABLE_SYSTEM_DEP:
		c_preproc.go_absolute=True

	ctx.load('waf', tooldir='rtems_waf')

	from rtems_waf.waf import rtems_stlib_command
	class cstlib(Task.classes['cstlib']):
		exec_command = rtems_stlib_command

	# Dump build log in JSON.
	if ctx.cmd == "build" \
		and ctx.env.BUILD_JSON \
		and not Context.repeat_hack:

		from rtems_waf.debug import logger_json_create, exec_command_json, exec_command_json_extra
		Context.repeat_hack = True

		# Make sure any previous handlers are closed so logs are written.
		if hasattr(Context, "logger_json"):
			Context.logger_json.handlers[0].close()

		Context.logger_json = logger_json_create(ctx)
		Context.exec_command = exec_command_json

		# Send extra information from the parent task.
		cls_task = Task.classes["Task"]

		# Avoid recursion since this can be run twice due to host building.
		if not hasattr(cls_task, "exec_command_real"):
			cls_task.exec_command_real = cls_task.exec_command
			cls_task.exec_command = exec_command_json_extra


	# Host is only meant for building host utilities.
	if ctx.variant == "host" and ctx.targets is "":
		ctx.recurse("tools/build")
		ctx.recurse("c")

		# Reset things back so a new log is created for the BSP.
		if ctx.cmd == "build" and ctx.env.BUILD_JSON:
			Context.repeat_hack = False
		return

	# Everything will break if you remove these lines below.
	ctx.cpu = libcpu(ctx)
	ctx.bsp = libbsp(ctx)

	ctx.recurse("cpukit")
	ctx.recurse("cpukit/score")
	ctx.recurse("cpukit/rtems")
	ctx.recurse("cpukit/posix")
	ctx.recurse("cpukit/libcsupport")
	ctx.recurse("cpukit/libfs")
	ctx.recurse("cpukit/libnetworking")
	ctx.recurse("cpukit/librpc")
	ctx.recurse("cpukit/libmisc")
	ctx.recurse("cpukit/zlib")
	ctx.recurse("c")

	if ctx.env.ENABLE_TESTS or "--enable-tests" in argv:
		pprint("YELLOW", "--- building %s tests ---" % ctx.env.BSP[0])
		ctx.recurse("testsuites")

