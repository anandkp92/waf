import wx

class tabSet(wx.Notebook):
        def __init__(self, parent, num):
		##TODO: name properly
		s1 = (400,400)
		n1 = "outer"
                outerNB = noteSet(parent, name=n1, no_of_tabs=num, style=wx.NB_TOP, size=s1)
                for i in range(0,len(outerNB.tabs)):
			n2="outer"+str(i+1)+"inner"
			s2 = (300,300)
                        innerNB = noteSet(outerNB.tabs[i], name=n2, no_of_tabs=num+1, style=wx.NB_LEFT,size=s2)

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

class tabPanel(wx.Panel):
        def __init__(self, parent, name):
                wx.Panel.__init__(self, parent, name = name)
