from subprocess import Popen, PIPE
from .tools import run
from waflib.ConfigSet import ConfigSet

def rtems_cmd_hello(ctx):
	c = ConfigSet("build/c4che/_cache.py")
	for bsp in c.BSP:
		print("\nBUILDING: %s" % bsp)
		a, b = bsp.split("/")
		c = ConfigSet("build/c4che/%s/%s_cache.py" % (a, b))

		cflags, cf_stderr, cf_rc = run(["./rtems-config", "--bsp=%s" % bsp, "--cflags"])
		ldflags, ld_stderr, ld_rc = run(["./rtems-config", "--bsp=%s" % bsp, "--ldflags"])

		if cf_rc or ld_rc:
			print(cf_stderr)
			print(ld_stderr)

		cmd = c.BIN_RTEMS_CC
		cmd += cflags.decode("utf-8").split(" ")
		cmd.append("-o")
		cmd.append("/tmp/hello")
		cmd.append("testsuites/samples/hello/init.c")
		cmd += ldflags.decode("utf-8").split(" ")

		print(" ".join(cmd))
		stdout, stderr, returncode = run(cmd)

		if stdout:
			print(stdout)
		if stderr:
			print(stderr)

		if cf_rc or ld_rc or returncode:
			ctx.fatal("Compilation Failed")
