import time
import pymysql
import random
import paho.mqtt.client as mqtt
import log_status_door
import update_status_locker
import log_detail_locker
import deposit
import time_user

host = "broker.mqttdashboard.com"
port = 8000

location = 1
site = 1
locker_main = 1

mqtt_u = "intninlab_pub"
mqtt_p = "intninlab_pub.."


topic = "DLK/"+str(location)+"/"+str(site)+"/"+str(locker_main)


global locker_open

def locker_main(RFID_user):

    global check_status

    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    #RFID_user = (input("ลงชื่อ : ")) ##scan  ควรอยู่ input แรก

    select_user = "SELECT * FROM access  WHERE DLK_RFID = '%s' and (CURRENT_TIME > DLK_RFID_Start and CURRENT_TIME < DLK_RFID_EXP )  " %(RFID_user)
    cursor.execute(select_user)
    user = cursor.fetchall()
    for row in user :
        Id_User = row[1]
        Start_Date = row[4]
        EXP_Date = row[5]




    if(user) :
            # Prepare SQL query to INSERT a record into the database.
            sql_check_blacklist = "SELECT * FROM blacklist where DLK_Id_User = '%d' " %(Id_User)



            # Execute the SQL command
            cursor.execute(sql_check_blacklist)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchone()
            # Now print fetched result
            #print (results)
            #print (name[1])
            if(results) :

                #publish ห้ามใช้งาน

                Web = "web|"+"Don't use|"+"10|"+"user|"
    
                client = mqtt.Client()
                client.connect(host)
                client.publish("DLK/3",Web)
                
                print ("ไม่สามารถใช้งานได้ค่ะ กรุณาติดต่อเจ้าหน้าที่")


            else :

                print ("ยินดีต้อนรับค่ะ")

                sql_check_item = "select * from details where DLK_RFID = '%s' and (DLK_Id_Result = 1 OR DLK_Id_Result = 5) " %(RFID_user)
                cursor.execute(sql_check_item)
                check_item = cursor.fetchone()

                if(check_item) :

                    #publish User มีของ #######################33

                    Web = "web|"+str(check_item[3])+"|6|"+"user|"
    
                    client = mqtt.Client()
                    client.connect(host)
                    client.publish("DLK/2",Web)
                    
                    print("ตู้ที่ %d" %check_item[3])
                    print("ฝากเพิ่ม / ถอน")

                    # update detail สแกนบัตรมาเอาของ

                    mass_conti = log_detail_locker.update_detail_start(check_item[0])

                    print('%s , %s ' %(topic,mass_conti))

                    locker_open = time_user.check_time() ## fuction time
                    print(locker_open)



                    if(locker_open==1) :

                        check_status = 0 #######

                        ## insert log ประตูเปิด


                        #log_status_door.open_door(Id_User,RFID_user,check_item[3])

                        mass_open = log_status_door.open_door(Id_User,RFID_user,check_item[3])

                        print('%s , %s ' %(topic,mass_open))
                        #client = mqtt.Client()
                        #client.connect(host)
                        #client.publish(topic,mass_open)



                        ##update locker open

                        update_status_locker.update_locker_open(check_item[3])

                        print("ตู้เปิด")
                        print("")
                        i = 1
                        while i<3 :
                            item = int(input("น้ำหนักสัมภาระ :> "))  ## load cell
                            if(item>0) :
                                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch # fuction 
                                print("")
                                if locker_open == 1 :
                                    # ไฟล์เสียง
                                    # Publish ตู้เปิด
                                    Web = "web|"+str(check_item[3])+"|3|"+"user|"
    
                                    client = mqtt.Client()
                                    client.connect(host)
                                    client.publish("DLK/3",Web)
                                    print("คุณยังไม่ได้ปิดตู้")
                                    print("")

                                    i=i+1
                                else :
                                    print("ตู้ปิด")
                                    print("คุณได้ฝากสัมภาระเพิ่มเรียบร้อยแล้ว")



                                    ## insert log ประตูปิด

                                    #log_status_door.close_door(Id_User,RFID_user,check_item[3])

                                    mass_close = log_status_door.close_door(Id_User,RFID_user,check_item[3])

                                    print('%s , %s ' %(topic,mass_close))

                                    # update detail สแกนบัตรมาเอาของฝากเพิ่ม

                                    mass_conti = log_detail_locker.update_detail_start(check_item[0])

                                    print('%s , %s ' %(topic,mass_conti))

                                    ##update locker busy

                                    update_status_locker.update_locker_busy(check_item[3])

                                   ## insert log ตู้ไม่ว่าง

                                    #log_status_door.busy_locker_withd(Id_User,RFID_user,check_item[3])

                                    mass_busy = log_status_door.busy_locker(Id_User,RFID_user,check_item[3])

                                    print('%s , %s ' %(topic,mass_busy))

                                    # Publish ขอบคุณ
                                    Web = "web|"+str(check_item[3])+"|7|"+"user|"
    
                                    client = mqtt.Client()
                                    client.connect(host)
                                    client.publish("DLK/3",Web)

                                    print("ขอบคุณที่ใช้บริการค่ะ")
                                    print("")
                                    break
                                    check_status = 1 #######

                            else :
                                print("ถอนสัมภาระ")
                                print("")
                                locker_open = int(input("เปิดตู้ไหม ? : ")) ## Megnetic door Switch # fuction 
                                print("")
                                if locker_open == 1 :
                                    # ไฟล์เสียง
                                    # Publish ตู้เปิด
                                    Web = "web|"+str(check_item[3])+"|9|"+"user|"
    
                                    client = mqtt.Client()
                                    client.connect(host)
                                    client.publish("DLK/3",Web)
                                    print("คุณยังไม่ได้ปิดตู้")
                                    print("")
                                    print("กรุณาปิดตู้ด้วยค่ะ")
                                    i=i+1
                                else :
                                    print("คุณได้ถอนฝากสัมภาระเรียบร้อยแล้วคะ")



                                    ## insert log ประตูปิด

                                    #log_status_door.close_door(Id_User,RFID_user,check_item[3])

                                    mass_close = log_status_door.close_door(Id_User,RFID_user,check_item[3])

                                    print('%s , %s ' %(topic,mass_close))

                                    # update detail เอาของออก

                                    mass_end = log_detail_locker.update_detail_end(check_item[0])

                                    print('%s , %s ' %(topic,mass_end))

                                    ##update locker empty

                                    update_status_locker.update_locker_empty(check_item[3])

                                   ## insert log ตู้ว่าง

                                    #log_status_door.empty_locker(Id_User,RFID_user,check_item[3])

                                    mass_empty = log_status_door.empty_locker(Id_User,RFID_user,check_item[3])

                                    print('%s , %s ' %(topic,mass_empty))

                                    # Publish ขอบคุณ
                                    Web = "web|"+str(check_item[3])+"|8|"+"user|"
    
                                    client = mqtt.Client()
                                    client.connect(host)
                                    client.publish("DLK/3",Web)

                                    print("ขอบคุณที่ใช้บริการค่ะ")

                                    break

                                    check_status = 1 #######

                        if(i==3 and item>0 ) :
                            print("Report")#
                            print("ไม่ปิดตู้แต่ฝากของอยู่")#

                            Web = "web|"+str(check_item[3])+"|4|"+"user|"
    
                            client = mqtt.Client()
                            client.connect(host)
                            client.publish("DLK/2",Web)

                            # # update detail ไม่ปิดตู้แต่ฝากของอยู่

                            mass_problem5 = log_detail_locker.update_detail_problem5(check_item[0])

                            print('%s , %s ' %(topic,mass_problem5))

                            print("คุณไม่ได้ปิดตู้ล็อคเกอร์ค่ะ")


                            check_status = 1 #######



                            print("")
                        elif(i==3 and item == 0) :
                            print("Report")#
                            print("ไม่ปิดตู้แต่ถอนของแล้ว")#

                            Web = "web|"+str(check_item[3])+"|11|"+"user|"
    
                            client = mqtt.Client()
                            client.connect(host)
                            client.publish("DLK/2",Web)

                            # # update detail ไม่ปิดตู้แต่ถอนของแล้ว

                            mass_problem6 = log_detail_locker.update_detail_problem6(check_item[0])

                            print('%s , %s ' %(topic,mass_problem6))

                            check_status = 1 #######





                    else :
                        check_status = 1 #######
                        print("ตู้ปิด")
                        print("ไม่ได้ฝากสัมภาระเพิ่มค่ะ")

                        # update detail สแกนแต่ไม่เปิดตู้

                        mass_conti = log_detail_locker.update_detail_start(check_item[0])

                        print('%s , %s ' %(topic,mass_conti))

                        #publish ไม่ฝากสัมภาระเพิ่ม

                        Web = "web|"+str(check_item[3])+"|2|"+"user|"
    
                        client = mqtt.Client()
                        client.connect(host)
                        client.publish("DLK/3",Web)


                        print("")

                else :
                    sql_select_locker = "select DLK_Number_Locker from lockers where DLK_status_Locker = 3 "
                    cursor.execute(sql_select_locker)
                    select_locker = cursor.fetchall()
                    print("เริ่มฝาก")

                    if(select_locker):
                        deposit.deposit_item(RFID_user,Id_User)
                    else :
                        print("ตู้ล็อคเกอร์เต็มค่ะ")






    else :

        #publish ห้ามใช้งาน
        Web = "web|"+"EXP"+"|10|"+"user|"
    
        client = mqtt.Client()
        client.connect(host)
        client.publish("DLK/3",Web)

        print(Web)
        
        print("บัตรหมดอายุค่ะ กรุณาติดต่อเจ้าหน้าที่")

        check_status = 1 #######




    # disconnect from server
    db.close()
