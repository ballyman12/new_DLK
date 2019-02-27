import time
import pymysql
import random
import paho.mqtt.client as mqtt

host = "broker.mqttdashboard.com"
port = 8000


status = 0

def check_mqtt(status_id):
    global status
    status = status_id
    #print(status)
    

def check_admin():
    check_admin = 0
    global status
    i = 10
    while i > -1 :
        print(i)
        if(check_admin != 0):
            status = 0
            break

        check_admin = status # รอรับค่าหน้า page
        print(check_admin)
        i-=1
        time.sleep(1)
    return check_admin

def input_menu() :
    input_menu = 0
    global status
    i = 5
    while i > -1 :
        print(i)
        if(input_menu != 0):
            status = 0
            break

        input_menu = status # รอรับค่าหน้า page
        print(input_menu)
        i-=1
        time.sleep(1)
    return input_menu

def select_locker() :
    select_locker = 0
    global status
    i = 8
    while i > -1 :
        print(i)
        if(select_locker != 0):
            status = 0
            break

        select_locker = status # รอรับค่าหน้า page
        print(select_locker)
        i-=1
        time.sleep(1)
    return select_locker

def select_lock2():
    global status

    locker = status
    status = 0
    return locker
    
def input_update():
    input_update = 0
    global status
    i = 5
    while i > -1 :
        print(i)
        if(input_update != 0):
            status = 0
            break

        input_update = status # รอรับค่าหน้า page
        print(input_update)
        i-=1
        time.sleep(1)
    return input_update
    
