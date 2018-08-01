#!/usr/bin/env python2
# encoding: utf-8

import glob, os

#   Description : 
#                   This application reads all the logs in the system and and it's address to parse it to main file
#   Todo        :
#                   [ ] Search Log files in the Folder
#                   [ ] import all those name as string
#                   [ ] import address of the log file
#                   [ ] count the logs
#                   [ ] parsig smoothly


def getTxTFile():
    logList = []
    os.chdir("./logs")
    for file in glob.glob('*.txt'):
        file = file[:-4]
        logList.append(file)
    return logList

if __name__ == "__main__":
    getTxTFile()
        

