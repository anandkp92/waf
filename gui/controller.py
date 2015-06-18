import wx
import os
import view

class Controller:
	def __init__(self, app, no_of_tabs):
		##== create an object of the View module ==##
		self.view = view.View(None, 'RTEMS Config', no_of_tabs)
		
		##== set up event handlers for the menu items ==##
		self.view.mb.Bind(wx.EVT_MENU, self.quit_event, self.view.mb.qmi)
		self.view.mb.Bind(wx.EVT_MENU, self.new_event, self.view.mb.new_cfg)
		self.view.mb.Bind(wx.EVT_MENU, self.open_event, self.view.mb.open_cfg)
		self.view.mb.Bind(wx.EVT_MENU, self.save_event, self.view.mb.save_cfg)
		self.view.Show(True)

	##== event handler when the user chooses Quit menu item ==##
	def quit_event(self, e):
		self.view.Close(True)

	##== event handler when the user chooses New menu item ==##	
	def new_event(self, e):
		dlg = wx.MessageDialog(self.view, "Do you want to exit without Saving?", "Confirmation")
		dlg.ShowModal()
		dlg.Destroy()

	##== event handler when the user chooses Open menu item ==##
	def open_event(self,e):
        	self.dirname = ''
		dlg = wx.FileDialog(self.view, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			f.close()
			dlg.Destroy()

	##== event handler when the user chooses Save menu item ==##
        def save_event(self,e):
                self.dirname = ''
                dlg = wx.FileDialog(self.view, "Choose a file", self.dirname, "", "*.*", wx.SAVE)
                if dlg.ShowModal() == wx.ID_OK:
                        self.filename = dlg.GetFilename()
                        self.dirname = dlg.GetDirectory()
                        f = open(os.path.join(self.dirname, self.filename), 'w')
                        self.control.SetValue(f.read())
                        f.close()
                        dlg.Destroy()
	
if __name__ == '__main__':
	no_of_tabs = 3
	app = wx.App(False)
	controller = Controller(app, no_of_tabs)
	app.MainLoop()
