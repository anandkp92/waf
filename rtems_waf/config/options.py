from textwrap import TextWrapper
from .base import options_map
from rtems_waf.compat import add_metaclass # 2to3

wrapper = TextWrapper()
wrapper.width = 75
wrapper.initial_indent = "# "
wrapper.subsequent_indent = "# "



class OptionMeta(type):
	"""Self register options."""
	skip = ("Option", "Boolean", "String", "StringList", "Integer")
	def __new__(cls, name, bases, dct):
		new = type.__new__(cls, name, bases, dct)
		if name not in cls.skip:
			if name in options_map:
				raise Exception("Duplicate option: %s" % name)
			options_map[name] = new
		return new

@add_metaclass(OptionMeta)
class Option(object):
	"""
		Base class for all Options

		.. py:attribute:: undef=True

			Whether to undefine the option in the header file when "disabled".

		.. py:attribute:: limit=None

			List or min,max to restrict the option to.  Depends on option type.

		.. py:attribute:: quote=False

			Whether to quote the value in the header.
	"""

	def __init__(self, value=None):
		self.name = self.__class__.__name__


		# Do not set a default if no_default set.
		if not hasattr(self, "no_default"):
			self.no_default = True

		# Whether to quote the value
		if not hasattr(self, "quote"):
			self.quote = False

		# Value limit
		if not hasattr(self, "limit"):
			self.limit = None

		if value is not None:
			self.validate(value)
			self.value = value
		elif self.no_default and not hasattr(self, "value"):
			raise Exception("no_default is set you must supply a value in bsp config")
		else:
			self.validate(self.value)

	def __add__(self, value):
		"""
			Hack around only a _set. Need a _convert and _set in each type of option.
	
			:rtype: Depends on subclass
			:return: Two options added together
		"""
		current = self.value
		self._set(value)
		optsum = self.value
		self.value = current
		return current + optsum


	def validate(self, value):
		"""Validate option."""
		self._fatal("Must be set in subclass.")


	def set(self, value):
		"""Set option value"""
		if value is None:
#			self.value = self.default #XXX: why is this here, a artifact?
			return

		self._set(value)


	def _fatal(self, str):
		"""Fatal error"""
		print("Fatal->%s.%s: %s" % (self.__class__.__bases__[0].__name__, self.__class__.__name__, str))
		exit(1)


	def config_get(self):
		"""
		Get string suitable for config.cfg

		:rtype: string
		:return: Pre-formatted Windows `.ini` block.
		"""

		opt = []
		opt += wrapper.wrap(self.descr.strip())
		opt += ["%s = %s" % (self.__class__.__name__, self._str_value())]
		return "\n".join(opt)


	def _str_value(self):
		"""
			Get option as a string.

		:rtype: string
		:return: Option value as a string.
		"""
		raise Exception("Needs to be implmented in subclass.")


	def set_config_header(self, ctx):
		"""
			1. If value is an integer always define it beacuse it could be 0.
			2. If value is empty "" or boolean=False undefine it
			3. if self.undef == True (undefine if false) undefine it.

			:param ctx: waf context
		"""
		if type(self.value) is not int and not self.value and self.undef:
			ctx.undefine(self.name)
			return
		self._set_config_header(ctx)


	def set_config_build(self, ctx):
		"""
			Set option inside waf as part of the build.

			:param ctx: waf context
		"""
		if type(self.value) is list:
			ctx.env.append_value(self.name, self.value)
		else:
			setattr(ctx.env, self.name, self.value)



class Boolean(Option):
	"""Boolean option value."""

	def validate(self, value):
		"""Validate as one of: 1, 0, true, false"""

		if type(value) is not bool:
			self._fatal("Not a boolean value (True|False): %s" % type(value))

	def _str_value(self):
		return str(self.value)

	# XXX: This is wrong (works for now!)
	def _set(self, value):

		if type(value) is str:
			if value.lower() == "true":
				value = True
			elif value.lower() == "false":
				value = False
			else:
				self._fatal("Internal error in Boolean._set()")

		self.validate(value)
		self.value = value

	def _set_config_header(self, ctx):
		"""Set value in config header."""

		if self.undef:
			ctx.define_cond(self.name, 1 if self.value else 0)
		else:
			ctx.define(self.name, 0)




class String(Option):
	def validate(self, value):
		"""Verify value is a string and is in `limit` if defined."""
		if type(value) is not str:
			self._fatal("Not a string: %s (%s)" % (value, type(value)))

		if self.limit:
			if type(limit) is not list:
				self._fatal("Only lists are supported as a limiter for strings.")

			if value not in limit:
				self._fatal("%s not in list of accepted values: %s" % (value, limit))

	def _str_value(self):
		return self.value

	def _set(self, value):
		"""Set string, strips bounding whitespace."""
		self.validate(value)
		self.value = value.strip()

	def _set_config_header(self, ctx):
		"""Define in header."""
		ctx.define(self.name, self.value, quote=self.quote)


class StringList(Option):
	def validate(self, value):
		"""Validate list of strings"""
		if type(value) is not list:
			self._fatal("Not a list: %s (%s)" % (value, type(value)))

		for v in value:
			if type(v) is not str:
				self._fatal("Value %s is not a String." % v)

#XXX: Needs to be fixed.
#		if self.limit:
#			if type(limit) is not list:
#				self._fatal("Only lists are supported as a limiter for strings.")

#			if value not in limit:
#				self._fatal("%s not in list of accepted values: %s" % (value, limit))

	def _str_value(self):
		return " ".join(self.value)

	def _set(self, value):
		"""Make sure value is a list otherwise split into one delimited by whitespace."""

		if type(value) is not list:
			value = value.split(" ")
			value = [x for x in value if x]

		self.validate(value)
		self.value = value

	def _set_config_header(self, ctx):
		ctx.define(self.name, self.value, quote=self.quote)



class Integer(Option):
	def validate(self, value):
		"""Verify value is an int and in limit if defined."""
		if type(value) is not int:
			self._fatal("Not an integer: %s (%s)" % (value, type(value)))

		if self.limit:
			if type(limit) is list:
				if value not in limit:
					self._fatal("%s not in list of accepted values: %s" % (value, limit))

			if type(limit) is tuple:
				min, max = limit
				if value < min or value > max:
					self._fatal("%s is outside min/max: %s/%s" % (value, min, max))

	def _str_value(self):
		return str(self.value)

	def _set(self, value):
		self.validate(value)
		v = int(value) #XXX: Is this even needed?  an artifact?
		self.value = v

	def _set_config_header(self, ctx):
		ctx.define(self.name, self.value, quote=self.quote)
