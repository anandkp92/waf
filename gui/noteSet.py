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
		self.base = wx.Panel(self.parent, size = (1000,1000), name = "Config")
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
			p = BasePanel(self.base, n, d, v)
			self.panels.append(p)
		box = wx.BoxSizer(wx.VERTICAL)
		for p in self.panels:
		        box.Add(p, wx.EXPAND)

		self.base.SetSizer(box)
		return self.base

class BasePanel(wx.Panel):
	def __init__(self, parent, name, desc, value):
		wx.Panel.__init__(self, parent=parent, id = wx.ID_ANY)
		item1 = wx.StaticText(self, -1, label = name)
		item2 = wx.StaticText(self, -1, label = "Default : %s"%(str('True')))
		item3 = wx.StaticText(self, -1, label = "Desc : %s"%desc)
		item4 = wx.StaticText(self, -1, label = "Value : %s"%value)
		grid = wx.GridSizer(5, 1)
		grid.Add(item1, wx.EXPAND)
		grid.Add(item2, wx.EXPAND)
		grid.Add(item3, wx.EXPAND)
		grid.Add(item4, wx.EXPAND)
		self.SetSizer(grid)

