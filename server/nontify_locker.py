import time
import pymysql
import datetime
import random
import string
import paho.mqtt.client as mqtt
import search_data
import insert_log_server
import line_notify_BC

host = "broker.mqttdashboard.com"
port = 8000

def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe("DLK/#")

def on_message(client, userdata,msg):
    #print(msg.payload.decode("utf-8", "strict"))

    mass = msg.payload.decode("utf-8", "strict")

    topic = msg.topic

    token = "z2WsddL9iRFLmy4BAQhJTHjIwvqZVuYLpDwwGHU8ef5"

    token_user = "dwGfp5pFMKcbU7WSqU3U1UQzudSpp62STbftYvBtl92"

    print(topic)

    topic_split = topic.split("/")

    msg = topic_split[0]
    location = topic_split[1]
    site = topic_split[2]
    locker_name_id =topic_split[3]

    print(msg)
    print(location)
    print(site)
    print(locker_name_id)

    location_name = search_data.location_name(location)
    print(location_name)
    site_name = search_data.site_name(site)
    print(site_name)
    locker_name = search_data.locker_name(locker_name_id)
    print(locker_name)

    #print(location_name)
    #print(site_name)
    #print(locker_name)

    print(mass)
    
    mass_split = mass.split("|")
    
    check_mass = mass_split[0]
    #user_id = mass_split[1]
    #rfid = mass_split[2]
    #locker = mass_split[3] # หา locker_id
    #status = mass_split[4]
    #first_time = mass_split[5]
    #last_time = mass_split[6]
    #id_detail = mass_split[7]
    #detail_ref = mass_split[8]
    #condi = mass_split[9]

    print(check_mass)
 
    

    if check_mass == "log" :
        print("log")
        user_id = mass_split[1]
        rfid = mass_split[2]
        locker = mass_split[3] # หา locker_id
        status = mass_split[4]
        first_time = mass_split[5]
        
        #locker_id = search_data.search_locker_id(location,site,locker)
        user_name = search_data.search_name(user_id)
        #rfid_id = search_data.search_rfid(rfid)
        print(user_name)

    
        status_name = search_data.status_name(status) 
        print(status_name)
        
        #insert_log = insert_log_server.insert_log(rfid_id,location,site,locker_name_id,locker,status,first_time,mass)
        mass_line = "Location : %s , Site : %s , Locker : %s , User : %s , RFID : %s , Status : %s , time : %s" %(location_name,site_name,locker_name,user_name,rfid,status_name,first_time)
        print(mass_line)
        #line = line_notify_BC.line_notify(token,mass_line)
    elif check_mass == "Detail" :
        
        print("Detail")
        user_id = mass_split[1]
        rfid = mass_split[2]
        locker = mass_split[3] # หา locker_id
        status = mass_split[4]
        first_time = mass_split[5]
        last_time = mass_split[6]
        id_detail = mass_split[7]
        detail_ref = mass_split[8]
        condi = mass_split[9]

        #locker_id = search_data.search_locker_id(location,site,locker)
        user_name = search_data.search_name(user_id)
        #rfid_id = search_data.search_rfid(rfid)
        print(user_name)

    
        status_name = search_data.status_name(status) 
        print(status_name)

        mass_line = "\
                    Location : %s \
                    Site : %s \
                    Locker : %s  \
                    User : %s \
                    RFID : %s  \
                    Status : %s ,, Time : %s \
                    Referencr Id : %s" \
                    %(location_name,site_name,locker_name,user_name,rfid,status_name,first_time,detail_ref)
        print(mass_line)
        line = line_notify_BC.line_notify(token_user,mass_line)

    
def sub_mqtt() :
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host)
    client.loop_forever()

sub_mqtt()
