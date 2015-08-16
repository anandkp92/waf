#! /usr/bin/env python
# encoding: UTF-8

'''This file creates the looks of the gui - the menu, tab set'''

import wx
import noteSet

class View(wx.Frame):
	'''GUI view - with menu bar and tabs'''
	def __init__(self, parent, title):
		self.size = wx.Size(600,400)
		wx.Frame.__init__(self, parent, title="RTEMS Config", pos = wx.DefaultPosition, size = self.size, style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		#self.outerNB = noteSet.noteSet(self, name="outer", style=wx.NB_TOP, size=wx.DefaultSize)
		self.mb  = self.menubar()
		self.SetMenuBar(self.mb)

	def menubar(self):
		'''menu and menu items in menubar'''
		menu = wx.MenuBar()

		fileMenu = wx.Menu()
		self.new_cfg = fileMenu.Append(wx.ID_NEW, '&New')
		self.open_cfg = fileMenu.Append(wx.ID_OPEN, '&Open')
		self.save_cfg = fileMenu.Append(wx.ID_SAVE, '&Save')
		fileMenu.AppendSeparator()
		self.qmi = fileMenu.Append(wx.ID_EXIT, '&Quit')

		viewMenu = wx.Menu()
		self.view_console = viewMenu.Append(wx.ID_ANY, '&Console')
		self.view_bsp_list = viewMenu.Append(wx.ID_VIEW_LIST, 'BSP_List')
		viewMenu.AppendSeparator()

		toolsMenu = wx.Menu()
		self.waf_configure = toolsMenu.Append(wx.ID_ANY, '&Configure')
		self.waf_build = toolsMenu.Append(wx.ID_ANY, '&Build')
		toolsMenu.AppendSeparator()

		stopMenu = wx.Menu()
		self.stop_configure = stopMenu.Append(wx.ID_ANY, '&Stop Configure')
		self.stop_build = stopMenu.Append(wx.ID_ANY, '&Stop Build')
		self.stop_configure.Enable(False)
		self.stop_build.Enable(False)

		menu.Append(fileMenu, '&File')
		menu.Append(viewMenu, '&View')
		menu.Append(toolsMenu, '&Tools')
		menu.Append(stopMenu, '&Stop')
		
		return menu
