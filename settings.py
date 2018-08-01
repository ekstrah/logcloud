import os.path
import datetime
import npyscreen

now = datetime.datetime.now()

def writeSettings(userName, email, logList):
    logCount = len(logList)
    os.chdir('../')
    with open('setting.config', 'w') as fp:
        fp.write('userName='+userName+'\n')
        fp.write('email='+email+'\n')
        fp.write('dateOfCreation='+now.strftime("%Y-%m-%d %H:%M")+'\n')
        fp.write('numOfLog='+str(logCount)+'\n\n')
        fp.write('logs=[\n')
        for log in logList:
            fp.write(log+',\n')
        fp.write(']')
    print 'Initializing Settings for your use ending'

def configExist():
    Fstatus = os.path.isfile('setting.config')
    return Fstatus 



if __name__ == '__main__':
    writeSettings('dongho', 'dongho@dongho.com', ['Hey', 'How are  you?'])
    print configExist()