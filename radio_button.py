import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 400))

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        self.rb1 = wx.RadioButton(self, label="Cat", pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(self, label="Dog", pos=(10, 40))
        self.rb2 = wx.RadioButton(self, label="Tiger", pos=(10, 70))

        self.label = wx.StaticText(self, label="", pos=(10, 100))

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio_button)

    def on_radio_button(self, e):
        rb = e.GetEventObject()
        self.label.SetLabelText("You Have Selected " + rb.GetLabel())
