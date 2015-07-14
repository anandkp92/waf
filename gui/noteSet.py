#! /usr/bin/env python
# encoding: UTF-8

import wx
import getOptions

'''create a set of tabs - according to the type of the options - Integer/Boolean/String/StringList as of now'''
class noteSet:
	def __init__(self, parent, name, style, size):
		nb = wx.Notebook(parent = parent, style = style, size = size)
		self.tabs = []
		#self.names = []
		#self.p = []

		g = getOptions.getOptions()
		option_class = g.run()
		types = g.getTypes(option_class)
		
		'''create tab for each type of option and add it to the set of tabs'''
		for t in types:
			type_specific_options = g.getTypeOptions(option_class, t)
			opt = createScrolledWindows(nb, type_specific_options)
			option_scrolledwindow = opt.getScrolledWindow()
			nb.AddPage(option_scrolledwindow, t)

'''create each tab - for each type of option [eg. Integer, Boolean etc.] as a scrolled window'''
class createScrolledWindows:
	def __init__(self, parent, option_class):
		self.parent = parent
		self.base = wx.ScrolledWindow(self.parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
		self.base.SetScrollRate(1, 1)
		self.scrolledwindows = []
		self.option_class = option_class

	def getScrolledWindow(self):
		for opt in self.option_class:
			n = opt.__name__
			d = opt.descr
			if hasattr(opt, 'value'):
				v = opt.value
			else:
				v = "must set value"
			if opt.__base__.__name__ == 'Boolean':
				p = GBoolean(self.base, n, d, v)
			elif opt.__base__.__name__ == 'Integer':
				p = GInteger(self.base, n, d, v)
			elif opt.__base__.__name__ == 'String':
				p = GString(self.base, n, d, v)
			else:
				p = BaseScrolledWindow(self.base, n, d, v)

			self.scrolledwindows.append(p)
		sizer_box = wx.BoxSizer(wx.VERTICAL)
		for p in self.scrolledwindows:
			sizer_box.Add(p, 0.25, wx.EXPAND)
			sizer_box.AddSpacer(20)

		sizer_box.Fit(self.base)
		self.base.SetSizer(sizer_box)
		return self.base

'''Base Panel for all options (irrespective of type) - creates scrollable window with common attributes and reset button'''
class BaseScrolledWindow(wx.ScrolledWindow):
	def __init__(self, parent, name, desc, value):
		wx.ScrolledWindow.__init__(self, parent=parent, id = wx.ID_ANY, style=wx.BORDER_SIMPLE)

		self.value = value
 		self.item1 = wx.StaticText(self, -1, label = name)
		self.item1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
		self.item2 = wx.StaticText(self, -1, label = "Description : %s" % desc)
		self.item3 = wx.StaticText(self, -1, label = "Default Value : %s" % self.value)
		self.item4 = wx.Button(self, -1, "Reset")

		self.item4.Disable()
		self.boxSizer = wx.BoxSizer(wx.VERTICAL)

		self.boxSizer.Add(self.item1, 0.5, wx.EXPAND)
		self.boxSizer.Add(self.item2, 0.5, wx.EXPAND)
		self.boxSizer.Add(self.item3, 0.5, wx.EXPAND)
		self.boxSizer.Add(self.item4, wx.EXPAND)
		self.SetSizer(self.boxSizer)

'''Panel to include Boolean options over Base Panel - Radio Buttons for True/False and event handlers'''
class GBoolean(BaseScrolledWindow):
	def __init__(self, parent, name, desc, value):
		BaseScrolledWindow.__init__(self, parent, name, desc, value)
		self.smallPanel = wx.Panel(self)
		self.boxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
		self.rbTrue = wx.RadioButton(self.smallPanel, id=wx.ID_ANY, label = "True", style=wx.RB_GROUP)
		self.rbFalse = wx.RadioButton(self.smallPanel, id=wx.ID_ANY, label = "False")
		
		self.Bind(wx.EVT_RADIOBUTTON, self.radio_event, self.rbTrue)
		self.Bind(wx.EVT_RADIOBUTTON, self.radio_event, self.rbFalse)
		self.Bind(wx.EVT_BUTTON, self.OnButtonClicked, self.item4)

		'''Initially Set value to the Default Value'''
		if self.value == True:
			self.rbTrue.SetValue(True)
		else:
			self.rbFalse.SetValue(True)
		
		self.boxSizer2.Add(self.rbTrue, 0.25, wx.EXPAND)
		self.boxSizer2.Add(self.rbFalse, 0.25, wx.EXPAND)
		self.smallPanel.SetSizer(self.boxSizer2)

		self.boxSizer.Add(self.smallPanel, 0.25, wx.EXPAND)
		self.SetSizer(self.boxSizer)
	
	'''If currently chosen value is not the default value, enable Reset button, else disable it'''
	def radio_event(self, event):
		radioSelected = event.GetEventObject()
		if self.value != True and self.value != False:
			self.item4.Disable()
		elif radioSelected.GetLabel() != str(self.value):
			self.item4.Enable()
		elif radioSelected.GetLabel() == str(self.value):
			self.item4.Disable()

	'''change value chosen to default value on Reset Button Click'''
	def OnButtonClicked(self, event):
		if self.value == True:
			self.rbTrue.SetValue(True)
			self.rbFalse.SetValue(False)
		elif self.value == False:
			self.rbFalse.SetValue(True)
			self.rbTrue.SetValue(False)
		event.GetEventObject().Disable()

'''Panel to include Integer options over Base Panel - Spin Control for entering integers and event handlers'''
class GInteger(BaseScrolledWindow):
	def __init__(self, parent, name, desc, value):
		BaseScrolledWindow.__init__(self, parent, name, desc, value)
                self.smallPanel = wx.Panel(self)
                self.boxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
		
		'''Maximum default value currently for Integer options is 128000000 (pll output clock frequency)'''
		#M is currently set to largest default value present
		M = 128000000
		self.spinInteger=wx.SpinCtrl(self.smallPanel,id=wx.ID_ANY, value=str(self.value), max=M,style=wx.SP_ARROW_KEYS)

                self.Bind(wx.EVT_SPINCTRL, self.OnSpin, self.spinInteger)
                self.Bind(wx.EVT_BUTTON, self.OnButtonClicked, self.item4)

                self.boxSizer2.Add(self.spinInteger, 0.25, wx.EXPAND)
                self.smallPanel.SetSizer(self.boxSizer2)

                self.boxSizer.Add(self.smallPanel, 0.25, wx.EXPAND)
                self.SetSizer(self.boxSizer)

	'''If chosen value is not the default value, enable Reset button, else disable it'''
	def OnSpin(self, event):
		obj = event.GetEventObject()
		if obj.GetValue() == self.value:
			self.item4.Disable()
		else:
			self.item4.Enable()

	'''change value chosen to default value on Reset Button Click'''
	def OnButtonClicked(self, event):
		self.spinInteger.SetValue(self.value)
		event.GetEventObject().Disable()

'''Panel to include String options over Base Panel - Text Control for entering strings and event handlers'''
class GString(BaseScrolledWindow):
	def __init__(self, parent, name, desc, value):
		BaseScrolledWindow.__init__(self, parent, name, desc, value)

		if self.value == "":
			self.value = "set value"

                self.smallPanel = wx.Panel(self)
                self.boxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
		
		self.textbox=wx.TextCtrl(self.smallPanel,id=wx.ID_ANY, value=str(self.value))

                self.boxSizer2.Add(self.textbox, 0.25, wx.EXPAND)
                self.smallPanel.SetSizer(self.boxSizer2)

                self.Bind(wx.EVT_TEXT, self.OnTextEntered, self.textbox)
                self.Bind(wx.EVT_BUTTON, self.OnButtonClicked, self.item4)

                self.boxSizer.Add(self.smallPanel, 0.25, wx.EXPAND)
                self.SetSizer(self.boxSizer)

	'''If chosen value is not the default value, enable Reset button, else disable it'''
	def OnTextEntered(self, event):
		obj = event.GetEventObject()
		if self.value == "set value":
			self.item4.Disable()
		elif obj.Value == self.value:
			self.item4.Disable()
		else:
			self.item4.Enable()

	'''change value chosen to default value on Reset Button Click'''
	def OnButtonClicked(self, event):
		self.textbox.SetValue(self.value)
		event.GetEventObject().Disable()
