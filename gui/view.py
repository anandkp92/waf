import wx
import tabSet as ts
class View(wx.Frame):
	def __init__(self, parent, title, no_of_tabs):
                wx.Frame.__init__(self, parent, title = title, size = (512, 512))
		##== tab layout ==##
		self.nb = ts.tabSet(self, no_of_tabs)
		##== setting up menus ==##
		self.mb  = menubar()
		self.SetMenuBar(self.mb)

class menubar(wx.MenuBar):
	def __init__(self):
		wx.MenuBar.__init__(self)

		##== set up File, View and Tools menu  ==##
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
