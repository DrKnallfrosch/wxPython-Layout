import wx



class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        grid_bag = wx.GridBagSizer(10, 10)

        btn1 = wx.Button(panel, label="Button 1")
        btn2 = wx.Button(panel, label="Button 2")
        btn3 = wx.Button(panel, label="Button 3")

        grid_bag.Add(btn1, pos=(0, 0), span=(1, 2), flag=wx.EXPAND)
        grid_bag.Add(btn2, pos=(1, 0), flag=wx.EXPAND)
        grid_bag.Add(btn3, pos=(1, 1), flag=wx.EXPAND)

        grid_bag.AddGrowableCol(0)  # Make column 0 growable
        grid_bag.AddGrowableCol(1)  # Make column 1 growable

        panel.SetSizer(grid_bag)


app = wx.App(False)
frame = MyFrame(None, title="GridBagSizer Example")
frame.Show()
app.MainLoop()
