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
			opt = createPanels(nb, options)
			option_panel = opt.getPanel()
			nb.AddPage(option_panel, t)

class createPanels:
	def __init__(self, parent, option_class):
		self.parent = parent
		self.base = wx.ScrolledWindow(self.parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
		self.base.SetScrollRate(5, 5)
		self.panels = []
		self.option_class = option_class

	def getPanel(self):
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
				p = BasePanel(self.base, n, d, v)
			self.panels.append(p)
		sizer_box = wx.BoxSizer(wx.VERTICAL)
		for p in self.panels:
		        sizer_box.Add(p, wx.EXPAND)

		sizer_box.Fit(self.base)
		self.base.SetSizer(sizer_box)
		return self.base

class BasePanel(wx.Panel):
	def __init__(self, parent, name, desc, value):
		wx.Panel.__init__(self, parent=parent, id = wx.ID_ANY)
		self.value = value
		self.item1 = wx.StaticText(self, -1, label = name)
		self.item2 = wx.StaticText(self, -1, label = "About : %s"%desc)
		self.item3 = wx.StaticText(self, -1, label = "Default Value : %s"%self.value)
		self.item4 = wx.Button(self, -1, "Reset")

		#self.item4.Disable()
		self.grid = wx.GridSizer(5, 1)

		self.grid.Add(self.item1, 1, wx.EXPAND)
		self.grid.Add(self.item2, 1, wx.EXPAND)
		self.grid.Add(self.item3, 1,wx.EXPAND)
		self.grid.Add(self.item4, wx.EXPAND)
		self.SetSizer(self.grid)

class GBoolean(BasePanel):
	def __init__(self, parent, name, desc, value):
		BasePanel.__init__(self, parent, name, desc, value)
		#self.value = value
		self.smallPanel = wx.Panel(self)
		self.grid2 = wx.GridSizer(1,2)
		self.rbTrue = wx.RadioButton(self.smallPanel, id=wx.ID_ANY, label = "True", style=wx.RB_GROUP)
		self.rbFalse = wx.RadioButton(self.smallPanel, id=wx.ID_ANY, label = "False")

		#TODO: put in controller class
		'''
		self.rbTrue.Bind(wx.EVT_RADIOBUTTON, self.radio_event, self.rbTrue)
		self.rbFalse.Bind(wx.EVT_RADIOBUTTON, self.radio_event, self.rbFalse)
		
		if self.value == 'True':
			self.rbTrue.SetValue(True)
		else:
			self.rbFalse.SetValue(True)
		'''
		self.grid2.Add(self.rbTrue, wx.EXPAND)
		self.grid2.Add(self.rbFalse, wx.EXPAND)
		self.smallPanel.SetSizer(self.grid2)
		
		self.grid.Add(self.smallPanel, wx.EXPAND)
		self.SetSizer(self.grid)
	'''
	def radio_event(self, event):
		if self.rbTrue == 'True' and self.value != 'True':
			self.item4.Enable()
		elif self.rbFalse == 'True' and self.value != 'False':
			self.item4.Enable()
	'''
