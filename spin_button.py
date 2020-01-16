import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        self.text = wx.TextCtrl(self, -1, "1", (30, 50), (60, -1))
        h = self.text.GetSize().height
        w = self.text.GetSize().width + self.text.GetPosition().x + 2

        self.spinButton = wx.SpinButton(self, -1,
                                        (w, 50),
                                        (h * 2 / 3, h),
                                        wx.SP_VERTICAL)

        self.spinButton.SetRange(1, 100)
        self.spinButton.SetValue(1)

        self.Bind(wx.EVT_SPIN, self.on_spin, self.spinButton)

    def on_spin(self, event):
        self.text.SetValue(str(event.GetPosition()))
