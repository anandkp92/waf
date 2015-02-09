try:
	from configparser import ConfigParser, NoOptionError
except:
	from ConfigParser import ConfigParser, NoOptionError

from os.path import exists
#from __init__ import options_map, Default, features_list, config_list
from rtems_waf.compat import add_metaclass #2to3
from sys import version_info

Default = None			# Default value.
Disable = "-DISABLED-"	# Disable this option
options_map = {}		# Global options map.
features_list = []		# Global features list.
config_list = []		# Global config list.


def fatal(str):
	print("FATAL: %s" % str)
	exit(1)


class Value(object):
	"""Holds an option value internally.  This acts in a similar fashion to a dictionary."""

	def __init__(self):
		self.__dict__["options"] = {}

	def __setattr__(self, key, value):
		"""Set a value, this either fetches the option or sets it if it already exists."""
		self._set_or_get(key, value)

	def __getitem__(self, key):
		"""Get an option from the internal table."""
		return self.options[key]

	def __getattr__(self, key):
		"""Allow an option to be fetched as an attribute."""
		return self.options[key]

	def _set_or_get(self, option, value):
		"""
			Set or get an option.

			:param option: Option name (string)
			:param value: Value to set option
		"""

		# Disabling an option removes it from the header completely irrespective of its type.
		if type(value) == str and value == "-DISABLED-":
			del self.options[option]
			return

		if option not in self.options:
			if option not in options_map:
				fatal("Missing default option: %s" % option)
			opt = options_map[option]	# Get option class
			i = opt(value)				# Create option with value
			self.options[i.name] = i	# Set in dictionary
		else:
			i = self.options[option]
			i.set(value)				# Set value

	def __str__(self):
		"""String representation of a value object."""
		return "Value object at %s: %s" % (hex(id(self)), self.value)

	def __iter__(self):
		"""Allow iteration."""
		return iter(self.options)



# Self register configs.
class ConfigMeta(type):
	"""Automatically register configs classes."""
	def __new__(cls, name, bases, dct):
		new = type.__new__(cls, name, bases, dct)
		if hasattr(new, "is_feature") and new.is_feature is True: # XXX: Find a better way to differentiate.
			features_list.append(new)
		elif hasattr(new, "name"):
			config_list.append(new)
		return new

@add_metaclass(ConfigMeta)
class Config(object):
	feature = () 							#: Feature list (XXX: Why is this required?)
	feature_default = ("gcc", "debug")		#: Default features.

	def __init__(self):
		self.base = False					#: Whether this is a base config or not.
		self.option_header = Value()		#: Internal header options
		self.option_build = Value()			#: Internal build options

		# Iterate over base classes in reverse order so the 'latest'
		# defined option is taken.
		for i in type(self).__mro__[::-1]:
			if hasattr(i, "header"):
				i.header(self, self.option_header)
			if hasattr(i, "build"):
				i.build(self, self.option_build)

		# Make sure features don't conflict with each other.
		processed = []
		feature_obj = [x for x in features_list if x.name in self.feature]
		for feature in feature_obj:
			conflicts = set(processed) & set(feature.conflicts)
			processed.append(feature.name)
			if conflicts:
				raise Exception("Feature %s conflicts with %s" % (feature.name, ", ".join(conflicts)))
			feature(self)

		self.feature += self.feature_default	# Features in this config


	def header(self, c):
		"""
			Header config options.

			:param c: `self.option_header`
		"""
		pass


	def build(self, c):
		"""
			Build config options.

			:param c: `self.build_header`
		"""
		pass

	# XXX: needs to merge both dictionaries and sort them.
	def config_get(self):
		"""Get the config.cfg (.ini) format for this config."""
		str = "[%s]\n" % self.name
		def add(d, str):
			for o in sorted(d):
				opt = d[o]
				str += "%s" % opt.config_get()
				str += "\n\n"
			return str

		str = add(self.option_header, str)
		str = add(self.option_build, str)
		return str




class Feature(Config):
	"""Build feature base class"""
	name = None			#: Name of feature
	description = None	#: Description
	exclude = None		#: BSPs to exclude
	include = None		#: BSPs to include
	conflicts = None	#: Other features this one conflicts with
	is_feature = True	#: Whether this is a feature or not

	def __init__(self, parent):
		self.build(parent.option_build)
		self.header(parent.option_header)

	def __str__(self):
		return "%s (%s)" % (self, self.name)



class cfg_general(Config):
	"""[general] block for `config.cfg.`"""
	name = "general"
	def build(self, c):
		c.BSP					= Default
		c.PREFIX				= Default
		c.PATH_TOOLS			= Default
		c.ENABLE_DEBUG			= Default
		c.CFLAGS				= Default
		c.LIBS					= Default
		c.LDFLAGS				= Default


class cfg_host(Config):
	"""[host] block for `config.cfg.`"""
	name = "host"
	def build(self, c):
		c.CFLAGS				= Default
		c.LIBS					= Default
		c.LDFLAGS				= Default


class cfg_bsp(Config):
	"""[bsp] block for `config.cfg` to hold BSP-specific settings"""
	name = "bsp"
	def build(self, c):
		c.ENABLE_DEBUG			= Default
		c.ENABLE_MP				= Default
		c.ENABLE_MULTILIB		= Default
		c.ENABLE_NETWORKING		= Default
		c.ENABLE_NEWLIB			= Default
		c.ENABLE_POSIX			= Default
		c.ENABLE_PTHREADS		= Default
		c.ENABLE_SERDBG			= Default
		c.ENABLE_SHELL			= Default
		c.ENABLE_SMP			= Default
		c.LINK_START			= Default
		c.LINK_END				= Default
		c.LINK_LINK				= Default





