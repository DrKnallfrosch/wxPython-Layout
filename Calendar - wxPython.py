import wx
import wx.adv
import datetime

class GridSizerApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, size=(700, 375))
        self.SetMinSize((700, 375))

        # Main panel and sizer
        panel = wx.Panel(self)
        grid_sizer = wx.GridSizer(rows=2, cols=2, hgap=10, vgap=10)

        # 1. Calendar (Top Left)
        calendar = wx.adv.CalendarCtrl(panel)
        calendar.SetMinSize((300, 200))  # Set a minimum size for the calendar
        grid_sizer.Add(calendar, 0, wx.EXPAND | wx.ALL, border=5)

        # 2. Scrollable List (Top Right)
        scrollable_list = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        scrollable_list.InsertColumn(0, "Appointments", width=200)
        for i in range(20):
            scrollable_list.InsertItem(i, f"Appointment {i+1}")
        scrollable_list.SetMinSize((300, 200))  # Set a minimum size for the list
        grid_sizer.Add(scrollable_list, 0, wx.EXPAND | wx.ALL, border=5)

        # 3. Horizontal BoxSizer with Date Pickers (Bottom Left)
        date_picker_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Change parent to `date_picker_sizer_container`
        date_picker_sizer_container = wx.Panel(panel)  # Panel to wrap the date pickers

        year_picker = wx.SpinCtrl(date_picker_sizer_container, min=1900, max=2100, initial=2024, size=(80, -1))
        month_picker = wx.SpinCtrl(date_picker_sizer_container, min=1, max=12, initial=1, size=(80, -1))
        day_picker = wx.SpinCtrl(date_picker_sizer_container, min=1, max=31, initial=1, size=(60, -1))

        year_picker.SetMinSize((80, -1))
        month_picker.SetMinSize((80, -1))
        day_picker.SetMinSize((60, -1))

        date_picker_sizer.Add(year_picker, 0, wx.RIGHT, 10)
        date_picker_sizer.Add(month_picker, 0, wx.RIGHT, 10)
        date_picker_sizer.Add(day_picker, 0)

        date_picker_sizer_container.SetSizer(date_picker_sizer)
        date_picker_sizer_container.SetMinSize((300, 50))  # Minimum size for the panel containing the date pickers
        grid_sizer.Add(date_picker_sizer_container, 0, wx.EXPAND | wx.ALL, border=5)

        # 4. WrapSizer with Buttons (Bottom Right)
        wrap_sizer_panel = wx.Panel(panel)  # Panel to hold the WrapSizer
        wrap_sizer = wx.WrapSizer(wx.HORIZONTAL)

        action = ["Add Appointment", "Edit Appointment", "Remove Appointment", "Request Appointment"]

        for i in range(1, 5):
            button = wx.Button(wrap_sizer_panel, label=action[i-1])
            button.SetMinSize((150, 40))  # Set a minimum size for the buttons
            wrap_sizer.Add(button, 0, wx.ALL, 5)

        wrap_sizer_panel.SetSizer(wrap_sizer)
        wrap_sizer_panel.SetMinSize((300, 50))  # Set a minimum size for the wrap sizer panel
        grid_sizer.Add(wrap_sizer_panel, 0, wx.EXPAND | wx.ALL , border=5)

        # Set the sizer for the main panel
        panel.SetSizerAndFit(grid_sizer)

        self.CreateStatusBar(2)
        self.update_status_bar()

        self.Show()

    def update_status_bar(self):
        self.SetStatusWidths([-1, 150])
        self.SetStatusText("Hausarzt Mustermann", 0)  # Left section
        self.SetStatusText(datetime.datetime.now().strftime("%Y-%m-%d"), 1)  # Right section
        return


if __name__ == "__main__":
    app = wx.App(False)
    frame = GridSizerApp(None, title="Calendar Manager")
    app.MainLoop()
