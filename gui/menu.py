import wx
class topMenu(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(topMenu, self).__init__(*args, **kwargs)
		self.displayUI()

	def displayUI(self):
		menubar = wx.MenuBar()
		
		fileMenu = wx.Menu()
		fileMenu.Append(wx.ID_NEW, '&New')
		fileMenu.Append(wx.ID_OPEN, '&Open')
		fileMenu.Append(wx.ID_SAVE, '&Save')
		fileMenu.AppendSeparator()

		viewMenu = wx.Menu()
		viewMenu.Append(wx.ID_VIEW_DETAILS, 'Config')
		viewMenu.Append(wx.ID_VIEW_LIST, 'BSP_List')
		viewMenu.AppendSeparator()
	
		toolsMenu = wx.Menu()
		toolsMenu.Append(-1, '&Configure')
		toolsMenu.Append(-1, '&Build')
		toolsMenu.AppendSeparator()

		qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
		fileMenu.AppendItem(qmi)

		self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
		
		menubar.Append(fileMenu, '&File')
		menubar.Append(viewMenu, '&View')
		menubar.Append(toolsMenu, '&Tools')
		self.SetMenuBar(menubar)
		
		self.SetSize((600,600))
		self.SetTitle('RTEMS Config')
		self.Centre()
		self.Show(True)

	def OnQuit(self, e):
		self.Close()

def main():
	ex = wx.App()
	topMenu(None)
	ex.MainLoop()

if __name__ == '__main__':
	main()

