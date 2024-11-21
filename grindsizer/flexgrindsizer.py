import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        flex_grid = wx.FlexGridSizer(2, 2, 10, 10)

        btn1 = wx.Button(panel, label="Button 1")
        btn2 = wx.Button(panel, label="Button 2")
        btn3 = wx.Button(panel, label="Button 3")
        btn4 = wx.Button(panel, label="Button 4")

        flex_grid.AddMany([(btn1, 0, wx.EXPAND), (btn2, 0, wx.EXPAND),
                           (btn3, 0, wx.EXPAND), (btn4, 0, wx.EXPAND)])

        flex_grid.AddGrowableRow(0)  # Row 0 will grow proportionally with the window
        flex_grid.AddGrowableCol(1)  # Column 1 will grow proportionally with the window

        panel.SetSizer(flex_grid)


app = wx.App(False)
frame = MyFrame(None, title="FlexGridSizer Example")
frame.Show()
app.MainLoop()
