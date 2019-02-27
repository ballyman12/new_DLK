import time
import pymysql
import datetime
import random

def insert_detail_start(Id_User,RFID_user,locker,ran):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql_insert = "INSERT INTO details(DLK_Id_User , \
                  DLK_RFID , DLK_Number_Locker, DLK_Ref , DLK_id_Result , MQTT_Status) \
                  VALUES ('%d', '%s', '%d', '%s' ,'%d' , '%d' )" % \
                  (Id_User,RFID_user,locker,ran , 1 , 0)
    try:
       # Execute the SQL command
       cursor.execute(sql_insert)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    sql_select = "SELECT DLK_Id_Detail FROM details ORDER BY DLK_Id_Detail DESC LIMIT 1"
    cursor.execute(sql_select)
    detail = cursor.fetchone()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_conti = "Detail|"+str(detail[0])+"|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|1|"+str(last_time)

    return mass_conti

def insert_detail_end(Id_User,RFID_user,locker):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql_insert = "INSERT INTO details(DLK_Id_User , \
       DLK_RFID,DLK_Number_Locker, DLK_id_Result, MQTT_Status) \
       VALUES ('%d', '%s', '%d', '%d' , '%d'  )" % \
       (Id_User,RFID_user, locker, 8 , 0 )
    try:
       # Execute the SQL command
       cursor.execute(sql_insert)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    sql_select = "SELECT DLK_Id_detail FROM details ORDER BY DLK_Id_Detail DESC LIMIT 1"
    cursor.execute(sql_select)
    detail = cursor.fetchone()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_end = "Detail|"+str(detail[0])+"|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|8|"+str(last_time)

    return mass_end

def insert_detail_cancel(Id_User , RFID_user , locker ,cancel):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql_insert = "INSERT INTO details(DLK_Id_User , \
        DLK_RFID , DLK_Number_Locker, DLK_id_Result , MQTT_Status ,DLK_Id_condi) \
        VALUES ('%d', '%s', '%d', '%d' , '%d' , '%s' )" % \
        (Id_User,RFID_user,locker, 7  , 0 , cancel)
    try:
       # Execute the SQL command
       cursor.execute(sql_insert)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    sql_select = "SELECT DLK_Id_Detail FROM details ORDER BY DLK_Id_Detail DESC LIMIT 1"
    cursor.execute(sql_select)
    detail = cursor.fetchone()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_cancel = "Detail|"+str(detail[0])+"|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|7|"+str(cancel)+"|"+str(last_time)

    return mass_cancel

def insert_detail_problem5(Id_User, RFID_user , locker):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql_insert = "INSERT INTO details(DLK_Id_User , \
       DLK_RFID , DLK_Number_Locker, DLK_id_Result , MQTT_Status) \
       VALUES ('%d', '%s', '%d', '%d', '%d')" % \
       (Id_User, RFID_user , locker, 5 , 0 )
    try:
       # Execute the SQL command
       cursor.execute(sql_insert)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    sql_select = "SELECT DLK_Id_Detail FROM details ORDER BY DLK_Id_Detail DESC LIMIT 1"
    cursor.execute(sql_select)
    detail = cursor.fetchone()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_problem = "Detail|"+str(detail[0])+"|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|5|"+str(last_time)

    return mass_problem



def insert_detail_problem6(Id_User, RFID_user , locker):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql_insert = "INSERT INTO details(DLK_Id_User , \
       DLK_RFID , DLK_Number_Locker, DLK_id_Result, MQTT_Status) \
       VALUES ('%d', '%s', '%d', '%d' , '%d' )" % \
       (Id_User, RFID_user , locker, 6 , 0 )
    try:
       # Execute the SQL command
       cursor.execute(sql_insert)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    sql_select = "SELECT DLK_Id_Detail FROM details ORDER BY DLK_Id_Detail DESC LIMIT 1"
    cursor.execute(sql_select)
    detail = cursor.fetchone()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_problem = "Detail|"+str(detail[0])+"|"+str(Id_User)+"|"+str(RFID_user)+"|"+str(locker)+"|5|"+str(last_time)

    return mass_problem

def update_detail_start(check_item):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , MQTT_Status = 0 \
                   WHERE details.DLK_Id_Detail = '%d' AND details.DLK_Id_result = 1 " \
                   %check_item
    try:
       # Execute the SQL command
       cursor.execute(sql_update)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_contin = "Detail|"+str(check_item)+"|1|"+str(last_time)

    return mass_contin

def update_detail_end(check_item):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , MQTT_Status = 0 , \
                   details.DLK_Id_result = 8 WHERE details.DLK_Id_Detail = '%d'  " \
                   %check_item
    try:
       # Execute the SQL command
       cursor.execute(sql_update)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_end = "Detail|"+str(check_item)+"|8|"+str(last_time)

    return mass_end

def update_detail_problem5(check_item):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , MQTT_Status = 0 , \
                   details.DLK_Id_result = 5 WHERE details.DLK_Id_Detail = '%d'  " \
                   %check_item
    try:
       # Execute the SQL command
       cursor.execute(sql_update)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_problem5 = "Detail|"+str(check_item)+"|5|"+str(last_time)

    return mass_problem5


    print("คุณไม่ได้ปิดตู้ล็อคเกอร์ค่ะ")


def update_detail_problem6(check_item):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , MQTT_Status = 0 , \
                   details.DLK_Id_result = 6 WHERE details.DLK_Id_Detail = '%d'  " \
                   %check_item
    try:
       # Execute the SQL command
       cursor.execute(sql_update)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_problem6 = "Detail|"+str(check_item)+"|6|"+str(last_time)

    return mass_problem6

    print("คุณไม่ได้ปิดตู้ล็อคเกอร์ค่ะ")

def update_by_admin_start(select_detail_0 , select_detail_2):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , details.DLK_Id_result = 1 , MQTT_Status = 0\
                   WHERE details.DLK_Id_Detail = '%d' AND details.DLK_RFID = '%s' " \
                   %(select_detail_0 , select_detail_2)
    try:
       # Execute the SQL command
       cursor.execute(sql_update)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_contin = "Detail|"+str(select_detail_0)+"|1|"+str(last_time)

    return mass_contin

def update_by_admin_end(select_detail_0 , select_detail_2):
     # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql_update = " UPDATE details SET DLK_Date_Curent = CURRENT_TIME() , details.DLK_Id_result = 8 , MQTT_Status = 0 \
                   WHERE details.DLK_Id_Detail = '%d' AND details.DLK_RFID = '%s' " \
                   %(select_detail_0 , select_detail_2)
    try:
       # Execute the SQL command
       cursor.execute(sql_update)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    last_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    mass_end = "Detail|"+str(select_detail_0)+"|8|"+str(last_time)

    return mass_end
