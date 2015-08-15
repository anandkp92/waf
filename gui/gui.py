#! /usr/bin/env python
# encoding: UTF-8

'''This is the starting file. Run this to execute the gui.'''

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
import GBsp
import noteSet
from subprocess import Popen, PIPE

class Controller:
	'''instantiates the View class, GBsp class and configures the necessary event handlers'''
	def __init__(self, app):
		self.view = view.View(None, 'RTEMS Config')
		self.gbsp = GBsp.GBsp(self.view, self.view.size)
		
		self.view.Bind(wx.EVT_MENU, self.quit_event, self.view.qmi)
		self.view.Bind(wx.EVT_MENU, self.new_event, self.view.new_cfg)
		self.view.Bind(wx.EVT_MENU, self.open_event, self.view.open_cfg)
		self.view.Bind(wx.EVT_MENU, self.save_event, self.view.save_cfg)
		self.view.Bind(wx.EVT_MENU, self.view_bsp_event, self.view.view_bsp_list)
		
		self.view.Bind(wx.EVT_MENU, self.waf_configure_event, self.view.waf_configure)
		self.view.Bind(wx.EVT_MENU, self.waf_build_event, self.view.waf_build)
		self.view.Show(True)

	def quit_event(self, e):
		'''event handler upon clicking Quit'''
		self.view.Close(True)

	def new_event(self, e):
		'''event handler upon clicking New'''
		dlg = wx.MessageDialog(self.view, "Do you want to exit without Saving?", "Confirmation")
		dlg.ShowModal()
		dlg.Destroy()

	def open_event(self,e):
		'''event handler upon clicking Open'''
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

        def save_event(self,e):
		'''event handler upon clicking Save'''
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

	def view_bsp_event(self, e):
		s = ""
		for bsp, bsp_class in self.gbsp.chosen_bsp:
                        s=s+bsp+"\n"
		dlg = wx.MessageDialog(self.view, "Chosen BSPs:\n"+s,"BSPS", wx.OK)
                result = dlg.ShowModal()
		dlg.Destroy()

	def waf_configure_event(self, e):
		process = Popen(["waf","configure"], stdout = PIPE, stderr = PIPE, cwd="../")
		op, err = process.communicate()
		if err == '':
	   		dlg = wx.MessageDialog(self.view, op ,"Success!", wx.OK)
		else:
			dlg = wx.MessageDialog(self.view, err, "Error", wx.OK)
                result = dlg.ShowModal()
		dlg.Destroy()

	def waf_build_event(self, e):
		process = Popen(["waf","build"], stdout = PIPE, stderr = PIPE, cwd="../")
                op, err = process.communicate()
		if err == '':
                        dlg = wx.MessageDialog(self.view, op ,"Success!", wx.OK)
                else:
                        dlg = wx.MessageDialog(self.view, err, "Error", wx.OK)
                result = dlg.ShowModal()
                dlg.Destroy()

if __name__ == '__main__':
	app = wx.App(False)
	controller = Controller(app)
	app.MainLoop()

