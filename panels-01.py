import wx

from webkit_gtk import WKHtmlWindow as HtmlWindow

class TestWKPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.html = HtmlWindow(self)
        self.html.SetEditable(True)

        self.box = wx.BoxSizer(wx.VERTICAL)
        self.box.Add(self.html, 1, wx.EXPAND)

        self.SetSizer(self.box)
        self.Layout()

        self.html.Hide()
        self.panel1 = wx.Panel(self)
        self.hurrr = wx.StaticText(self.panel1, label="Hello!")

        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.box2.Add(self.panel1, 1, wx.EXPAND)

        self.SetSizer(self.box2)
        self.Layout()


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)
        self.Show()

        TestWKPanel(self)

        # This is needed for wxPython2.8,
        # for 2.6 doesnt hurt
        self.SendSizeEvent()


if __name__ == '__main__':
    app = wx.App()
    f = Frame()
    app.MainLoop()
