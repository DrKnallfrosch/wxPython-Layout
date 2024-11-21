import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        grid = wx.GridSizer(2, 2, 10, 10)  # 2x2 grid, with spacing between cells

        btn1 = wx.Button(panel, label="Button 1")
        btn2 = wx.Button(panel, label="Button 2")
        btn3 = wx.Button(panel, label="Button 3")
        btn4 = wx.Button(panel, label="Button 4")

        grid.AddMany([(btn1, 0, wx.EXPAND), (btn2, 0, wx.EXPAND),
                      (btn3, 0, wx.EXPAND), (btn4, 0, wx.EXPAND)])

        panel.SetSizer(grid)


app = wx.App(False)
frame = MyFrame(None, title="GridSizer Example")
frame.Show()
app.MainLoop()
