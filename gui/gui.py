#! /usr/bin/env python
# encoding: UTF-8

'''This is the starting file. Run this to execute the gui.'''

import os
from sys import path
cwd = os.getcwd()

from os.path import exists
if not exists("py"):
	path.insert(0, cwd[0:cwd.rfind('/')])
else:
	path.insert(0, cwd)

import wx
import sys
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
		self.view.Bind(wx.EVT_MENU, self.view_console_event, self.view.view_console)

		self.view.Bind(wx.EVT_MENU, self.waf_configure_event, self.view.waf_configure)
		self.view.Bind(wx.EVT_MENU, self.waf_build_event, self.view.waf_build)
		self.view.Bind(wx.EVT_MENU, self.waf_clean_event, self.view.waf_clean)
		self.view.Bind(wx.EVT_MENU, self.waf_custom_event, self.view.waf_custom)

		self.view.Bind(wx.EVT_MENU, self.stop_configure_event, self.view.stop_configure)
		self.view.Bind(wx.EVT_MENU, self.stop_build_event, self.view.stop_build)
		self.view.Bind(wx.EVT_CLOSE, self.onViewCloseWindow)

		self.console = NewWindow(None, -1)
		consoleSizer = wx.BoxSizer(wx.VERTICAL)
		
		self.log = ''
		self.console_clear_button = wx.Button(parent = self.console, label = "Clear")
		self.console.Bind(wx.EVT_BUTTON, self.onClearButton, self.console_clear_button)
		consoleSizer.Add(self.console_clear_button)

		self.console_textbox = wx.TextCtrl(parent = self.console, value = self.log, style = wx.TE_READONLY | wx.TE_MULTILINE, size = (600,400))
		consoleSizer.Add(self.console_textbox)

		self.console.Bind(wx.EVT_CLOSE, self.onConsoleCloseWindow)
		self.console.SetSizer(consoleSizer)
		self.console.Show(False)

		self.view.Show(True)

	def onViewCloseWindow(self, e):
		dlg = wx.MessageDialog(self.view, "Are you sure you want to exit?","Confirmation", wx.OK | wx.CANCEL)
		if dlg.ShowModal() == wx.ID_OK:	
			self.view.Destroy()
			self.console.Destroy()
			sys.exit(0)

	def onConsoleCloseWindow(self, e):
		self.console.Show(False)
	
	def onClearButton(self, e):
		self.log = ''
		self.console_textbox.Clear()

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

	def view_console_event(self, e):
		self.console.Show(True)

	def waf_configure_event(self, e):
		self.view.stop_configure.Enable(True)
		waf_dir = os.path.dirname(cwd)
		self.log = self.log+ "\n"
		process = Popen(["waf","configure"], stdout = PIPE, stderr = PIPE, cwd=waf_dir, bufsize=1)

		out_log = "\nwaf configure Output Stream:\n"
		err_log = "\nwaf configure Error Stream:\n"
		for line in iter(process.stdout.readline, b''):
			out_log = out_log + line
			for err in iter(process.stderr.readline, b''):
				err_log = err_log + err
				break

			self.console_textbox.Refresh()
			self.console_textbox.SetValue(self.log + out_log + err_log)
		self.log = self.log + out_log + err_log
		process.wait()
		
		if process.returncode == 0:
			op = "waf configure successful! Details, check console."
			title = "Success"
		else:
			op = "waf configure unsuccessful. Details, check console."
			title = "Error"
		
		dlg = wx.MessageDialog(self.view, op, title, wx.OK)
		self.waf_configure_pid = process.pid
		self.view.stop_configure.Enable(False)
	        result = dlg.ShowModal()
		dlg.Destroy()
		process.stdout.close()
		process.stderr.close()

	def waf_build_event(self, e):
		self.view.stop_build.Enable(True)
		
		waf_dir = os.path.dirname(cwd)
		self.log = self.log+ "\n"
		process = Popen(["waf","build"], stdout = PIPE, stderr = PIPE, cwd=waf_dir, bufsize=1)

		out_log = "\nwaf build Output Stream:\n"
		err_log = "\nwaf build Error Stream:\n"
		for line in iter(process.stdout.readline, b''):
			out_log = out_log + line
			for err in iter(process.stderr.readline, b''):
				err_log = err_log + err
				break

			self.console_textbox.Refresh()
			self.console_textbox.SetValue(self.log + out_log + err_log)
		self.log = self.log + out_log + err_log
		process.wait()

		if process.returncode == 0:
                        op = "waf build successful! Details, check console."
                        title = "Success"
                else:
                        op = "waf build unsuccessful. Details, check console."
                        title = "Error"

                dlg = wx.MessageDialog(self.view, op, title, wx.OK)
                self.waf_build_pid = process.pid
                self.view.stop_build.Enable(False)
                result = dlg.ShowModal()
                dlg.Destroy()
                process.stdout.close()
                process.stderr.close()

	def waf_clean_event(self, e):
		waf_dir = os.path.dirname(cwd)
		self.log = self.log+ "\n"
		process = Popen(["waf","clean"], stdout = PIPE, stderr = PIPE, cwd=waf_dir, bufsize=1)

		out_log = "\nwaf clean Output Stream:\n"
		err_log = "\nwaf clean Error Stream:\n"
		for line in iter(process.stdout.readline, b''):
			out_log = out_log + line
			for err in iter(process.stderr.readline, b''):
				err_log = err_log + err
				break

			self.console_textbox.Refresh()
			self.console_textbox.SetValue(self.log + out_log + err_log)
		self.log = self.log + out_log + err_log
		process.wait()

		if process.returncode == 0:
                        op = "waf clean successful! Details, check console."
                        title = "Success"
                else:
                        op = "waf clean unsuccessful. Details, check console."
                        title = "Error"

                dlg = wx.MessageDialog(self.view, op, title, wx.OK)
                #self.waf_build_pid = process.pid
                #self.view.stop_build.Enable(False)
                result = dlg.ShowModal()
                dlg.Destroy()
                process.stdout.close()
                process.stderr.close()
		
	def waf_custom_event(self, e):
		dlg = wx.TextEntryDialog(self.view, "Enter waf target", "Custom Build")
		dlg.ShowModal()
		target = dlg.GetValue()
		dlg.Destroy()

		waf_dir = os.path.dirname(cwd)
		self.log = self.log+ "\n"
		process = Popen(["waf",target], stdout = PIPE, stderr = PIPE, cwd=waf_dir, bufsize=1)

		out_log = "\nwaf "+target+" Output Stream:\n"
		err_log = "\nwaf "+target+" Error Stream:\n"
		for line in iter(process.stdout.readline, b''):
			out_log = out_log + line
			for err in iter(process.stderr.readline, b''):
				err_log = err_log + err
				break

			self.console_textbox.Refresh()
			self.console_textbox.SetValue(self.log + out_log + err_log)
		self.log = self.log + out_log + err_log
		process.wait()

		if process.returncode == 0:
                        op = "waf "+target+" successful! Details, check console."
                        title = "Success"
                else:
                        op = "waf "+target+" unsuccessful. Details, check console."
                        title = "Error"

                dlg = wx.MessageDialog(self.view, op, title, wx.OK)
                #self.waf_build_pid = process.pid
                #self.view.stop_build.Enable(False)
                result = dlg.ShowModal()
                dlg.Destroy()
                process.stdout.close()
                process.stderr.close()		

	def stop_configure_event(self, e):
		try:
			import signal
			os.kill(self.waf_configure_pid, signal.SIGKILL)
			msg = "Killed the Process"
		except OSError, err:
			msg = "Error. Details: "+str(err)
		dlg = wx.MessageDialog(self.view, msg,"Kill waf configure", wx.OK)
	        result = dlg.ShowModal()
        	dlg.Destroy()
		self.view.stop_configure.Enable(False)
		

	def stop_build_event(self, e):
		try:
			import signal
			os.kill(self.waf_build_pid, signal.SIGKILL)
			msg = "Killed the process"
		except OSError, err:
			msg = "Error. Details:\n"+str(err)
		dlg = wx.MessageDialog(self.view, msg,"Kill waf build", wx.OK)
	        result = dlg.ShowModal()
        	dlg.Destroy()
		self.view.stop_build.Enable(False)

class NewWindow(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, None, id, 'Console', size = (600,400))
		self.Show(False)

if __name__ == '__main__':
	app = wx.App(False)
	controller = Controller(app)
	app.MainLoop()

