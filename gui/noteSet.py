import wx
import getOptions

class noteSet:
        def __init__(self, parent, name, style, size):
                nb = wx.Notebook(parent = parent, style = style, size = size)
                self.tabs = []
                self.names = []
                self.p = []

		g = getOptions.getOptions()
		option_class = g.run()
		types = g.getTypes(option_class)
		types = g.getTypes(option_class)
		
		for t in types:
			options = g.getTypeOptions(option_class, t)
			opt = createScrolledWindows(nb, options)
			option_scrolledwindow = opt.getScrolledWindow()
			nb.AddPage(option_scrolledwindow, t)

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

class BaseScrolledWindow(wx.ScrolledWindow):
	def __init__(self, parent, name, desc, value):

		wx.ScrolledWindow.__init__(self, parent=parent, id = wx.ID_ANY, style=wx.SUNKEN_BORDER)

		self.value = value
 		self.item1 = wx.StaticText(self, -1, label = name)
		self.item1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
                self.item2 = wx.StaticText(self, -1, label = "About : %s"%desc)
                self.item3 = wx.StaticText(self, -1, label = "Default Value : %s"%self.value)
                self.item4 = wx.Button(self, -1, "Reset")

                self.item4.Disable()
  		#self.grid = wx.GridSizer(5, 1)
		self.boxSizer = wx.BoxSizer(wx.VERTICAL)

                self.boxSizer.Add(self.item1, 0.5, wx.EXPAND)
                self.boxSizer.Add(self.item2, 0.5, wx.EXPAND)
                self.boxSizer.Add(self.item3, 0.5, wx.EXPAND)
                self.boxSizer.Add(self.item4)#, wx.EXPAND)
                self.SetSizer(self.boxSizer)

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

                if self.value == True:
                        self.rbTrue.SetValue(True)
                else:
                        self.rbFalse.SetValue(True)
                
                self.boxSizer2.Add(self.rbTrue, 0.25)#, wx.EXPAND)
                self.boxSizer2.Add(self.rbFalse, 0.25)#, wx.EXPAND)
                self.smallPanel.SetSizer(self.boxSizer2)

                self.boxSizer.Add(self.smallPanel, 0.25)#, wx.EXPAND)
                self.SetSizer(self.boxSizer)
        
        def radio_event(self, event):
		radioSelected = event.GetEventObject()
		if self.value != True and self.value != False:
			self.item4.Disable()
		elif radioSelected.GetLabel() != str(self.value):
			self.item4.Enable()
		elif radioSelected.GetLabel() == str(self.value):
			self.item4.Disable()

	def OnButtonClicked(self, event):
		if self.value == True:
			self.rbTrue.SetValue(True)
			self.rbFalse.SetValue(False)
		elif self.value == False:
			self.rbFalse.SetValue(True)
			self.rbTrue.SetValue(False)
		event.GetEventObject().Disable()

