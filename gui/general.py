import wx

class MyPanel(wx.Panel):
	def __init__(self, parent, name, value, desc):
		wx.Panel.__init__(self, parent)
		value = value
		desc = desc
		
		#self.pos = (0,0)
		wx.StaticText(self, id=wx.ID_ANY, label = name, pos = (0,0))
		wx.StaticText(self, id=wx.ID_ANY, label = "Default Value:", pos = (0,30))
		wx.StaticText(self, id=wx.ID_ANY, label = str(value), pos = (100, 30))
		wx.StaticText(self, id=wx.ID_ANY, label = desc, pos = (0,60))
		self.pos = (0,60)
		#wx.StaticText(self, id=wx.ID_ANY, label = "value", pos = (0,90))

class GBoolean(MyPanel):
	def __init__(self, parent, name, value, desc, type):
		MyPanel.__init__(self, parent, name, value, desc)
		if type != "Boolean":
			'''error handling'''
		else:
			###change this
			wx.RadioButton(self, id=wx.ID_ANY, label = "1", pos = (0,90), style=wx.RB_GROUP)
			wx.RadioButton(self, id=wx.ID_ANY, label = "2", pos = (100,90), style=wx.RB_GROUP)
		

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "hello world")
p = GBoolean(frame, "base", True, "Boolean", "Boolean")
frame.Show(True)
app.MainLoop()
	
