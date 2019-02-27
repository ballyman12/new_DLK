import time
import pymysql
import random
import locker_sping
import Open_Locker1
import Open_Locker2
import TurnOn_Locker
import paho.mqtt.client as mqtt
import time_admin
import time_user

host = "broker.mqttdashboard.com"
port = 8000


def open_locker(RFID_user,User) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    #RFID_user = input("ลงชื่อ : ") ##scan  ควรอยู่ input แรก 


    print("เลือกตู้")

    select_locker = 3#int(time_admin.select_locker())

    if(select_locker == 0) :

        Web = "555555"
    
        client = mqtt.Client()
        client.connect(host)
        ret = client.publish("DLK/4",Web)
        print(ret)
        
        
            
        
    else :

        select_user = input("User : ")

        sql_check = "SELECT * FROM details WHERE DLK_RFID = '%s' and DLK_Number_Locker = '%d' and DLK_Id_Result = 1 " %(select_user , select_locker)
        cursor.execute(sql_check)
        check_user = cursor.fetchone()
        

        if(check_user) :         
            print("ปลดล็อคตู้")          
            
            locker_open = int(input(":: ")) #time_user.check_time()#int(input("เลือก : "))  ########function เวลา
            
            if(locker_open == 1) :
                print("ตู้เปิด")
                Web = "555555"
    
                client = mqtt.Client()
                client.connect(host)
                ret = client.publish("DLK/4",Web)
                check_status = 0 ######
                ## insert log ประตูเปิด
                mass_open = log_status_door.open_door(User,RFID_user,check_user[3])
                print('%s , %s ' %(topic,mass_open))
                
                ##update locker ประตูเปิด

                update_status_locker.update_locker_open(check_user[3])

                while locker_open == 1 :
                    #sleep 30 s
                    check_items = int(input("Weight : "))
                    #close ?
                    locker_open = int(input("ปิดประตูไหม ? ปิด 0 / เปิด 1"))
                    #print("55")
                if (check_items > 0) :

                    #มีของ

                    print("555")

                else :

                    print("555")

                
                    

            else:
                print("ตู้ปิด")
                Web = "555555"
    
                client = mqtt.Client()
                client.connect(host)
                ret = client.publish("DLK/4",Web)

                
        else :
            print("ตู้ปิด 2")
            Web = "6666"

            client = mqtt.Client()
            client.connect(host)
            ret = client.publish("DLK/4",Web)
        
    # disconnect from server
    db.close()

open_locker(5,6)
