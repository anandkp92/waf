#! /usr/bin/env python
# encoding: UTF-8

'''This file defines functions to get required options, option types and list of options of a particular type'''

import wx 
from py.waf import defaults 
from py.config.tool import get_option_class, get_config_class 
from py.config import RTEMSConfig

class getOptions:
	def __init__(self):
		self.option_class = []

	'''get all option classes'''
	def run(self):
		'''get dictionary of options from py/waf/defaults/options.py'''
		options = get_option_class(defaults)
	
		'''get list of classes from each file in py/waf/defaults/bsp'''
		configs = get_config_class(defaults.bsp)
		
		specific_options = RTEMSConfig(options, configs)
		tags = []
		for opt in specific_options.options_get():
			self.option_class.append(opt)

		return self.option_class

	'''get list of the distinct types of all the options present'''
	def getTypes(self, option_class):
		self.types = []
		for opt in option_class:
			if opt.__base__.__name__ not in self.types:
				self.types.append(opt.__base__.__name__)
		return self.types

	'''get list of all options of a particular type'''
	def getTypeOptions(self, option_class, type):
		self.type_specific_options = []
		for opt in option_class:
			if opt.__base__.__name__ == type:
				self.type_specific_options.append(opt)
		return self.type_specific_options

