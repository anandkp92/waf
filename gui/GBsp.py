#! /usr/bin/env python
# encoding: UTF-8

'''creates a new frame and displays all bsps as checkboxes'''

import wx
import getBSP
import py.waf.defaults.bsp as bsp
import noteSet

class GBsp():
	def __init__(self, parent, size):
		self.parent = parent
		self.size = size
		self.dialog_result = 'False'
		self.bsp_list = getBSP.get_bsp_classes(bsp)
		self.createBspPanel()

	def createBspPanel(self):
		'''populate the frame with bsps (as checkboxes)'''
                self.base = wx.ScrolledWindow(self.parent, wx.ID_ANY, wx.DefaultPosition, self.size,wx.HSCROLL|wx.VSCROLL)
                self.base.SetScrollRate(1, 1)
		self.checkboxlist = []
		self.bsp_count = 0
		self.chosen_bsp = []

		for bsp in self.bsp_list:
			mod = bsp.__module__.split(".")[-1]
			c = wx.CheckBox(parent = self.base, name = mod+"/"+bsp.__name__, label = mod+"/"+bsp.__name__)
			self.parent.Bind(wx.EVT_CHECKBOX, self.checkboxevent, c)
			self.checkboxlist.append(c)

		sizer_box = wx.BoxSizer(wx.VERTICAL)
		for c in self.checkboxlist:
			sizer_box.Add(c, 0.25, wx.EXPAND)
	
		self.submit = wx.Button(self.base, -1, "Submit")
		self.parent.Bind(wx.EVT_BUTTON, self.submitOnClicked, self.submit)
		self.submit.Disable()
		sizer_box.Add(self.submit, 0.5)

		sizer_box.Fit(self.base)
                self.base.SetSizer(sizer_box)
	
	def checkboxevent(self, event):
		'''checkbox event handler'''
		checkbox = event.GetEventObject()
		if checkbox.IsChecked():
			self.bsp_count+=1
			self.chosen_bsp.append(checkbox.GetLabel())
			self.submit.Enable()
		else:
			self.bsp_count-=1
			self.chosen_bsp.remove(checkbox.GetLabel())
			if self.bsp_count == 0:	
				self.submit.Disable()	

	def submitOnClicked(self, event):
		'''submit button event handler - displays chosen bsps for now'''
		s = ""
		for bsp in self.chosen_bsp:
			s=s+bsp+"\n"
		dlg = wx.MessageDialog(self.parent, "Chosen BSPs:\n"+s+"Confirm?", "Confirmation")
                result = dlg.ShowModal()
		if result == wx.ID_OK:
			'''hide the bsp window and display the options window'''
			#print "Pressed ok"
			self.base.Show(False)
			self.parent.outerNB = noteSet.noteSet(self.parent, name="outer", style=wx.NB_TOP, size = self.size)
		dlg.Destroy()

