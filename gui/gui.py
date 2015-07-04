#! /usr/bin/env python
# encoding: UTF-8
'''This is the starting file. Run this to execute the gui'''

from os import getcwd
from sys import path
cwd = getcwd()

from os.path import exists
if not exists("py"):
	path.insert(0, cwd[0:cwd.rfind('/')])
else:
	path.insert(0, cwd)

import wx
import os
import view

class Controller:
	'''instantiates the View class and configures the necessary event handlers'''
	def __init__(self, app):
		self.view = view.View(None, 'RTEMS Config')
		
		self.view.mb.Bind(wx.EVT_MENU, self.quit_event, self.view.mb.qmi)
		self.view.mb.Bind(wx.EVT_MENU, self.new_event, self.view.mb.new_cfg)
		self.view.mb.Bind(wx.EVT_MENU, self.open_event, self.view.mb.open_cfg)
		self.view.mb.Bind(wx.EVT_MENU, self.save_event, self.view.mb.save_cfg)
		self.view.Show(True)

	'''event handler upon clicking Quit'''
	def quit_event(self, e):
		self.view.Close(True)

	'''event handler upon clicking New'''
	def new_event(self, e):
		dlg = wx.MessageDialog(self.view, "Do you want to exit without Saving?", "Confirmation")
		dlg.ShowModal()
		dlg.Destroy()

	'''event handler upon clicking Open'''
	def open_event(self,e):
        	self.dirname = ''
		dlg = wx.FileDialog(self.view, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			try:
				f = open(os.path.join(self.dirname, self.filename), 'r')
				self.control.SetValue(f.read())
				dlg.Destroy()
			except IOError as err:
				errorDlg = wx.MessageDialog(self.view, "Read Error: File cannot be opened/read from.\n%s"%err, "Error")
				errorDlg.ShowModal()
				errorDlg.Destroy()
			else:				
				f.close()

	'''event handler upon clicking Save'''
        def save_event(self,e):
                self.dirname = ''
                dlg = wx.FileDialog(self.view, "Choose a file", self.dirname, "", "*.*", wx.SAVE)
                if dlg.ShowModal() == wx.ID_OK:
                        self.filename = dlg.GetFilename()
                        self.dirname = dlg.GetDirectory()
			try:
	                        f = open(os.path.join(self.dirname, self.filename), 'w')
	                        self.control.SetValue(f.read())
	                        dlg.Destroy()
			except IOError as err:
				errorDlg = wx.MessageDialog(self.view, "Write Error: File cannot be opened/written to.\n%s"%err, "Error")
				errorDlg.ShowModal()
				errorDlg.Destroy()
			else:
				f.close()
	
if __name__ == '__main__':
	app = wx.App(False)
	controller = Controller(app)
	app.MainLoop()

