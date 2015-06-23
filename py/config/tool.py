import inspect


# Collect a list of options from a module.
# XXX: check to make sure only options are fed to this, remove the 'skip' list.
def get_option_class(module):
	map = {}
	skip = ("Option", "Boolean", "String", "StringList", "Integer")
	for name, obj in inspect.getmembers(module):
		if inspect.isclass(obj) and name not in skip:
			if name in map:
				raise Exception("Duplicate option: %s" % name)
			map[name] = obj

	return map


# Collect a list of configs from a module
# XXX: Check to make sure only configs are passed to this, remove the 'skip' list.
def get_config_class(module):
	config_list = []
	skip = ("__class__", "Base", "Config")

	for tmp_name, tmp_obj in inspect.getmembers(module): # XXX: This is a hack need to find a better way to 'flatten' the module
		for name, obj in inspect.getmembers(tmp_obj):
			if inspect.isclass(obj) and name not in skip:
				config_list.append(obj)

	return config_list


