from waflib.ConfigSet import ConfigSet

def system(ctx):
	info = {}

	from waflib.Utils import unversioned_sys_platform
	info["platform_waf"] = unversioned_sys_platform()

	from multiprocessing import cpu_count
	info["cpu_count"] = cpu_count()

	# platform information
	import platform
	methods = [
		"machine",
		"platform",
		"processor",
		"python_build",
		"python_version",
		"python_version_tuple",
		"system",
#		"system_alias",
		"release",
#		"version",
#		"uname",
		"win32_ver",
		"mac_ver",
		"linux_distribution"
	]
	for method in methods:
		info[method] = getattr(platform, method)()

	return info


def rtems(ctx):
	info = {}

	c = ConfigSet("build/c4che/_cache.py")


	info["version"] = c.RTEMS_VERSION

	info["bsp"] = {}
	for bsp in c.BSP:
		a, b = bsp.split("/")
		c = ConfigSet("build/c4che/%s/%s_cache.py" % (a, b))

		b = {}

		info["bsp"][bsp] = b

	return info


def rtems_cmd_info(ctx):
	info = {}

	info["system"] = system(ctx)
	info["rtems"] = rtems(ctx)


	for val in sorted(info):
		print("\n%s" % val)
		for v in sorted(info[val]):
			print("    %s = %s" % (v, info[val][v]))

#	import pprint
#	pp = pprint.PrettyPrinter(indent=4)
#	pp.pprint(info)


