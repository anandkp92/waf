# Compat code for python 2<->3.


# Borrowed from the Six package: https://pypi.python.org/pypi/six
# Copyright (c) 2010-2015 Benjamin Peterson
def add_metaclass(metaclass):
	"""Class decorator for creating a class with a metaclass."""
	def wrapper(cls):
		orig_vars = cls.__dict__.copy()
		slots = orig_vars.get('__slots__')
		if slots is not None:
			if isinstance(slots, str):
				slots = [slots]
			for slots_var in slots:
				orig_vars.pop(slots_var)
		orig_vars.pop('__dict__', None)
		orig_vars.pop('__weakref__', None)
		return metaclass(cls.__name__, cls.__bases__, orig_vars)
	return wrapper

