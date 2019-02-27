import time
import pymysql
import datetime
import random
import string
import paho.mqtt.client as mqtt
import log_status_door
import update_status_locker
import log_detail_locker
import time_user

host = "broker.mqttdashboard.com"
port = 8000


location = 1
site = 1
locker_main = 1

mqtt_u = "intninlab_pub"
mqtt_p = "intninlab_pub.."


topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)



def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def gennarate():
    
    gennarate = random.randint(1,3)

    if gennarate ==1 :
        ran = randomStringDigits(6)
    elif gennarate == 2 :
        ran = randomStringDigits(8)
    else :
        ran = randomStringDigits(10)

    return ran
    

def deposit_item(RFID_user,Id_User) :

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_locker = "select DLK_Number_Locker from lockers where DLK_status_Locker = 3 "
    cursor.execute(sql_select_locker)
    select_locker = cursor.fetchall()
    #print(select_locker)
    loc_ker = []
    for row in select_locker:
      locker = row[0]
      # Now print fetched result
      #print ("locker = %d" %(locker))
      loc_ker.append(row[0])
    #print(loc_ker)
    locker = random.choice(loc_ker)
    print("ตู้ที่ : %d" %locker)

    ran = gennarate()

    #print(ran)

    #Publish ฝากใหม่
    
    Web = "web|"+str(locker)+"|0|"+"user|"
    
    client = mqtt.Client()
    client.connect(host)
    client.publish("DLK/2",Web)

    #mass_scan = log_status_door.scan_locker(Id_User,RFID_user,locker)
    
    ##check_cancel = int(input("ยกเลิกไหม ? (1) หรือ ไม่ยกเลิก (0) >>> : "))

    ##if(check_cancel == 0) :

    locker_open = time_user.check_time() # รับค่าจาก เมเนติก เวลา
    print(locker_open)

    if(locker_open==1) :

        check_status = 0  #######

        ## insert log ประตูเปิด

        #log_status_door.open_door(Id_User,RFID_user,locker)

        mass_open = log_status_door.open_door(Id_User,RFID_user,locker)

        print('%s , %s ' %(topic,mass_open))
        #client = mqtt.Client()
        #client.connect(host)
        #client.publish(topic,mass_open)


        #update status open

        update_status_locker.update_locker_open(locker)

        print("ตู้เปิด")
        print("")
        print("กรุณาฝากสัมภาระ")
        i = 1
        # sleep
        while i<3 :
            item = int(input("น้ำหนักสัมภาระ :> "))  ## load cell
            if(item>0) :
                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch function
                print("")
                if locker_open == 1 :
                    # ไฟล์เสียง
                    # Publish ตู้เปิด
                    Web = "web|"+str(locker)+"|3|"+"user|"
    
                    client = mqtt.Client()
                    client.connect(host)
                    client.publish("DLK/2",Web)
    
                    print("คุณยังไม่ได้ปิดตู้")
                    print("")
                    print("กรุณาปิดตู้ค่ะ")
                    i=i+1
                else :
                    print("ตู้ปิด")

                    ## insert log ประตูปิด

                    #log_status_door.close_door(Id_User,RFID_user,locker)

                    mass_close = log_status_door.close_door(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)

                    print('%s , %s ' %(topic,mass_close))


                    # insert detail เริ่มใช้งาน

                    mass_start = log_detail_locker.insert_detail_start(Id_User,RFID_user,locker,ran)

                    print('%s , %s ' %(topic,mass_start))

                    #update status busy

                    update_status_locker.update_locker_busy(locker)


                   ## insert log ตู้ไม่ว่าง

                    #log_status_door.busy_locker(Id_User,RFID_user,locker)

                    mass_busy = log_status_door.busy_locker(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)

                    print("%s , %s " %(topic,mass_busy))
                    #client = mqtt.Client()
                    #client.connect(host)
                    #client.publish(topic,mass_busy)


                    
                    # Publish ขอบคุณ

                    Web = "web|"+str(locker)+"|1|"+"user|"
    
                    client = mqtt.Client()
                    client.connect(host)
                    client.publish("DLK/2",Web)




                    print("คุณได้ฝากสัมภาระเรียบร้อยแล้ว")
                    print("ขอบคุณที่ใช้บริการค่ะ")
                    print("")
                    break

                    check_status = 1 #######

            else :
                print("ไม่ได้ฝากของ")
                print("")
                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch function
                print("")
                if locker_open == 1 :
                     # ไฟล์เสียง
                    # Publish ตู้เปิด
                    Web = "web|"+str(locker)+"|3|"+"user|"
    
                    client = mqtt.Client()
                    client.connect(host)
                    client.publish("DLK/2",Web)
                    
                    print("คุณยังไม่ได้ปิดตู้")
                    print("")
                    print("กรุณาปิดตู้ค่ะ")
                    i=i+1
                else :

                    print("ตู้ปิด")

                    ## insert log ประตูปิด

                    #log_status_door.close_door(Id_User,RFID_user,locker)

                    mass_close = log_status_door.close_door(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)

                    print('%s , %s ' %(topic,mass_close))


                    #update status empty

                    update_status_locker.update_locker_empty(locker)


                   ## insert log ตู้ว่าง

                    #log_status_door.empty_locker(Id_User,RFID_user,locker)

                    mass_empty = log_status_door.empty_locker(Id_User,RFID_user,locker)

                    #mqtt_publish.mqtt_publish(mass)

                    print('%s , %s ' %(topic,mass_empty))

                    check_cancel = time_user.check_cancel() # รอรับค่า
                    print(check_cancel)
                    
                    if(check_cancel == 0) :

                        #insert detail สำเร็จ

                        mass_end = log_detail_locker.insert_detail_end(Id_User,RFID_user,locker)

                        print('%s , %s ' %(topic,mass_end))

                        
                        # Publish ไม่ฝาก

                        Web = "web|"+str(locker)+"|2|"+"user|"
    
                        client = mqtt.Client()
                        client.connect(host)
                        client.publish("DLK/2",Web)

                        print("คุณไม่ได้ฝากสัมภาระ")
                        print("ขอบคุณที่ใช้บริการค่ะ")
                        print("")
                        break

                        check_status = 1 #######
                    else :

                        #publish หน้ายกเลิก
                        sql_select_condi = "select * from conditions "
                        cursor.execute(sql_select_condi)
                        select_condi = cursor.fetchall()
                        #print(select_locker)

                        for row in select_condi:
                          num_con = row[0]
                          condi = row[1]
                          # Now print fetched result
                          print ("%d = %s" %(num_con , condi))


                        cancel = time_user.input_cancel()#int(input("ยกเลิกเพราะ ?  >>> : "))  ####### function เลือกต้องกำหนดเวลา

                        #insert detail ยกเลิก

                        mass_cancel = log_detail_locker.insert_detail_cancel(Id_User,RFID_user,locker,cancel)

                        print('%s , %s ' %(topic,mass_cancel))


                        #publish ขอบคุณ
                        #Web = "web|"+str(locker)+"|1|"+"user|"
    
                        #client = mqtt.Client()
                        #client.connect(host)
                        #client.publish("DLK/2",Web)
                        print("ขอบคุณที่ใช้บริการค่ะ")
                        print("")

                        break

                        check_status = 1 #######

        if i==3 and item > 0 :

            Web = "web|"+str(locker)+"|4|"+"user|"
    
            client = mqtt.Client()
            client.connect(host)
            client.publish("DLK/2",Web)

            check_status = 1 #######

            print("Report")#
            print("Report")#
            print("ไม่ปิดตู้แต่ฝากของอยู่")#

            #insert detail ไม่ปิดตู้แต่ฝากของอยู่

            mass_problem = log_detail_locker.insert_detail_problem5(Id_User,RFID_user,locker)

            print('%s , %s ' %(topic,mass_problem))


            #report ผ่านทางโทรศัพท์มือถือ,ไลน์, email

        elif i==5 and item == 0 :

            check_status = 1 #######

            Web = "web|"+str(locker)+"|4|"+"user|"
    
            client = mqtt.Client()
            client.connect(host)
            client.publish("DLK/2",Web)

            print("ไม่ปิดตู้ไม่ฝากของ")#

            #insert detail ไม่ปิดตู้ไม่ฝากของ

            print("")

            mass_problem = log_detail_locker.insert_detail_problem6(Id_User,RFID_user,locker)

            print('%s , %s ' %(topic,mass_problem))



            #report ผ่านทางโทรศัพท์มือถือ,ไลน์, email




    elif(locker_open==0) :
        print("ตู้ปิด")
        print("คุณไม่ได้ทำการเปิดตู้")

        #insert detail สำเร็จ

        mass_end = log_detail_locker.insert_detail_end(Id_User,RFID_user,locker)

        print('%s , %s ' %(topic,mass_end))

        Web = "web|"+str(locker)+"|2|"+"user|"
    
        client = mqtt.Client()
        client.connect(host)
        client.publish("DLK/2",Web)

        print("ไม่ได้ฝากสัมภาระ")
        print("ขอบคุณที่ใช้บริการค่ะ")

        check_status = 1 #######



    # disconnect from server
    db.close()
