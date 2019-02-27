import time
import pymysql
import random
import paho.mqtt.client as mqtt

host = "broker.mqttdashboard.com"
port = 8000


status = 0
    
def check_time():

    i = 10
    locker_open = 0
    while i > -1 :
        
        #locker_open = 0
        #print(i)
        if(locker_open == 1):
            #return locker_open
            break
        elif (locker_open == 5) :
            #return locker_open
            break
        #elif (i==5):
            #locker_open = 1
        
        locker_open = random.randint(0,1) ## รอรับค่า Menetic sensor
        
    
        i-=1
        time.sleep(1)
    return locker_open

def check_mqtt(status_id):
    global status
    status = status_id
    #print(status)
    

def check_cancel():
    check_cancel = 0
    global status
    i = 10
    while i > -1 :
        print(i)
        if(check_cancel != 0):
            status = 0
            break

        check_cancel = status # รอรับค่าหน้า page
        print(check_cancel)
        i-=1
        time.sleep(1)
    return check_cancel

def input_cancel() :
    input_cancel = 0
    global status
    i = 5
    while i > -1 :
        print(i)
        if(input_cancel != 0):
            status = 0
            break

        input_cancel = status # รอรับค่าหน้า page
        print(input_cancel)
        i-=1
        time.sleep(1)
    return input_cancel

    

        
         


    
    

