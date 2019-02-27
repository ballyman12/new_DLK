
from threading import Thread
import time
import Admin
import deposit
import paho.mqtt.client as mqtt
import pymysql
import time_user
import time_admin

host = "broker.mqttdashboard.com"
port = 8000

location = 1
site = 1
locker_main = 1

topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)



def input_user() :

    
    

    while True :

            
            
            RFID_user = (input("ลงชื่อ : ")) ##scan  ควรอยู่ input แรก
            Admin.main_using(RFID_user)
            time.sleep(5)


def check_locker() :
    
    global check_status  ## 1 = ไม่มีคนใช้งาน
    global locker_open

    if(check_status == 1):
        print("เช็คตู้ 1-9")  ## Menetic Sensor
    else :
        print("Waiting Process")
        
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def publish_log_status():

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    while True :
        # Open database connection
        db = pymysql.connect("localhost","root","","locker" )

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
                        print("In wait loop")
                        time.sleep(1)
                    print("in Main Loop")
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
                    print("connection failed")
                    client.loop_stop()    #Stop loop 
                    client.disconnect() # disconnect
                

        else :

            print("wait MQTT Status")
            time.sleep(3)

    # disconnect from server
    db.close()

        
def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe("DLK/#")

def on_message(client, userdata,msg):
    #print(msg.payload.decode("utf-8", "strict"))

    mass = msg.payload.decode("utf-8", "strict")

    print(mass)
    
    array = mass.split("|")
    
    check_mass = array[0]
    locker = array[1]
    status = array[2]
    posit = array[3]

    #print(status)

    if check_mass == "web" :
        if posit == "user":
            if status == "500" :
                #print(status)
                time_user.check_mqtt(status)
            elif locker == "cancel" :
                time_user.check_mqtt(status)
        elif posit == "admin" :
            if locker =="status" :
                if status == "1000" :
                    time_admin.check_mqtt(status)
            elif locker == "menu" :
                time_admin.check_mqtt(status)
            elif locker == "Open1":
                time_admin.check_mqtt(status)
            elif locker == "Open2" :
                time_admin.check_mqtt(status)
            elif locker == "Open3" :
                time_admin.check_mqtt(status)
        elif posit == "adminss" :
            time_admin.check_mqtt(status)
    
def sub_mqtt() :
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host)
    client.loop_forever()
        

thread1 = Thread(target=input_user)
#thread2 = Thread(target=publish_log_status)
thread3 = Thread(target=sub_mqtt)
thread1.start()
#thread2.start()
thread3.start()
