from .base import BuildConfig, Config, Default, Feature, Disable
from .options import Option, Boolean, String, StringList, Integer
from .tag import tag_map

class RTEMSConfig(object):

	def __init__(self, default, config):
		self.default = default	# Dictionary of options.
		self.config = config	# List of configs.
#		self.config = feature	# List of features.

	# Return sorted list of options
	def options_get(self, category=False):

		if category:
			tmp = {}
			for name, option in self.default.items():
				if not set(category).isdisjoint(option.tag):
					tmp[name] = option
			return [v for (k, v) in sorted(tmp.items())]

		return [v for (k, v) in sorted(self.default.items())]
