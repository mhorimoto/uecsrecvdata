#! /usr/bin/env python3
###! /opt/rh/rh-python36/root/usr/bin/python
#coding: utf-8
#
from socket import *
import sys
import os
import datetime
import time

VERSION = "2.00"
HOST = ''
PORT = 16520
LOGF = "/var/log/uecs/recvdata.log"

try:
  lgf = open(LOGF,'a',1)   # line buffering
except:
  print("Can not open logfile {0}".format(lgf))
  quit()

s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

while True:
  msg, address = s.recvfrom(512)
  if msg == ".":
    print("Sender is closed")
    break
  a=datetime.datetime.now()
  d="{0:4d}/{1:02d}/{2:02d}".format(a.year,a.month,a.day)
  t="{0:02d}:{1:02d}:{2:02d}".format(a.hour,a.minute,a.second)
  x="{0}-{1}".format(d,t)
  # <?xml version="1.0"?><UECS ver="1.00-E10">
  lgf.write("{0} {1}\n".format(x,msg.decode()))
lgf.close()
s.close()
sys.exit()

