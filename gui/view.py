#! /usr/bin/env python
# encoding: UTF-8

'''This file creates the looks of the gui - the menu, tab set'''

import wx
import noteSet

'''GUI view - with menu bar and tabs'''
class View(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title="RTEMS Config", pos = wx.DefaultPosition, size = wx.Size(600,400), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		self.outerNB = noteSet.noteSet(self, name="outer", style=wx.NB_TOP, size=wx.DefaultSize)
		self.mb  = self.menubar()
		self.SetMenuBar(self.mb)

	'''menu and menu items in menubar'''
	def menubar(self):
		menu = wx.MenuBar()

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

		menu.Append(fileMenu, '&File')
		menu.Append(viewMenu, '&View')
		menu.Append(toolsMenu, '&Tools')
	
		return menu
