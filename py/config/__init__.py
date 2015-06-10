from .base import BuildConfig, Config, Default, Feature, Disable
#from .feature import *
#from .options import *

class RTEMSConfig(object):
	options_map = {}       # Global options map.
	features_list = []     # Global features list.
	config_list = []       # Global config list.

	def __init__(self, default, config):
		self.default = default
		self.config = config
