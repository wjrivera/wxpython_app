import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        self.button = wx.Button(self, label="Open Question Dialog", pos=(100, 100))
        self.Bind(wx.EVT_BUTTON, self.questionDialog)

    def questionDialog(self, event):
        dialog = wx.MessageDialog(None, "Do You Want To Close?", 'Close', wx.YES_NO | wx.ICON_QUESTION)
        result = dialog.ShowModal()

        if result == wx.ID_YES:
            print("Yes Closed")

        else:
            print("No Close")