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
		self.base.SetScrollRate(5, 5)
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
			p = BaseScrolledWindow(self.base, n, d, v)
			self.scrolledwindows.append(p)
		sizer_box = wx.BoxSizer(wx.VERTICAL)
		for p in self.scrolledwindows:
		        sizer_box.Add(p, wx.EXPAND)

		sizer_box.Fit(self.base)
		self.base.SetSizer(sizer_box)
		return self.base

class BaseScrolledWindow(wx.ScrolledWindow):
	def __init__(self, parent, name, desc, value):

		wx.ScrolledWindow.__init__(self, parent=parent, id = wx.ID_ANY)
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

