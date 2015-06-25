import wx 
from py.waf import defaults 
from py.config.tool import get_option_class, get_config_class 
from py.config import RTEMSConfig

class getOptions:
	def __init__(self):
		self.option_class = []
	def run(self):
		'''get dictionary of options from py/waf/defaults/options.py'''
		option = get_option_class(defaults)
	
		'''get list of classes from each file in py/waf/defaults/bsp'''
		config = get_config_class(defaults.bsp)
		
		r = RTEMSConfig(option, config)
		tags = []
		for opt in r.options_get():
			self.option_class.append(opt)

		return self.option_class

	def getTypes(self, option_class):
		self.types = []
		for opt in option_class:
			if opt.__base__.__name__ not in self.types:
				self.types.append(opt.__base__.__name__)
		return self.types

	def getTypeOptions(self, option_class, type):
		self.obj = []
		for opt in option_class:
			if opt.__base__.__name__ == type:
				self.obj.append(opt)
		return self.obj
