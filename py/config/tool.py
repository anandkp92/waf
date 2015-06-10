import inspect


# Collect a list of options from a module.
# XXX: check to make sure only options are fed to this.
def get_option_class(module):
	map = {}
	skip = ("Option", "Boolean", "String", "StringList", "Integer")
	for name, obj in inspect.getmembers(module):
		if inspect.isclass(obj) and name not in skip:
			if name in map:
				raise Exception("Duplicate option: %s" % name)
			map[name] = obj

	return map


