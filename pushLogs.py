#!/usr/bin/env python2
# encoding: utf-8
import datetime
import json
from sender import *
import time
import psycopg2 as p

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
    dateOfSentTime = str(datetime.datetime.now())
    logDict['dateOfSent'] = dateOfSentTime
    eachLogDict = {}
    logDict['logName'] = 'http://155.230.91.221:8000/ekstrah'
    writeToJSONFile(logDict)
    connectsDatabase(userName, logCount, 'http://155.230.92.221:8000/ekstrah', email, dateOfSentTime)



def writeToJSONFile(dataDict):
    fileNamePathExt = 'parsingText.json'
    with open(fileNamePathExt, 'w') as fp:
        json.dump(dataDict, fp, indent=4)


def sendLogToStorage(logList):
    for log in logList:
        log = log+'.txt'
        print log
        sendLog(log)
        time.sleep(10)

def connectsDatabase(username, logcount, logname, email, dateofsent):
    #connecting to database: you have to give user, password and database name
    db = p.connect(database='log_database', user='admin2', password='admin', host='155.230.91.221', port='5432')
    insert_to_db(username, logcount, logname, email, dateofsent, db)

def insert_to_db(username, logcount, logname, email, dateofsent, db):
    cursor = db.cursor()
    query = "INSERT INTO logs_schema.logs_table (username, logcount, logname, email, dateofsent) VALUES (%s, %s, %s, %s, %s);"
    values = (username, logcount, logname, email, dateofsent)
    cursor.execute(query, values)
    db.commit()


def loadLogStr(logName):
    logString = []
    with open(logName, 'r') as logF:
        logString.append(logF.read().replace('\n', ''))
    return logString


if __name__ == "__main__":
    # mainLogFunc('ekstrah', 'ekstrah@naver.com', ['APACHE', 'POSTFIX', 'REDHAT'])
    connectsDatabase()