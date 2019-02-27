import time
import pymysql
import log_status_door
import update_status_locker
import log_detail_locker
import paho.mqtt.client as mqtt
import time_admin

host = "broker.mqttdashboard.com"
port = 8000


location = 1
site = 1
locker_main = 1

mqtt_u = "intninlab_pub"
mqtt_p = "intninlab_pub.."


topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)

def turn_on_locker(RFID_user,User) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    print("เลือกตู้")
    select_locker = int(time_admin.select_locker()) #int(input("เลือกตู้ : "))


    if(select_locker == 0):

        print("ไม่มีการทำงาน")

    

    #else :

    print("เลือก Menu")
    update = int(time_admin.input_update())#int(input("เปิดใช้งาน 1 / ระงับใช้งาน 0  :"))

    if(update == 1) :

        check_status = 0  #######

        ## insert log ประตูเปิดใช้งาน


        mass_empty = log_status_door.empty_locker(User,RFID_user,select_locker)

        print('%s , %s ' %(topic,mass_empty))

        print("เปิด")

        ##update locker ว้่าง

        update_status_locker.update_locker_empty(select_locker)

        check_status = 1  #######

      


    else :

        check_status = 0  #######

        ## insert log ประตูระงับใช้งาน

        print("ระงับ")

        mass_disable = log_status_door.disable_locker(User,RFID_user,select_locker)

        print('%s , %s ' %(topic,mass_disable))

        print("เปิด")

        ##update locker ว้่าง

        update_status_locker.update_locker_disable(select_locker)

        check_status = 1  #######

         
            
    #publish เสร็จสิ้นเปลั้ยนหน้า 

    # disconnect from server
    db.close()