class BuildConfig(object):
	"""
		This class handles creating and loading `config.cfg`.
	"""
	file_config = "config.cfg"	#: Default config file name.

	def __init__(self, list_bsp=[]):
		self.cfg_default = [cfg_general(), cfg_host(), cfg_bsp()]	#: Default BSP configuration.
		self.cfg = list(self.cfg_default)							#: BSP config.
		self.list_bsp = []

		if list_bsp:
			self.list_bsp = sorted(list_bsp)
		elif not exists(self.file_config):
			fatal("Missing config.cfg")
		else:
			# Load on-disk config.
			self.cfg_user = ConfigParser()
			self.cfg_user.read(self.file_config)

			# Set BSP list.
			# XXX: Far too complicated due to chicken-and-egg issue.
			#      This will be refactored in the future.
			tmp = cfg_general()
			opt = tmp.option_build["BSP"]
			o = self.cfg_user.get("general", "BSP")
			if version_info < (3,) and type(o) is unicode: #2to3
				o = str(o)
			opt.set(o)
			self.list_bsp = opt.value

		# Parse BSPs
		self._parse_bsp(self.list_bsp)

		# Load user configuration
		if not list_bsp:
			self._cfg_user_load()

		# Make sure BSP= is always set.
		self.option_set("general", "BSP", " " .join(self.list_bsp))


	def _parse_bsp(self, list_bsp):
		"""
			Parse BSP config.

			:param: list_bsp: List of BSPs in this config.
		"""

		# Make this simplier
		bsp_map = {}
		for b in self.list_bsp:
			bsp = [x for x in config_list if x.name == b][0]
			bsp_arch = [x for x in config_list if x.name == bsp.arch][0]
			bsp_map.setdefault((bsp_arch.name, bsp_arch), []).append(bsp)

		# Save for usage in config_set
		self.bsp_map = bsp_map

		for bsp_name, bsp_arch in sorted(bsp_map):
			self.cfg.append(bsp_arch())
			for bsp in bsp_map[(bsp_name, bsp_arch)]:
				self.cfg.append(bsp())


	def save(self):
		"""Save config to disk."""
		with open(self.file_config, "w") as fp:
			fp.write(self._cfg_get())
			fp.write("\n\n") # Handy.


	def config_set(self, ctx, cfg_name, arch_name=None):
		"""
			Apply config internally to waf.

		:param ctx: waf Context.
		:param cfg_name: BSP config name (arch/bsp format).
		:param arch_name: Architecture name.
		"""
		cfg = None
		if arch_name:
#			self.config_set(ctx, arch_name)
			cfg_name = "%s/%s" % (arch_name, cfg_name)

		for c in self.cfg:
			if c.name == cfg_name:
				cfg = c
				break

		if not cfg:
			fatal("BuildConfig:config_set(): Invalid config: %s" % cfg_name)

		for option in cfg.option_build:
			opt = cfg.option_build[option]
#			self._set_cfg_user(cfg_name, opt)
			opt.set_config_build(ctx)

		for option in cfg.option_header:
			opt = cfg.option_header[option]
#			self._set_cfg_user(cfg_name, opt)
			opt.set_config_header(ctx)


	def bsp_get_detail(self, arch, bsp):
		cfg = None

		for c in config_list:
			if c.name == "%s/%s" % (arch, bsp):
				cfg = c
				break

		if cfg is None:
			return "MISSING" # XXX: Throw an exception if this is missing?

		return "."


	def option_set(self, cfg, option, value):
		"""
			Set an option within a config

			:param cfg: Config to set.
			:param option: Option name.
			:param value: Value to set.
		"""
		for config in self.cfg_default:
			if config.name == cfg:
				# Only allow build options to be set for now.
				for o in config.option_build:
					opt = config.option_build[o]
					if opt.name == option:
						opt.set(value)

	def _cfg_get(self):
		"""Get config text."""
		cfg = ""
		for bsp in self.cfg:
			cfg += "\n\n"
			cfg += bsp.config_get()
		return cfg.strip()


	#XXX: unused
	def _cfg_add(self, str):
		self.cfg += "\n"
		self.cfg += str


	def _cfg_user_load(self):
		"""Load user config from disk."""
		for cfg_bsp in self.cfg:
			section = cfg_bsp.name

			if not self.cfg_user.has_section(section):
				fatal("Missing section: [%s]" % section)

			for option in cfg_bsp.option_build:
				opt = cfg_bsp.option_build[option]

				o = self.cfg_user.get(section, opt.name)

				# configpaser does not convert values anymore.
				if o in ["True", "False"]:
					o = self.cfg_user.getboolean(section, opt.name)

				# We do not support unicode internally
				if version_info < (3,) and type(o) is unicode: #2to3
					o = str(o)

				self._set_cfg_user(section, opt)

#				opt.set(o)

			for option in cfg_bsp.option_header:
				opt = cfg_bsp.option_header[option]
				self._set_cfg_user(section, opt)
#				o = self.cfg_user.get(section, opt.name)
#				opt.set(o)


	def _set_cfg_user(self, section, opt):
		if not self.cfg_user.has_section(section):
			fatal("Missing section: [%s]" % section)

		o = self.cfg_user.get(section, opt.name)

		# configpaser does not convert values anymore.
		if o in ["True", "False"]:
			o = self.cfg_user.getboolean(section, opt.name)

		# We do not support unicode internally
		if version_info < (3,) and type(o) is unicode: #2to3
			o = str(o)

		opt.set(o)






# This needs to be here to avoid recursive deps, it's more convenient to
# have the features in a seperate file.
#import feature
#import rtems_waf.defaults.bsp
