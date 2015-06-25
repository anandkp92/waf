#! /usr/bin/env python
# encoding: UTF-8

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
	def __init__(self, app):
		self.view = view.View(None, 'RTEMS Config')
		
		self.view.mb.Bind(wx.EVT_MENU, self.quit_event, self.view.mb.qmi)
		self.view.mb.Bind(wx.EVT_MENU, self.new_event, self.view.mb.new_cfg)
		self.view.mb.Bind(wx.EVT_MENU, self.open_event, self.view.mb.open_cfg)
		self.view.mb.Bind(wx.EVT_MENU, self.save_event, self.view.mb.save_cfg)
		self.view.Show(True)

	def quit_event(self, e):
		self.view.Close(True)

	def new_event(self, e):
		dlg = wx.MessageDialog(self.view, "Do you want to exit without Saving?", "Confirmation")
		dlg.ShowModal()
		dlg.Destroy()

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
	app = wx.App(False)
	controller = Controller(app)
	app.MainLoop()

