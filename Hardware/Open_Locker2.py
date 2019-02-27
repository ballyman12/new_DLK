import time
import pymysql
import log_status_door
import update_status_locker
import log_detail_locker
import time_user
import time_admin
import paho.mqtt.client as mqtt

host = "broker.mqttdashboard.com"
port = 8000


location = 1
site = 1
locker_main = 1

mqtt_u = "intninlab_pub"
mqtt_p = "intninlab_pub.."


topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)

def on_publish(client,userdata,result):             
    print("data published \n")
    pass


def open_locker_admin(RFID_user,User) :

    global check_status
    
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()



    select_locker = int(time_admin.select_locker()) #int(input("เลือกตู้ : "))

    ## นำตู้ที่เลือกไป เช็ค ใน details ว่ามีผู้ใช้หรือไหม ? ถ้าไม่มี ก็ไม่ต้องอัพเดทค่า
    ## ถ้ามีก็เปลี่ยนสถานะตู้ผู้นั้นเมื่อกระทำการใด ๆ

    sql_select_detail = "select * from details where DLK_Number_Locker = '%s' and DLK_Id_Result = 1 " %select_locker
    cursor.execute(sql_select_detail)
    select_detail = cursor.fetchone()
    #print(select_detail[3])

    if(select_detail) :

        #เสียง ตู้ปลดล็อค

        print("ตู้ปลดล็อค")

        locker_open = int(time_user.check_time()) #int(input("เปิดตู้ไหม ? (ปิด 0) , (เปิด 1) : ")) ## Megnetic door Switch

        if(locker_open==1) :

            print("ประตูเปิด")

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

                ## insert log ประตูปิด

                Web = "web|"+str(select_locker)+"|0|"+"admin|"

                print(Web)
    
                client = mqtt.Client()
                client.connect(host)
                client.publish("DLK/2",Web)
                
                mass_close = log_status_door.close_door(User,RFID_user,select_detail[3])

                print('%s , %s ' %(topic,mass_close))

                # update detail by admin

                mass_conti = log_detail_locker.update_by_admin_start(select_detail[0] , select_detail[2])

                print('%s , %s ' %(topic,mass_conti))


                ## update status ตู้ไม่ว่าง

                update_status_locker.update_locker_busy(select_detail[3])

                ## insert log ตู้ใช้งาน

                mass_busy = log_status_door.busy_locker(User,RFID_user,select_detail[3])

                print('%s , %s ' %(topic,mass_busy))
                   

                check_status = 1  #######

                #publish เสร็จเพื่อเปลี่ยนหน้า

                

            else :

                ## ไม่มีของ

                ## insert log ประตูปิด

                Web = "web|"+str(select_locker)+"|0|"+"admin|"

                print(Web)
    
                client = mqtt.Client()
                client.connect(host)
                client.publish("DLK/2",Web)
                
                mass_close = log_status_door.close_door(User,RFID_user,select_detail[3])
            
                print('%s , %s ' %(topic,mass_close))

                ##update locker ว้่าง

                update_status_locker.update_locker_empty(select_detail[3])

                ## insert log ประตูพร้อมใช้งาน

                

                ## insert log ประตูว่างพร้อมใช้งาน

                mass_empty = log_status_door.empty_locker(User,RFID_user,select_detail[3])
            
                print('%s , %s ' %(topic,mass_empty))

                # update detail by admin

                log_detail_locker.update_by_admin_end(select_detail[0] , select_detail[2])


                check_status = 1  #######

                #publish เสร็จเพื่อเปลี่ยนหน้า

                

        else :

            Web = "web|"+str(select_locker)+"|0|"+"admin|"

            
            client= mqtt.Client("control1")                           
            client.on_publish = on_publish                          
            client.connect(host,port)                                 
            ret= client.publish("DLK/2",Web)
            print(ret)

            print("ไม่ได้เปิดตู้ค่ะ 555")

            check_status = 1  #######

            #publish เสร็จเพื่อเปลี่ยนหน้า

            


        

        
    else :

        print("ตู้ปลดล็อค")

        locker_open = time_user.check_time() #int(input("เปิดตู้ไหม ? (ปิด 0) , (เปิด 1) : ")) ## Megnetic door Switch

        if(locker_open==1) :

            print("ประตูเปิด")

            Web = "web|openLocker|"+str(select_locker)+"|admin|"

            client = mqtt.Client()
            client.connect(host)
            client.publish("DLK/10",Web)

            check_status = 0  #######

            ## insert log ประตูเปิด

            mass_open = log_status_door.open_door(User,RFID_user,select_locker)
        
            print('%s , %s ' %(topic,mass_open))

            ##update locker ประตูเปิด

            update_status_locker.update_locker_open(select_locker)

            
            while locker_open == 1 :
                ## time.sleep(30)

                ## ถามว่าปิดตู้ไหม ?

                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch

            ## insert log ประตูปิด

            #publish เสร็จเพื่อเปลี่ยนหน้า

            Web = "web|"+str(select_locker)+"|0|"+"admin|"

            print(Web)

            client = mqtt.Client()
            client.connect(host)
            client.publish("DLK/2",Web)

            mass_close = log_status_door.close_door(User,RFID_user,select_locker)
            
            print('%s , %s ' %(topic,mass_close))

            ##update locker ว้่าง

            update_status_locker.update_locker_empty(select_locker)   

            ## insert log ประตูว่างพร้อมใช้งาน

            mass_empty = log_status_door.empty_locker(User,RFID_user,select_locker)
        
            print('%s , %s ' %(topic,mass_empty))
            

            check_status = 1  #######

            
            
        else :
            Web = "web|"+str(select_locker)+"|0|"+"admin|"

            print(Web)

            client = mqtt.Client()
            client.connect(host)
            client.publish("DLK/2",Web)
            
            print("ไม่ได้เปิดตู้ค่ะ")

            check_status = 1  #######

            #publish เสร็จเพื่อเปลี่ยนหน้า

            

    # disconnect from server
    db.close()
