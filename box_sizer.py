import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        v_box_sizer = wx.BoxSizer(wx.VERTICAL)
        h_box_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.label = wx.StaticText(self, label="This is a label", style=wx.ALIGN_CENTER)
        v_box_sizer.Add(self.label, 0, wx.EXPAND)

        self.label2 = wx.StaticText(self, label="This is Second label", style=wx.ALIGN_CENTER)
        v_box_sizer.Add(self.label2, 0, wx.EXPAND)

        self.label3 = wx.StaticText(self, label="This is third label", style=wx.ALIGN_CENTER)
        h_box_sizer.Add(self.label3, 0, wx.EXPAND)

        self.label4 = wx.StaticText(self, label="This is fourth label", style=wx.ALIGN_CENTER)
        h_box_sizer.Add(self.label4, 0, wx.EXPAND, wx.ALIGN_RIGHT, 20)
        h_box_sizer.AddStretchSpacer(1)

        v_box_sizer.Add(h_box_sizer, 1, wx.ALL | wx.EXPAND)

        self.SetSizer(v_box_sizer)
        # self.SetSizer(h_box_sizer)


