import wx


class CalculatorApp(wx.App):
    def OnInit(self):
        frame = CalculatorFrame(None, title="Calculator")
        frame.Show()
        return True


class CalculatorFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, size=(400, 450))
        self.SetMinSize((400, 450))

        # Top-level panel and sizer
        self.panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Result Bar
        self.result_bar = wx.TextCtrl(self.panel, style=wx.TE_RIGHT, size=(-1, 30))
        main_sizer.Add(self.result_bar, flag=wx.EXPAND | wx.ALL, border=5, proportion=0)

        # Horizontal sizer for hidden panel and main grid
        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        ### Hidden Panel ###
        self.hidden_panel = wx.Panel(self.panel)
        self.hidden_sizer = wx.FlexGridSizer(5, 4, 5, 5)

        for i in range(4):
            spacer = wx.StaticText(self.hidden_panel, label="")
            self.hidden_sizer.Add(spacer, 0, wx.EXPAND | wx.ALL, border=5)
        self.hidden_sizer.SetItemMinSize(spacer, -1, 45)

        functions = [
            "π", "e", "sin", "cos",
            "tan", "(", ")", "√x",
            "x²", "x³", "xⁿ", "10ⁿ",
            "log", "ln", "1/x", "|x|"
        ]

        for func in functions:
            button = wx.Button(self.hidden_panel, label=func)
            self.hidden_sizer.Add(button, 0, wx.EXPAND | wx.ALL, border=5)

        for row in range(1, 5):
            self.hidden_sizer.AddGrowableRow(row)
        for col in range(4):
            self.hidden_sizer.AddGrowableCol(col)

        self.hidden_panel.SetSizerAndFit(self.hidden_sizer)
        self.hidden_panel.Hide()

        ### Main Grid Panel ###
        self.main_grid_panel = wx.Panel(self.panel)
        self.main_grid_sizer = wx.GridBagSizer()
        self.main_grid_panel.SetSizer(self.main_grid_sizer)

        clear_button = wx.Button(self.main_grid_panel, label="Clear")
        self.main_grid_sizer.Add(clear_button, pos=(0, 1), flag=wx.EXPAND | wx.ALL, border=5)
        self.main_grid_sizer.Add(wx.Button(self.main_grid_panel, label="⌫"), pos=(0, 2), flag=wx.EXPAND | wx.ALL, border=5)
        self.main_grid_sizer.Add(wx.Button(self.main_grid_panel, label="="), pos=(0, 3), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=5)

        self.main_grid_sizer.SetItemMinSize(clear_button, -1, 50)

        self.expand_button = wx.Button(self.main_grid_panel, label="<", size=(15, -1))
        self.main_grid_sizer.Add(self.expand_button, pos=(1, 0), span=(4, 1), flag=wx.EXPAND | wx.ALL, border=5)
        self.expand_button.Bind(wx.EVT_BUTTON, self.on_expand)

        calculator_buttons = [
            "7", "8", "9", "÷",
            "4", "5", "6", "X",
            "1", "2", "3", "-",
            "Ans", "0", ",", "+"
        ]
        for index, label in enumerate(calculator_buttons):
            row = 1 + index // 4
            col = 1 + index % 4
            button = wx.Button(self.main_grid_panel, label=label)
            self.main_grid_sizer.Add(button, pos=(row, col), flag=wx.EXPAND | wx.ALL, border=5)

        for row in range(1, 5):
            self.main_grid_sizer.AddGrowableRow(row)
        for col in range(1, 4):
            self.main_grid_sizer.AddGrowableCol(col)

        horizontal_sizer.Add(self.hidden_panel, flag=wx.EXPAND | wx.ALL, proportion=1)
        horizontal_sizer.Add(self.main_grid_panel, flag=wx.EXPAND | wx.ALL, proportion=1)
        main_sizer.Add(horizontal_sizer, flag=wx.EXPAND | wx.ALL, proportion=1)
        self.panel.SetSizerAndFit(main_sizer)

        self.Center()

    def on_expand(self, event):
        if self.hidden_panel.IsShown():
            self.hidden_panel.Hide()
            self.expand_button.SetLabel("<")
            self.SetMinSize((400, 450))
            self.SetSize(self.GetSize().GetWidth() // 2, self.GetSize().GetHeight())
        else:
            self.hidden_panel.Show()
            self.expand_button.SetLabel(">")
            self.SetMinSize((800, 450))
            self.SetSize(self.GetSize().GetWidth() * 2, self.GetSize().GetHeight())
        self.panel.Layout()
        self.panel.Refresh()
        self.panel.Update()


if __name__ == "__main__":
    app = CalculatorApp()
    app.MainLoop()