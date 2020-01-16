import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 400))

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.label = wx.StaticText(self, label="Changed Text")

        sizer.Add(self.label, 1, wx.EXPAND)

        self.btn = wx.Button(self, label="Click Me")
        sizer.Add(self.btn, 0)

        self.btn.Bind(wx.EVT_BUTTON, self.on_click_me)

        self.SetSizer(sizer)

    def on_click_me(self, event):
        self.label.SetLabelText("Hello World")
