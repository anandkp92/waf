import wx
class View(wx.Frame):
        def __init__(self, parent, title):
                wx.Frame.__init__(self, parent, title = title)

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

                menubar = wx.MenuBar()
                menubar.Append(fileMenu, '&File')
                menubar.Append(viewMenu, '&View')
                menubar.Append(toolsMenu, '&Tools')
                self.SetMenuBar(menubar)
                #self.Show(True)

