#! /usr/bin/env python3
#coding: utf-8
#
from socket import *
import sys
import os
import datetime
import time
#import ambient
import xml.etree.ElementTree as ET

VERSION="2.30"
HOST = ''
PORT = 16520
LOGF = "/var/log/uecs/recvdata.log"
#AMBF = "/var/log/uecs/amb.log"
TMPD = "/tmp/ckua-"

try:
  lgf = open(LOGF,'a',1)   # line buffering
except:
  print("Can not open logfile {0}".format(lgf))
  quit()

#try:
#  ambf = open(AMBF,'a',1)
#except:
#  print("Can not open ambient logfile {0}".format(ambf))
#  quit()


s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))
a=datetime.datetime.now()
d = "{0:4d}/{1:02d}/{2:02d}".format(a.year,a.month,a.day)
t = "{0:02d}:{1:02d}:{2:02d}".format(a.hour,a.minute,a.second)
x = "{0}-{1}".format(d,t)
lgf.write("\n{0} START UECS recvdata.py VER.{1}\n".format(x,VERSION))
#ambf.write("\n{0} START UECS recvdata.py VER.{1}\n".format(x,VERSION))
#pmnh191 = 0
#pmnh192 = 0

while True:
  msg, address = s.recvfrom(4096)
  a=datetime.datetime.now()
  d="{0:4d}/{1:02d}/{2:02d}".format(a.year,a.month,a.day)
  t="{0:02d}:{1:02d}:{2:02d}".format(a.hour,a.minute,a.second)
  x="{0}-{1}".format(d,t)
  # <?xml version="1.0"?><UECS ver="1.00-E10">
  lgf.write("{0} {1}\n".format(x,msg.decode()))
  xmlroot = ET.fromstring(msg)
  ipa = xmlroot.find('IP').text
  SMPF=TMPD+ipa+".chk"
  if (os.path.exists(SMPF)):
    os.remove(SMPF)
  # mn191 = int(a.minute)
  # mn192 = int(a.minute)
  # if (mn191%5==0) and (pmnh191!=mn191):
  #   xmlroot191 = xmlroot
  #   #    lgf.write("{0} 5min interval {1}\n".format(x,xmlroot.find('IP').text))
  #   if (xmlroot191.find('IP').text=="192.168.0.191"):
  #     for dt in xmlroot191.iter('DATA'):
  #       if (dt.attrib['type']=="InAirTemp.mIC"):
  #         d1911 = dt.text
  #       if (dt.attrib['type']=="InAirHumid.mIC"):
  #         d1912 = dt.text
  #       if (dt.attrib['type']=="CO2.mIC"):
  #         d1913 = dt.text
  #       if (dt.attrib['type']=="cnd.mIC"):
  #         am191 = ambient.Ambient(15884,'ed86025f2ac0ee2b')
  #         ambf.write("{0} 192.168.0.191 {2} {3} {4}\n".format(x,d1911,d1912,d1913))
  #         am191.send({'d1': d1911, 'd2': d1912, 'd3': d1913})
  #         d="{0:4d}/{1:02d}/{2:02d}".format(a.year,a.month,a.day)
  #         t="{0:02d}:{1:02d}:{2:02d}".format(a.hour,a.minute,a.second)
  #         x="{0}-{1}".format(d,t)
  #         ambf.write("{0} Sending Done\n".format(x))
  #         d1911 = 0.0
  #         d1912 = 0.0
  #         d1913 = 0
  #         pmnh191 = mn191

  # if (mn192%5==0) and (pmnh192!=mn192):
  #   xmlroot192 = xmlroot
  #   if (xmlroot192.find('IP').text=="192.168.0.192"):
  #     for dt in xmlroot192.iter('DATA'):
  #       if (dt.attrib['type']=="InAirTemp.mIC"):
  #         d1921 = dt.text
  #       if (dt.attrib['type']=="InAirHumid.mIC"):
  #         d1922 = dt.text
  #       if (dt.attrib['type']=="CO2.mIC"):
  #         d1923 = dt.text
  #       if (dt.attrib['type']=="cnd.mIC"):
  #         am192 = ambient.Ambient(15962,'f084426b6bed4c3e')
  #         ambf.write("{0} 192.168.0.192 {2} {3} {4}\n".format(x,d1921,d1922,d1923))
  #         am192.send({'d1': d1921, 'd2': d1922, 'd3': d1923})
  #         d="{0:4d}/{1:02d}/{2:02d}".format(a.year,a.month,a.day)
  #         t="{0:02d}:{1:02d}:{2:02d}".format(a.hour,a.minute,a.second)
  #         x="{0}-{1}".format(d,t)
  #         ambf.write("{0} Sending Done\n".format(x))
  #         d1921 = 0.0
  #         d1922 = 0.0
  #         d1923 = 0
  #         pmnh192 = mn192

lgf.close()
#ambf.close()
s.close()
sys.quit()

