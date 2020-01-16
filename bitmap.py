import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 400))

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        image_file = "resources/pickaxe.png"
        image1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button1 = wx.BitmapButton(self, id=-1, bitmap=image1,
                                       size=(image1.GetWidth() + 40, image1.GetHeight() + 40))
        self.button1.SetLabel("Pickaxe")

        hbox.Add(self.button1, 0, wx.ALIGN_CENTER)
        self.button1.Bind(wx.EVT_BUTTON, self.on_clicked)

        image_file2 = "resources/pickaxe_dev.png"
        image2 = wx.Image(image_file2, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button2 = wx.BitmapButton(self, id=-1, bitmap=image2,
                                       size=(image2.GetWidth() + 40, image1.GetHeight() + 40))
        self.button2.SetLabel("Pickaxe DEV")

        hbox.Add(self.button2, 0, wx.ALIGN_CENTER)
        self.button2.Bind(wx.EVT_BUTTON, self.on_clicked)

        image_file3 = "resources/yellowpages.png"
        image3 = wx.Image(image_file3, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button3 = wx.BitmapButton(self, id=-1, bitmap=image3,
                                       size=(image3.GetWidth() + 40, image3.GetHeight() + 40))
        self.button3.SetLabel("Yellow Pages")

        hbox.Add(self.button3, 0, wx.ALIGN_CENTER)
        self.button3.Bind(wx.EVT_BUTTON, self.on_clicked)

        vbox.Add(hbox, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)

    def on_clicked(self, event):
        btn = event.GetEventObject().GetLabel()
        print("Label Of Pressed Button Is", btn)
