import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.cb1 = wx.CheckBox(self, label="Cat")
        vbox.Add(self.cb1)

        self.cb2 = wx.CheckBox(self, label="Dog")
        vbox.Add(self.cb2)

        self.cb3 = wx.CheckBox(self, label="Tiger")
        vbox.Add(self.cb3)

        self.label = wx.StaticText(self, label="")
        vbox.Add(self.label)

        self.SetSizer(vbox)

        self.Bind(wx.EVT_CHECKBOX, self.on_checked)

    def on_checked(self, e):
        cb = e.GetEventObject()
        self.label.SetLabelText('You Have Selected ' + cb.GetLabel())
