
#!/usr/bin/env python2
# encoding: utf-8

#   Description :
#                   It is main pythong file, it allows the program to run all together. This application only does Terminal User Interaface. The other's should
#                   programmed on seperate file.
#   Todo        :
#                   [ ] Much smoother TUI system

import npyscreen
from getLogList import *
from pushLogs import *
from settings import *



class SettingApp(npyscreen.NPSApp):
    def __init__(self):
        email = ''
        username = None
        Properties = None
        logName = None

    def main(self):
        msgFront = npyscreen.Form(name = 'Please Answer Following questions to configure your settings')
        self.username =  msgFront.add(npyscreen.TitleText, name = "User Name: ", )
        self.email = msgFront.add(npyscreen.TitleText, name = "email: ")
        ml = msgFront.add(npyscreen.MultiLineEdit,value = "",max_height=3, rely=4)

        self.logName= msgFront.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick application You want to store",values = getTxTFile(), scroll_exit=True)
        msgFront.edit()
    
    def setDataType(self):
        self.username = self.username.get_value()
        self.email = self.email.get_value()
        self.logName = self.logName.get_selected_objects()

    def createSettings(self):
        writeSettings(self.username, self.email, self.logName)
    
    def formalizeAndSend(self):
        mainLogFunc(self.username, self.email, self.logName)
    
    def sendLog(self):
        sendLogToStorage(self.logName)


if __name__ == "__main__":
    App = SettingApp()
    App.run()
    App.setDataType()
    App.createSettings()
    App.formalizeAndSend()
    App.sendLog()

