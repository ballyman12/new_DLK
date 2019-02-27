import os
import re
import RPi.GPIO as GPIO
#from Tkinter import *

while True:
    msg=os.popen('/usr/bin/nfc-poll').read()
    print(msg)

    buffers= msg.splitlines()
    #print buffers
    for buffer in buffers:
        if(buffer.find('NFCID1') != -1):
                rfid=re.sub(" ","",buffer.split(':',1)[1])
                msg=""
                buffer=""
                buffers=""
                break

    str_RFID = str(rfid)
    print(str_RFID)
    str_RFID=""
