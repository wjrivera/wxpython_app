# https://codeloop.org/category/wxpython-tutorials/

import wx


class MyApp(wx.App):
    def OnInit(self):
        """
        # Box Sizer
        import box_sizer
        self.frame = box_sizer.MyFrame(parent=None, title="Sizers")
        import grid_sizer
        self.frame = grid_sizer.MyFrame(parent=None, title="Grid Sizer")
        import buttons
        self.frame = buttons.MyFrame(parent=None, title="Buttons")
        import toggle_button
        self.frame = toggle_button.MyFrame(parent=None, title="Buttons")
        import bitmap
        self.frame = bitmap.MyFrame(parent=None, title="Buttons")
        import checkbox
        self.frame = checkbox.MyFrame(parent=None, title="Buttons")
        import radio_button
        self.frame = radio_button.MyFrame(parent=None, title="Buttons")
        from question_dialog_box import MyFrame
        self.frame = MyFrame(parent=None, title="Message Box")
        from spin_button import MyFrame
        self.frame = MyFrame(parent=None, title="Message Box")
        from grid_list import MyFrame
        self.frame = MyFrame(parent=None, title="Message Box")
        """
        from grid_customized import MyFrame
        self.frame = MyFrame(parent=None, title="Message Box")

        self.frame.Show()
        return True


app = MyApp()
app.MainLoop()
