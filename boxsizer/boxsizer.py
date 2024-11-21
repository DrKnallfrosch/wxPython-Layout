import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Erstellen eines Panels innerhalb des Frames
        panel = wx.Panel(self)

        # Erstellen eines vertikalen BoxSizers
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Erstellen von drei Buttons
        btn1 = wx.Button(panel, label="Button 1")
        btn2 = wx.Button(panel, label="Button 2")
        btn3 = wx.Button(panel, label="Button 3")

        # Hinzufügen der Buttons zum Sizer mit optionalen Rändern und Ausrichtungsflags
        vbox.Add(btn1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(btn2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(btn3, flag=wx.EXPAND | wx.ALL, border=10)

        # Setzen des Sizers für das Panel
        panel.SetSizer(vbox)


# Erstellen der App-Instanz
app = wx.App(False)

# Erstellen und Anzeigen des Frames
frame = MyFrame(None, title="BoxSizer Example")
frame.Show()

# Starten der Haupt-Ereignisschleife
app.MainLoop()
