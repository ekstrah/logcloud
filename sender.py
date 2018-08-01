#!/usr/bin/env python

from socket import *
import sys
from subprocess import call
def sendLog(logName):
    logName = './logs/'+logName
    s = socket(AF_INET,SOCK_DGRAM)
    host = '155.230.91.221'
    port = 9999
    buf =1024
    addr = (host,port)

    file_name = logName
    s.sendto(file_name,addr)

    f=open(file_name,"rb")
    data = f.read(buf)
    while (data):
        if(s.sendto(data,addr)):
            print "sending ..."
            data = f.read(buf)
    s.close()
    f.close()

