import pymysql
import paho.mqtt.client as mqtt
import time
from threading import Thread

host = "broker.mqttdashboard.com"
port = 8000


location = 1
site = 1
locker_main = 1

mqtt_u = "intninlab_pub"
mqtt_p = "intninlab_pub.."

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)


topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)

def pub_log():

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    while True :
        # Open database connection
        db = pymysql.connect("localhost","pi","1234","locker" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        
        sql_select_log = "SELECT * FROM log_status_locker WHERE MQTT_Status = 0"
        cursor.execute(sql_select_log)
        select_log = cursor.fetchall()

        #print(select_log)

        if(select_log) :
            for row in select_log :
                log_id = row[0]
                Id_User = row[1]
                RFID_user = row[2]
                locker = row[3]
                status_locker = row[4]
                last_time = row[5]
                mass = "log|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|"+str(status_locker)+"|"+str(last_time)

                print(mass)
                
                mqtt.Client.connected_flag=False#create flag in class
                client = mqtt.Client()             #create new instance 
                client.on_connect=on_connect  #bind call back function
                client.loop_start()
                print("Connecting to broker : ",host)
                try:
                    client.connect(host)      #connect to broker
                    while not client.connected_flag: #wait in loop
                        print("In wait loop Log Status")
                        time.sleep(1)
                    print("in Main Loop Log Status")
                    client.publish(topic,mass)
                    client.loop_stop()    #Stop loop 
                    client.disconnect() # disconnect

                    sql_update_log = "Update log_status_locker set MQTT_Status = 1 where log_id = '%d' " %log_id ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
                    try:
                       # Execute the SQL command
                       cursor.execute(sql_update_log)
                       # Commit your changes in the database
                       db.commit()
                    except:
                       # Rollback in case there is any error
                       db.rollback()
                    
                except:
                    print("connection failed Log Status")
                    client.loop_stop()    #Stop loop 
                    client.disconnect() # disconnect

                time.sleep(3)
                

        else :

            print("wait MQTT Log Status")
            time.sleep(3)

    # disconnect from server
    db.close()

def pub_detail():
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    while True :
        # Open database connection
        db = pymysql.connect("localhost","pi","1234","locker" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        
        sql_select_detail = "SELECT * FROM details WHERE MQTT_Status = 0"
        cursor.execute(sql_select_detail)
        select_detail = cursor.fetchall()

        #print(select_log)

        if(select_detail) :
            for row in select_detail :
                detail_id = row[0]
                Id_User = row[1]
                RFID_user = row[2]
                locker = row[3]
                status_detail = row[4]
                detail_ref = row[5]
                condi = row[6]
                first_time = row[7]
                last_time = row[8]
                mass = "Detail|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|"+str(status_detail)+"|"+str(first_time)+"|"+str(last_time)+"|"+str(detail_id)+"|"+str(detail_ref)+"|"+str(condi)

                print(mass)
                
                mqtt.Client.connected_flag=False#create flag in class
                client = mqtt.Client()             #create new instance 
                client.on_connect=on_connect  #bind call back function
                client.loop_start()
                print("Connecting to broker : ",host)
                try:
                    client.connect(host)      #connect to broker
                    while not client.connected_flag: #wait in loop
                        print("In wait loop Detail")
                        time.sleep(1)
                    print("in Main Loop Detail")
                    client.publish(topic,mass)
                    client.loop_stop()    #Stop loop 
                    client.disconnect() # disconnect

                    sql_update_log = "Update details set MQTT_Status = 1 where DLK_Id_Detail = '%d' " %detail_id ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
                    try:
                       # Execute the SQL command
                       cursor.execute(sql_update_log)
                       # Commit your changes in the database
                       db.commit()
                    except:
                       # Rollback in case there is any error
                       db.rollback()
                    
                except:
                    print("connection failed Detail")
                    client.loop_stop()    #Stop loop 
                    client.disconnect() # disconnect
                
                time.sleep(3)
        else :

            print("wait MQTT Status Detail")
            time.sleep(3)
    


thread1 = Thread(target=pub_log)
thread2 = Thread(target=pub_detail)
thread1.start()
thread2.start()
