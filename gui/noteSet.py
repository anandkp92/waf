#! /usr/bin/env python
# encoding: UTF-8

'''This file creates the tab set to display the options in these multiple tabs'''

import wx
import getOptions
import GOptions

class noteSet:
	'''create a set of tabs - according to the type of the options - Integer/Boolean/String/StringList as of now'''
	def __init__(self, parent, name, style, size):
		nb = wx.Notebook(parent = parent, style = style, size = size)
		self.tabs = []
		#self.names = []
		#self.p = []

		g = getOptions.getOptions()
		option_class = g.run()
		types = g.getTypes(option_class)
		
		for t in types:
			type_specific_options = g.getTypeOptions(option_class, t)
			opt = self.createScrolledWindows(nb,type_specific_options)
			option_scrolledwindow = self.getScrolledWindow()
			nb.AddPage(option_scrolledwindow, t)

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


