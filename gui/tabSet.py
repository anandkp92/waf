import wx

##== set up a list of tabs/panes ==##
class tabSet(wx.Notebook):
        def __init__(self, parent, no_of_tabs):
		##== create set of outer tabs ==##
                outerNB = noteSet(parent, name = "outer", no_of_tabs = no_of_tabs, style=wx.NB_TOP, size = (400, 400))
                for i in range(0,len(outerNB.tabs)):
			##==create set of inner tabs for each outer tab ==##
			##!!! naming bit weird ##
                        innerNB = noteSet(outerNB.tabs[i], name = "outer"+str(i+1)+" inner", no_of_tabs = no_of_tabs+1, style = wx.NB_LEFT, size = (300,300))

##== create a notebook with 'no_of_tabs' tabs ==##
class noteSet(wx.Notebook):
        def __init__(self, parent, name, no_of_tabs, style, size):
                nb = wx.Notebook(parent, style = style, size = size)
                self.tabs = []
                self.names = []
                self.p = []
                for i in range(0, no_of_tabs):
                        n = name
                        n = n+str(i+1)
                        self.names.append(n)
                        self.p.append(tabPanel(nb, self.names[i]))
                        self.tabs.append(self.p[i])
                        nb.AddPage(self.tabs[i], self.names[i])

##== each tab is a Panel ==##
class tabPanel(wx.Panel):
        def __init__(self, parent, name):
                wx.Panel.__init__(self, parent, name = name)
