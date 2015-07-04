#! /usr/bin/env python
# encoding: UTF-8

#no longer being used - kept for references only
import wx

'''create multilayered tabs - a set of tabs, with each tab containing another set of tabs'''
class tabSet(wx.Notebook):
        def __init__(self, parent, num):
		##TODO: name properly
		s1 = (400,400)
		n1 = "outer"
                self.outerNB = noteSet(parent, name=n1, no_of_tabs=num, style=wx.NB_TOP, size=s1)
		for i, val in enumerate(self.outerNB.tabs):
			n2="outer"+str(i+1)+"inner"
			s2 = (300,300)
                        self.innerNB = noteSet(val, name=n2, no_of_tabs=num+1, style=wx.NB_LEFT,size=s2)

'''create notebook - set of tabs'''
class noteSet(wx.Notebook):
        def __init__(self, parent, name, no_of_tabs, style, size):
                nb = wx.Notebook(parent, style = style, size = size)
                self.tabs = []
                self.names = []
                self.p = []
                for i in xrange(no_of_tabs):
                        n = name
                        n = n+str(i+1)
                        self.names.append(n)
                        self.p.append(tabPanel(nb, self.names[i]))
                        self.tabs.append(self.p[i])
                        nb.AddPage(self.tabs[i], self.names[i])

'''each page of the notebook is a simple panel'''
class tabPanel(wx.Panel):
        def __init__(self, parent, name):
                wx.Panel.__init__(self, parent, name = name)

