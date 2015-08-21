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
import threading
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
		self.view.Bind(wx.EVT_MENU, self.stop_clean_event, self.view.stop_clean)
		self.view.Bind(wx.EVT_MENU, self.stop_custom_event, self.view.stop_custom)
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
		self.log = self.log+ "\n"

		returnCode = self.threadedPrinting(["waf","configure"])

		if returnCode == 0:
			op = "waf configure successful! Details, check console."
			title = "Success"
		else:
			op = "waf configure unsuccessful. Details, check console."
			title = "Error"
		
		dlg = wx.MessageDialog(self.view, op, title, wx.OK)
		self.view.stop_configure.Enable(False)
	        result = dlg.ShowModal()
		dlg.Destroy()

	def waf_build_event(self, e):
		self.view.stop_build.Enable(True)
		self.log = self.log+ "\n"
		
		returnCode = self.threadedPrinting(["waf","build"])

		if returnCode == 0:
                        op = "waf build successful! Details, check console."
                        title = "Success"
                else:
                        op = "waf build unsuccessful. Details, check console."
                        title = "Error"

                dlg = wx.MessageDialog(self.view, op, title, wx.OK)
                self.view.stop_build.Enable(False)
                result = dlg.ShowModal()
                dlg.Destroy()

	def waf_clean_event(self, e):
		self.view.stop_clean.Enable(True)
		self.log = self.log+ "\n"

		returnCode = self.threadedPrinting(["waf","clean"])

		if returnCode == 0:
                        op = "waf clean successful! Details, check console."
                        title = "Success"
                else:
                        op = "waf clean unsuccessful. Details, check console."
                        title = "Error"

                dlg = wx.MessageDialog(self.view, op, title, wx.OK)
                self.view.stop_clean.Enable(False)
                result = dlg.ShowModal()
                dlg.Destroy()
		
	def waf_custom_event(self, e):
		dlg = wx.TextEntryDialog(self.view, "Enter waf target", "Custom Build")
		dlg.ShowModal()
		self.custom_target = dlg.GetValue()
		dlg.Destroy()
		
		self.view.stop_custom.Enable(True)
		self.log = self.log+ "\n"
		returnCode = self.threadedPrinting(["waf",self.custom_target])

		if returnCode == 0:
                        op = "waf "+self.custom_target+" successful! Details, check console."
                        title = "Success"
                else:
                        op = "waf "+self.custom_target+" unsuccessful. Details, check console."
                        title = "Error"

                dlg = wx.MessageDialog(self.view, op, title, wx.OK)
                self.view.stop_custom.Enable(False)
                result = dlg.ShowModal()
                dlg.Destroy()

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
		
	def stop_clean_event(self, e):
		try:
			import signal
			os.kill(self.waf_clean_pid, signal.SIGKILL)
			msg = "Killed the process"
		except OSError, err:
			msg = "Error. Details:\n"+str(err)
		dlg = wx.MessageDialog(self.view, msg,"Kill waf clean", wx.OK)
	        result = dlg.ShowModal()
        	dlg.Destroy()
		self.view.stop_clean.Enable(False)		

	def stop_custom_event(self, e):
		try:
			import signal
			os.kill(self.waf_custom_pid, signal.SIGKILL)
			msg = "Killed the process"
		except OSError, err:
			msg = "Error. Details:\n"+str(err)
		dlg = wx.MessageDialog(self.view, msg,"Kill waf "+self.custom_target, wx.OK)
	        result = dlg.ShowModal()
        	dlg.Destroy()
		self.view.stop_clean.Enable(False)

	def threadedPrinting(self, cmd):
		waf_dir = os.path.dirname(cwd)

	        process = Popen(cmd, stdout = PIPE, stderr = PIPE, cwd=waf_dir)

	        stdout_reader = AsynchronousFileReader(process.stdout, "stdout", self.console_textbox)
	        stdout_reader.start()
	        stderr_reader = AsynchronousFileReader(process.stderr, "stderr", self.console_textbox)
	        stderr_reader.start()

		ppid = process.pid
		
		if cmd[1] == "configure":
			self.waf_configure_pid = ppid
		elif cmd[1] == "build":
			self.waf_build_pid = ppid
		elif cmd[1] == "clean":
			self.waf_build_pid = ppid
		else:
			self.waf_custom_pid = ppid
		
	        stdout_reader.join()
	        stderr_reader.join()

		self.log = self.console_textbox.GetValue()
		process.wait()

		returncode = process.returncode
		#print returncode
	
	        process.stdout.close()
        	process.stderr.close()

		return returncode


class NewWindow(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, None, id, 'Console', size = (600,400))
		self.Show(False)

class AsynchronousFileReader(threading.Thread):
        def __init__(self, fd, name, txtbox):
                threading.Thread.__init__(self)
                self._fd = fd
                self._name = name
                self.output = ''
		self.txtbox = txtbox

        def run(self):
                for line in iter(self._fd.readline, ''):
                        op = self._name + " : "+line
			self.txtbox.SetValue(self.txtbox.GetValue() +op)
                        self.output = self.output + op

if __name__ == '__main__':
	app = wx.App(False)
	controller = Controller(app)
	app.MainLoop()

