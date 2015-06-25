import wx
import noteSet
class View(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER, size = (1024,1024))
		s1 = (1000,1000)
		n1 = "outer"
		self.outerNB = noteSet.noteSet(self, name=n1, style=wx.NB_TOP, size=s1)
		self.mb  = menubar()
		self.SetMenuBar(self.mb)

class menubar(wx.MenuBar):
	def __init__(self):
		wx.MenuBar.__init__(self)

		fileMenu = wx.Menu()
		self.new_cfg = fileMenu.Append(wx.ID_NEW, '&New')
		self.open_cfg = fileMenu.Append(wx.ID_OPEN, '&Open')
		self.save_cfg = fileMenu.Append(wx.ID_SAVE, '&Save')
		fileMenu.AppendSeparator()
		self.qmi = fileMenu.Append(wx.ID_EXIT, '&Quit')

		viewMenu = wx.Menu()
		viewMenu.Append(wx.ID_VIEW_DETAILS, 'Config')
		viewMenu.Append(wx.ID_VIEW_LIST, 'BSP_List')
		viewMenu.AppendSeparator()

		toolsMenu = wx.Menu()
		toolsMenu.Append(wx.ID_ANY, '&Configure')
		toolsMenu.Append(wx.ID_ANY, '&Build')
		toolsMenu.AppendSeparator()

		self.Append(fileMenu, '&File')
		self.Append(viewMenu, '&View')
		self.Append(toolsMenu, '&Tools')

