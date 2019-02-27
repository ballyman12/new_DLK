from threading import Thread
import time
import pymysql
import os
import re
import RPi.GPIO as GPIO

def have_use(RFID_user):
    print("Hello")
    print("%s" %RFID_user)
def dont_user():
    print("Try Agian")

def input_user() :

    while True :
            msg=os.popen('/usr/bin/nfc-poll').read()
            print(msg)

            buffers= msg.splitlines()
            #print buffers
            for buffer in buffers:
                if(buffer.find('NFCID1') != -1):
                        rfid = re.sub(" ","",buffer.split(':',1)[1])
                        msg=""
                        buffer=""
                        buffers=""
                        break

            RFID_user = str(rfid)
            print(RFID_user)
            #RFID_user=""
            if(RFID_user):
                have_use(RFID_user)
            else :
                dont_user()

            RFID_user=""

            time.sleep(5)



thread1 = Thread(target=input_user)
#thread2 = Thread(target=publish_log_status)
thread1.start()
