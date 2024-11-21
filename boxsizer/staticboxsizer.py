import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        static_box = wx.StaticBox(panel, label="Options")
        static_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        btn1 = wx.Button(panel, label="Option 1")
        btn2 = wx.Button(panel, label="Option 2")

        static_sizer.Add(btn1, flag=wx.ALL, border=5)
        static_sizer.Add(btn2, flag=wx.ALL, border=5)

        panel.SetSizer(static_sizer)


app = wx.App(False)
frame = MyFrame(None, title="StaticBoxSizer Example")
frame.Show()
app.MainLoop()
