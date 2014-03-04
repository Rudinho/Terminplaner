#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import time
import  wx.calendar as wxcal


class Hauptschirm(wx.Frame):
 
    def __init__(self, parent, title):
        super(Hauptschirm, self).__init__(parent, title=title,
                               size=schirmsize)

        #Allgemeine Einstellungen, und Paneloptions
        #create a satusbar, which shows current time
        self.statusbar= self.CreateStatusBar()
        self.statusbar.SetStatusText("Ready")
        
        self.panel=wx.Panel(self, -1)
        self.backgroundcolpanel="#2FEB96"
        self.panel.SetBackgroundColour(self.backgroundcolpanel)

        #Displayoptionen
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        
        #de = wx.StaticText(self.panel, -1, 'Germany', (500, 50))
        #de.SetFont(font)
        self.OnTimer(None)
        #self.time_display=wx.StaticText(self.panel, -1, self.time_,(500,75))
        self.timer=wx.Timer(self, -1)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        #Kalender
        cal2 = wxcal.GenericCalendarCtrl(self.panel, -1, wx.DateTime.Today(),pos=(0,0),size=(165,150),style=wxcal.CAL_MONDAY_FIRST)

        #self.tc3 = wx.TextCtrl(pnl, size=(180, -1))
        
        self.tc = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE,pos=(150,200))
        sendButton=wx.Button(self.panel, label="Save to File", pos=(300,200))
        sendButton.Bind(wx.EVT_BUTTON, save_to_file())
        #Rechte Seite vom Bildschirm
    def save_to_file(self,event):
        text_to_save=self.tc.GetValue()
        print(text_to_save)

        """for i in range(20, 385, 20):
            wx.StaticText(diary, label=str(x)+":00", pos=(5, i))
            wx.TextCtrl(diary, pos=(35, i),size=(180,-1))
            wx
            x+=1
            if x==24:
                break
            
        """
        
        self.Centre()
        self.Show()
    def OnTimer(self, event):
        current = time.localtime(time.time())
        self.time_=time.strftime("%X", current)
        #self.time_display=wx.StaticText(self.panel, -1, self.time_, (500,75))
        self.statusbar.SetStatusText(self.time_)
if __name__== "__main__":

    program_name="Rudis Custom Calendar"
    schirmsize=(600,600)
    app=wx.App()
    Hauptschirm(None, title=program_name)
    app.MainLoop()
