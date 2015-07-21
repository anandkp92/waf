import wx

'''This file contains the Base Panel for displaying options with type specific additions'''

class BaseScrolledWindow(wx.ScrolledWindow):
	'''Base Panel for all options (irrespective of type) - creates scrollable window with common attributes and reset button'''
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

class GBoolean(BaseScrolledWindow):
	'''Panel to include Boolean options over Base Panel - Radio Buttons for True/False and event handlers'''
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
	
	def radio_event(self, event):
		'''If currently chosen value is not the default value, enable Reset button, else disable the radio button'''
		radioSelected = event.GetEventObject()
		if self.value != True and self.value != False:
			self.item4.Disable()
		elif radioSelected.GetLabel() != str(self.value):
			self.item4.Enable()
		elif radioSelected.GetLabel() == str(self.value):
			self.item4.Disable()

	def OnButtonClicked(self, event):
		'''change value chosen to default value on Reset Button Click'''
		if self.value == True:
			self.rbTrue.SetValue(True)
			self.rbFalse.SetValue(False)
		elif self.value == False:
			self.rbFalse.SetValue(True)
			self.rbTrue.SetValue(False)
		event.GetEventObject().Disable()

class GInteger(BaseScrolledWindow):
	'''Panel to include Integer options over Base Panel - Spin Control for entering integers and event handlers'''
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

	def OnSpin(self, event):
		'''If chosen value is not the default value, enable Reset button, else disable it'''
		obj = event.GetEventObject()
		if obj.GetValue() == self.value:
			self.item4.Disable()
		else:
			self.item4.Enable()

	def OnButtonClicked(self, event):
		'''change value chosen to default value on Reset Button Click'''
		self.spinInteger.SetValue(self.value)
		event.GetEventObject().Disable()

class GString(BaseScrolledWindow):
	'''Panel to include String options over Base Panel - Text Control for entering strings and event handlers'''
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

	def OnTextEntered(self, event):
		'''If chosen value is not the default value, enable Reset button, else disable it'''
		obj = event.GetEventObject()
		if self.value == "set value":
			self.item4.Disable()
		elif obj.Value == self.value:
			self.item4.Disable()
		else:
			self.item4.Enable()

	def OnButtonClicked(self, event):
		'''change value chosen to default value on Reset Button Click'''
		self.textbox.SetValue(self.value)
		event.GetEventObject().Disable()

class GStringList(BaseScrolledWindow):
	def __init__(self, parent, name, desc, value):
		BaseScrolledWindow.__init__(self, parent, name, desc, value)

		if len(self.value) == 0:
			self.value.append("set value")
                self.smallPanel = wx.Panel(self)
                self.boxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
		self.dropdown=wx.ComboBox(self.smallPanel,id=wx.ID_ANY, choices = self.value, style = wx.CB_READONLY)
		self.dropdown.SetSelection(0)

                self.boxSizer2.Add(self.dropdown, 0.25, wx.EXPAND)
                self.smallPanel.SetSizer(self.boxSizer2)
                self.boxSizer.Add(self.smallPanel, 0.25, wx.EXPAND)
                self.SetSizer(self.boxSizer)
