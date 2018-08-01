#!/usr/bin/env python2
# encoding: utf-8
import datetime
import json
#   Description :
#                   This python file helps to push log files to the cloud with json format
#   Todo        :
#                   [ ] able to load all log files
#                   [ ] push to elasticsearch server
#                   [ ] sucessfull flag generate


###Customizing my dictionary class for further usage
def mainLogFunc(userName, email, logList):
    logDict = {}
    logCount = len(logList)
    logDict['userName'] = userName
    logDict['email'] = email
    logDict['logCount'] = logCount
    logDict['dateOfSent'] = str(datetime.datetime.now())
    eachLogDict = {}
    logDict['logName'] = eachLogDict
    for log in logList:
        logPath = './logs/'+log+'.txt'
        logString = loadLogStr(logPath)
        eachLogDict[log] = logString
    writeToJSONFile(logDict)


def writeToJSONFile(dataDict):
    fileNamePathExt = 'parsingText.json'
    with open(fileNamePathExt, 'w') as fp:
        json.dump(dataDict, fp, indent=4)



def loadLogStr(logName):
    logString = []
    with open(logName, 'r') as logF:
        logString.append(logF.read().replace('\n', ''))
    return logString


if __name__ == "__main__":
    mainLogFunc('ekstrah', 'ekstrah@naver.com', ['APACHE', 'POSTFIX', 'REDHAT'])