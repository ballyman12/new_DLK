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


def main_using(RFID_user) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    #RFID_user = input("ลงชื่อ : ") ##scan  ควรอยู่ input แรก 

    sql_check_admin = "SELECT * FROM access WHERE DLK_RFID = '%s' and DLK_Position_User = 'admin' " %RFID_user
    cursor.execute(sql_check_admin)
    select_admin = cursor.fetchall()
    for row in select_admin :
        User = row[1]
        Start_Date = row[4]
        EXP_Date = row[5]
    ##print(User) ส่งค่า

    if(select_admin) :

        #print("5555")

        #Publish Admin

        Web = "web|"+str(User)+"|0|"+"admin|"
    
        client = mqtt.Client()
        client.connect(host)
        ret = client.publish("DLK/4",Web)
        print(ret)
        
        select_status = time_admin.check_admin() #int(input("เลือกสถานะ Admin (1) / User (0) : "))
        print(select_status)##เลือก สถานะก่อนใช้งานสำหรับ Admin function เวลา เกินเวลาให้ปรับเป็น user
        if(select_status == "1000") :
            #print("88888")
            #publish Menu Admin
            
            print("1. ปลดล็อคตู้")
            print("2. ปลดล็อคโดย Admin ผู้เดียว")
            print("3. ระงับการใช้งานของตู้")
            select_menu = time_admin.input_menu()#int(input("เลือก : "))  ########function เวลา
            if(select_menu == "1") :
                print("1. ปลดล็อคตู้")
                #punlish Admin 1
                Open_Locker1.open_locker(RFID_user,User)

            elif(select_menu == "2") :
                print("2. ปลดล็อคโดย Admin ผู้เดียว")
                #publish Admin 2
                Open_Locker2.open_locker_admin(RFID_user,User)

                
            elif (select_menu == "3") :
                #publish Admin 3
                print("3. ระงับการใช้งานของตู้")

                TurnOn_Locker.turn_on_locker(RFID_user,User)
                
            elif select_menu == 0 :

                print(" ไม่มีการทำงาน")
                
                
                    
                    

        elif select_status == 0 :
            locker_sping.locker_main(RFID_user)
            
        
    else :
        locker_sping.locker_main(RFID_user)
        
    # disconnect from server
    db.close()
