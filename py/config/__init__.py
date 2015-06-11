from .base import BuildConfig, Config, Default, Feature, Disable

tag_map = {
	"general": "General settings",
	"build":   "Build options",
	"network": "Network option",
	"storage": "Storage option"
}



class RTEMSConfig(object):
	options_map = {}       # Dictionary of options.
	features_list = []     # List of features.
	config_list = []       # List of configs.

	def __init__(self, default, config):
		self.default = default
		self.config = config
