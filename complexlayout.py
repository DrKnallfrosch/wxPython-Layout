import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # Erstellen einer beschrifteten Box für die Gruppe der Bedienelemente
        static_box = wx.StaticBox(panel, label="Einstellungen")
        static_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        # Erstellen des FlexGridSizers, um die Bedienelemente in einem Raster anzuordnen
        flex_grid = wx.FlexGridSizer(rows=3, cols=2, hgap=10, vgap=10)

        # Beispielhafte Bedienelemente
        label1 = wx.StaticText(panel, label="Option 1:")
        input1 = wx.TextCtrl(panel)
        label2 = wx.StaticText(panel, label="Option 2:")
        input2 = wx.TextCtrl(panel)
        label3 = wx.StaticText(panel, label="Option 3:")
        input3 = wx.TextCtrl(panel)

        # Hinzufügen der Bedienelemente zum FlexGridSizer
        flex_grid.Add(label1, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_grid.Add(input1, flag=wx.EXPAND)
        flex_grid.Add(label2, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_grid.Add(input2, flag=wx.EXPAND)
        flex_grid.Add(label3, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        flex_grid.Add(input3, flag=wx.EXPAND)

        # Festlegen, dass alle Spalten in der Breite anpassbar sind
        flex_grid.AddGrowableCol(1)  # Macht die zweite Spalte anpassbar

        # FlexGridSizer zum StaticBoxSizer hinzufügen
        static_sizer.Add(flex_grid, flag=wx.EXPAND | wx.ALL, border=10)

        # StaticBoxSizer zum Panel hinzufügen
        panel.SetSizer(static_sizer)

        # Fenstergröße festlegen
        self.SetSize((400, 250))


app = wx.App(False)
frame = MyFrame(None, title="StaticBoxSizer mit FlexGridSizer Beispiel")
frame.Show()
app.MainLoop()
