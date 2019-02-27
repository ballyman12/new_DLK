import paho.mqtt.client as mqtt
import time
import pymysql
import log_status_door
import update_status_locker
import log_detail_locker
import time_user
import time_admin


host = "broker.mqttdashboard.com"
port = 8000


location = 1
site = 1
locker_main = 1

mqtt_u = "intninlab_pub"
mqtt_p = "intninlab_pub.."


topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)

def open_locker(RFID_user,User) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    

    print("เลือกตู้")
    select_locker = int(time_admin.select_locker()) #int(input("เลือกตู้ : "))  ## รับสแกนจาก RFID

    if (select_locker) == 0 :
        select_locker = 0
        
        
        
    else :

        ##Publish scan

        select_user = input("ผู้ใช้งานตู้ : ") ## รับสแกนจาก RFID

        sql_select_detail = "select * from details where DLK_RFID = '%s' and DLK_Number_Locker = '%s' and DLK_Id_Result = 1 " %(select_user , select_locker)
        cursor.execute(sql_select_detail)
        select_detail = cursor.fetchone()
        ##print(select_detail[3])

        if(select_detail) :

            print("ตู้ปลดล็อค")

            locker_open = time_user.check_time()#int(input("เปิดตู้ไหม ? (ปิด 0) , (เปิด 1) : ")) ## Megnetic door Switch

            if(locker_open==1) :

                Web = "web|openLocker|"+str(select_locker)+"|admin|"

                client = mqtt.Client()
                client.connect(host)
                client.publish("DLK/10",Web)

                check_status = 0  #######

                ## insert log ประตูเปิด

                mass_open = log_status_door.open_door(User,RFID_user,select_detail[3])
            
                print('%s , %s ' %(topic,mass_open))

                ##update locker ประตูเปิด

                update_status_locker.update_locker_open(select_detail[3])

                

                while locker_open == 1 :
                ## time.sleep(30)

                    check_item = int(input("น้ำหนักของ : ")) ##load cell check

                ## ถามว่าปิดตู้ไหม ?

                    locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch

                if(check_item > 0) :

                    ## มีของ

                    Web = "web|"+str(select_locker)+"|0|"+"admin|"

                    client = mqtt.Client()
                    client.connect(host)
                    client.publish("DLK/10",Web)

                    ## insert log ประตูปิด

                    mass_close = log_status_door.close_door(User,RFID_user,select_detail[3])
            
                    print('%s , %s ' %(topic,mass_close))

                    # update detail by admin

                    mass_conti = log_detail_locker.update_by_admin_start(select_detail[0] , select_detail[2])

                    print('%s , %s ' %(topic,mass_conti))

                    ## insert log ประตูใช้งาน

                    mass_busy = log_status_door.busy_locker(User,RFID_user,select_detail[3])

                    print('%s , %s ' %(topic,mass_busy))

                    ## update status ตู้ไม่ว่าง

                    update_status_locker.update_locker_busy(select_detail[3])               

                    check_status = 1  #######

                    #publish เสร็จเพื่อเปลี่ยนหน้า

                    

                else :

                    check_status = 0  #######

                    Web = "web|"+str(select_locker)+"|0|"+"admin|"

                    client = mqtt.Client()
                    client.connect(host)
                    client.publish("DLK/10",Web)

                    ## ไม่มีของ

                    ## insert log ประตูปิด

                    mass_close = log_status_door.close_door(User,RFID_user,select_detail[3])
                
                    print('%s , %s ' %(topic,mass_close))

                    # update detail by admin

                    mass_end = log_detail_locker.update_by_admin_end(select_detail[0] , select_detail[2])

                    print('%s , %s ' %(topic,mass_end))

                    ##update locker ว้่าง

                    update_status_locker.update_locker_empty(select_detail[3])

                    ## insert log ประตูว่างพร้อมใช้งาน

                    mass_empty = log_status_door.empty_locker(User,RFID_user,select_detail[3])
                
                    print('%s , %s ' %(topic,mass_empty))

                    check_status = 1  #######

                    #publish เสร็จเพื่อเปลี่ยนหน้า

                    
                    
            else :

                print("ตู้ไม่เปิด")

                #publish เสร็จเพื่อเปลี่ยนหน้า

                Web = "web|"+str(select_locker)+"|0|"+"admin|"

                client = mqtt.Client()
                client.connect(host)
                client.publish("DLK/10",Web)
                
                check_status = 1  #######

        else :
            print("เงื่อนไขไม่ตรงกันกรุณาลองอีกครั้ง")

            Web = "web|"+str(select_locker)+"|15|"+"admin|"
            client = mqtt.Client()
            client.connect(host)
            client.publish("DLK/10",Web)
            

    
            
    # disconnect from server
    db.close()

    
