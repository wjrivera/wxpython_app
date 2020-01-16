import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label="Hello")
        vbox.Add(self.label, 0, wx.EXPAND)

        self.toggleBtn = wx.ToggleButton(self, label="Click To On")
        vbox.Add(self.toggleBtn, 0)

        self.toggleBtn.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_click)

        self.SetSizer(vbox)

    def on_toggle_click(self, event):
        state = event.GetEventObject().GetValue()

        if state:
            self.label.SetLabelText("Off")
            event.GetEventObject().SetLabel("Click To Off")

        else:
            self.label.SetLabelText("On")
            event.GetEventObject().SetLabel("Click To On")
