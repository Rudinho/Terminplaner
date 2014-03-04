#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rudolph
#
# Created:     01.03.2014
# Copyright:   (c) Rudolph 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
import time
import  wx.calendar as wxcal#Das Zeug hier wird alles gebraucht

#the main menu is created. It inherits most of its features from wx.Frame, 
class Menu_Main(wx.Frame):
    def __init__(self, parent, title):
        super(Menu_Main, self).__init__(parent, title=title, #To be honest, I do not completely understand those lines. Any hints are appreciated
                               size=schirmsize)

        self.InitUI() #In General its more clever to outsource the initialization of the window. So above this comment general attributes
        #of the object should be defined, any kind of data structure you might need etc.



    def InitUI(self):
        mainpanel=wx.Panel(self,-1) #the Panel is just another kind of widget, as far as I know, derives from frame, is more suitable for
        #graphical changes
        
        
        #I could have created the calendar as an object on its own, not as an attribute of the mainframe, but I think its more clever to do,
        #because if you use functions that access methods and attributes of the calendar, it will be much easier that way
        self.cal2 = wxcal.GenericCalendarCtrl(mainpanel, -1, wx.DateTime.Today(),pos=(0,150),size=(165,150),style=wxcal.CAL_MONDAY_FIRST)
                                               #^# Inheritance of graphical widgets, does also hint at, on top of what this widget appears
                                               # If I would chose to inherit from Menu_Main(aka self) instead, the calendar might not even be visible
                                               #or some other weird thing might happen
                                               
        #Just a simple Static Text Box, most things should be pretty clear, just a reminder, for most arguments there are default values
        #you just have to declare the parent, and the label 
        txtstr="Haus"
        st1 = wx.StaticText(mainpanel, label=str(txtstr), style=wx.ALIGN_CENTRE,pos=(200,300))



        self.Centre()
        self.Show()








if __name__ == '__main__':
    program_name="Proto-Calendar"
    schirmsize=(600,500)
    app=wx.App()
    Menu_Main(None, title=program_name)
    app.MainLoop()
