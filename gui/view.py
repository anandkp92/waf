import wx
class View(wx.Frame):
	def __init__(self, parent, title, no_of_tabs):
                wx.Frame.__init__(self, parent, title = title)
		##== tab layout ==##
		self.nb = tabSet(self, no_of_tabs)
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

class tabSet(wx.Notebook):
	##== set up a list of tabs/panes ==##
	def __init__(self, parent, no_of_tabs):
                nb = wx.Notebook(parent)
                self.tabs = []
                for i in range(0,no_of_tabs):
                        name = "Tab "+str(i+1)
                        self.tabs.append(tabPanel(nb, name))
                        nb.AddPage(self.tabs[i], name)
                self.tabs[0].SetFocus()	

class tabPanel(wx.Panel):
	##== each tab is a separate Panel ==##
        def __init__(self, parent, name):
                wx.Panel.__init__(self, parent, name = name)
