import wx 
#from gui import Controller 
#from general import GBoolean 
from py.waf import defaults 
from py.config.tool import get_option_class, get_config_class 
from py.config import RTEMSConfig

class MyFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent)
		g = getOptions()
		option_class = g.run()
		c = createPanels(self, option_class)
		box = c.run()

		self.SetAutoLayout(True)
		self.SetSizer(box)
		self.Layout()
		self.Show(True)

class createPanels:
	def __init__(self, parent, option_class):
		self.parent = parent
		self.panels = []
		self.option_class = option_class
	def run(self):
		for opt in self.option_class:
			n = opt.__name__
			p = BasePanel(self.parent, n)
			self.panels.append(p)
		box = wx.BoxSizer(wx.VERTICAL)
		for p in self.panels:
		        box.Add(p)#, 2, wx.EXPAND)

	        #self.SetAutoLayout(True)
	        #self.SetSizer(box)
	        #self.Layout()
		
		return box

class BasePanel(wx.Panel):
	def __init__(self, parent, name):
		wx.Panel.__init__(self, parent=parent, id = wx.ID_ANY)
		wx.StaticText(self, -1, label = name)

class getOptions:
	def __init__(self):
		self.option_class = []
		#return self.run()
	def run(self):
		#self.frame = f
		'''get dictionary of options from py/waf/defaults/options.py'''
		option = get_option_class(defaults)
	
		'''get list of classes from each file in py/waf/defaults/bsp'''
		config = get_config_class(defaults.bsp)
		
		r = RTEMSConfig(option, config)
		tags = []
		#self.option_class = []
		#self.option_panel = []
		for opt in r.options_get():
			self.option_class.append(opt)
			'''
			self.option_class.append(opt)
			tag = opt.tag
			if tag not in tags:
				tags.append(tag)
			if opt.__base__.__name__ == "Boolean":
				n = opt.__name__
				d = opt.descr
				type = opt.__base__.__name__

				print n, d, type, tag
			'''
		#self.no_of_tabs = len(tags)
		return self.option_class


if __name__ == '__main__':
	app = wx.App(False)
	frame = MyFrame(None)#, wx.ID_ANY, "hello world")
	#frame.Show(True)
	app.MainLoop()
	#getOptions()
	'''
        controller = Controller(app, 5)
	p = controller.view.nb.innerNB.p[0]
        app.MainLoop()
	'''
