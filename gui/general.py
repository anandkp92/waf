import wx 
class BasePanel(wx.Panel):
	def __init__(self, parent, name, value, desc, p):
		wx.Panel.__init__(self, parent, wx.NewId())
		value = value
		desc = desc
		
		#self.pos = (0,0)
		l1 = wx.StaticText(self, id=wx.ID_ANY, label = name, pos = (p[0]+0,p[1]+0))
		l2 = wx.StaticText(self, id=wx.ID_ANY, label = "Default Value:", pos = (p[0]+0,p[1]+30))
		l3 = wx.StaticText(self, id=wx.ID_ANY, label = str(value), pos = (p[0]+100,p[1]+30))
		b1 = wx.Button(self, id=wx.ID_ANY, label = "RESET", pos = (p[0]+300,p[1]+30))
		l4 = wx.StaticText(self, id=wx.ID_ANY, label = desc, pos = (p[0]+0,p[1]+60))
		#wx.StaticText(self, id=wx.ID_ANY, label = "value", pos = (0,90))
		
		box = wx.BoxSizer(wx.VERTICAL)
		box.Add(l1)
		box.Add(l2)
		box.Add(l3)
		box.Add(b1)
		box.Add(l4)
		
		self.SetAutoLayout(True)
		self.SetSizer(box)
		self.Layout()

class GBoolean(BasePanel):
	def __init__(self, parent, name, value, desc, type, p):
		BasePanel.__init__(self, parent, name, value, desc, p)
		if type != "Boolean":
			'''error handling'''
		else:
			self.rbTrue = wx.RadioButton(self, id=wx.ID_ANY, label = "True", pos = (p[0]+0,p[1]+90), style=wx.RB_GROUP)
			self.rbFalse = wx.RadioButton(self, id=wx.ID_ANY, label = "False", pos = (p[0]+100,p[1]+90))
			box = wx.BoxSizer(wx.HORIZONTAL)
			box.Add(self.rbTrue)
			box.Add(self.rbFalse)
			self.SetAutoLayout(True)
			self.SetSizer(box)
			self.Layout()


app = wx.App(False)
frame = wx.Frame(None, -1 ,"options")

g1 = GBoolean(frame, 'options', 'True', 't/f', 'Boolean', p = (0,0))
g2 = GBoolean(frame, 'options2', 'True', 't/f', 'Boolean', p = (100,100))

box = wx.BoxSizer(wx.VERTICAL)
box.Add(g1, wx.EXPAND)
box.Add(g2, wx.EXPAND)

frame.SetAutoLayout(True)
frame.SetSizer(box)
frame.Layout()

frame.Show(True)
app.MainLoop()

