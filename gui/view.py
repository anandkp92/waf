#! /usr/bin/env python
# encoding: UTF-8

import wx
import noteSet

'''GUI view - with menu bar and tabs'''
class View(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title="RTEMS Config", pos = wx.DefaultPosition, size = wx.Size(600,400), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		self.outerNB = noteSet.noteSet(self, name="outer", style=wx.NB_TOP, size=wx.DefaultSize)
		self.mb  = menubar()
		self.SetMenuBar(self.mb)

'''menu and menu items in menubar'''
class menubar(wx.MenuBar):
	def __init__(self):
		wx.MenuBar.__init__(self)

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

		self.Append(fileMenu, '&File')
		self.Append(viewMenu, '&View')
		self.Append(toolsMenu, '&Tools')

