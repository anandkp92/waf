#! /usr/bin/env python
# encoding: UTF-8

'''This file creates the tab set to display the options in these multiple tabs'''

import wx
import getOptions
import GOptions
import py.waf.defaults
import py.waf.defaults.bsp

class noteSet:
	'''create a set of tabs - according to the type of the options - Integer/Boolean/String/StringList as of now'''
	def __init__(self, parent, name, style, size, bsp_list):
		nb = wx.Notebook(parent = parent, style = style, size = size)
		self.bsp_list = bsp_list
		self.tabs = []

		g = getOptions.getOptions()
		#option_class = g.run()
		#option_class = sorted(option_class, key=self.getName)
		#tags = g.getTags(option_class)

		list = []
		for bsp, bsp_class in self.bsp_list:
			list.append(str(bsp))
		print list

		
		'''begin: create config file'''
		from py.config import BuildConfig, RTEMSConfig
		from py.config.tool import get_option_class, get_config_class
		from py.waf import defaults

		rc = RTEMSConfig(get_option_class(defaults), get_config_class(defaults.bsp))
		cfg = BuildConfig(rc, list)
		cfg.save()
		'''end: create config file'''
		
		for bsp, bsp_class in self.bsp_list:
			print bsp_class.__module__ #py.waf.defaults.bsp.sparc
			print bsp #sparc/sis
			print bsp.split("/")[0] #sparc
			print bsp_class #<class py.waf.defaults.bsp.sparc.sis>

			###below already written
			option_class = g.run(bsp_class.__module__)
			option_class = sorted(option_class, key=self.getName)
			print len(option_class)
			tags = g.getTags(option_class)

			nb2 = wx.Notebook(parent = nb, style = wx.NB_LEFT, size = size)
			for tg in tags:
				tag_specific_options = g.getTagOptions(option_class, tg)
				opt = self.createScrolledWindows(nb2,tag_specific_options)
				option_scrolledwindow = self.getScrolledWindow()
				nb2.AddPage(option_scrolledwindow, tg)
			
			nb.AddPage(nb2, bsp)

	def createScrolledWindows(self, parent, option_class):
		'''create each tab - for each type of option [eg. Integer, Boolean etc.] as a scrolled window'''
		self.parent = parent
		self.base = wx.ScrolledWindow(self.parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
		self.base.SetScrollRate(1, 1)
		self.scrolledwindows = []
		self.option_class = option_class

	def getScrolledWindow(self):
		'''instiate the gui object for the options according to the type'''
		for opt in self.option_class:
			n = opt.__name__
			d = opt.descr
			if hasattr(opt, 'value'):
				v = opt.value
			else:
				v = "must set value"
			if opt.__base__.__name__ == 'Boolean':
				p = GOptions.GBoolean(self.base, n, d, v)
			elif opt.__base__.__name__ == 'Integer':
				p = GOptions.GInteger(self.base, n, d, v)
			elif opt.__base__.__name__ == 'String':
				p = GOptions.GString(self.base, n, d, v)
			elif opt.__base__.__name__ == 'StringList':
				p = GOptions.GStringList(self.base, n, d, v)
			else:
				p = GOptions.BaseScrolledWindow(self.base, n, d, v)

			self.scrolledwindows.append(p)
		sizer_box = wx.BoxSizer(wx.VERTICAL)
		for p in self.scrolledwindows:
			sizer_box.Add(p, 0.25, wx.EXPAND)
			sizer_box.AddSpacer(20)

		sizer_box.Fit(self.base)
		self.base.SetSizer(sizer_box)
		return self.base

	def getName(self,obj):
		'''function to return option name and convert to lower case for sorting'''
		return obj.__name__.lower()
