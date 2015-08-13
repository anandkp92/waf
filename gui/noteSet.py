#! /usr/bin/env python
# encoding: UTF-8

'''This file creates the tab set to display the options in these multiple tabs'''

import wx
import getOptions
import GOptions
import py.waf.defaults
import py.waf.defaults.bsp
from py.config import BuildConfig, RTEMSConfig
from py.config.tool import get_option_class, get_config_class
from py.waf import defaults

class noteSet:
	'''create a set of tabs - according to the type of the options - Integer/Boolean/String/StringList as of now'''
	def __init__(self, parent, name, style, size, bsp_list):
		self.parent = parent
		nb = wx.Notebook(parent = self.parent, style = style, size = size)
		self.bsp_list = bsp_list
		self.tabs = []
		self.option_gui_list = []

		g = getOptions.getOptions()

		list = []
		for bsp, bsp_class in self.bsp_list:
			list.append(str(bsp))
		
		self.rc = RTEMSConfig(get_option_class(defaults), get_config_class(defaults.bsp))
		self.cfg = BuildConfig(self.rc, list)

		for bsp in self.cfg.cfg:
			option_class = bsp.config_get_class_list()
			#print option_class
			option_class = sorted(option_class, key=self.getName)
			tags = g.getTags(option_class)

			nb2 = wx.Notebook(parent = nb, style = wx.NB_LEFT, size = size)
			for tg in tags:
				tag_specific_options = g.getTagOptions(option_class, tg)
				opt = self.createScrolledWindows(nb2,tag_specific_options)
				option_scrolledwindow = self.getScrolledWindow()
				nb2.AddPage(option_scrolledwindow, tg)
			
			nb.AddPage(nb2, bsp.name)

	def createScrolledWindows(self, parent, option_class):
		'''create each tab - for each type of option [eg. Integer, Boolean etc.] as a scrolled window'''
		#self.parent = parent
		self.base = wx.ScrolledWindow(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
		self.base.SetScrollRate(1, 1)
		self.option_class = option_class

	def getScrolledWindow(self):
		'''create gui object for the each option according to the type'''
		scrolledwindows = []
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

			scrolledwindows.append(p)
			self.option_gui_list.append(p)
		sizer_box = wx.BoxSizer(wx.VERTICAL)
		for p in scrolledwindows:
			sizer_box.Add(p, 0.25,  wx.EXPAND)
			sizer_box.AddSpacer(20)

		self.submit_button = wx.Button(self.base, label = "Submit")
		sizer_box.Add(self.submit_button)
		self.base.Bind(wx.EVT_BUTTON, self.submit_config, self.submit_button)

		sizer_box.Fit(self.base)
		self.base.SetSizer(sizer_box)
		return self.base

	def getName(self,obj):
		'''function to return option name and convert to lower case for sorting'''
		return obj.__name__.lower()

	def submit_config(self, event):
		'''submit the current options and values entered to create the config.cfg file'''
		
		dlg = wx.MessageDialog(self.base, "Confirm submission of current option values?")
                result = dlg.ShowModal()
		if result == wx.ID_OK:
			'''get value of the option from the gui based on type of option'''
			for option_window in self.option_gui_list:
				type = option_window.__class__.__name__
				if type == 'GBoolean':
					option_value = option_window.rbTrue.GetValue()
				elif type == 'GInteger':
					option_value = int(option_window.spinInteger.GetValue())
				elif type == 'GString':
					option_value = str(option_window.textbox.GetValue())
					if option_value == "set value":
						option_value = ""
				elif type == 'GStringList':
					option_value = str(option_window.dropdown.GetValue())
					if option_value == "set value":
						option_value = ""
				else:
					option_value = ""
				option_name = option_window.item1.GetLabel()
				#print option_name
				self.cfg.option_set_gui(self.cfg.cfg, option_name, option_value)

				print type, option_name, option_value
			self.cfg.file_config = "../%s"%self.cfg.file_config
			self.cfg.save()
			##TODO: verify this
			cfgDlg = wx.MessageDialog(self.base, "config.cfg created!", "Success!", wx.OK)
	                result = cfgDlg.ShowModal()
         	        cfgDlg.Destroy()
			#self.parent.Close()
                dlg.Destroy()
