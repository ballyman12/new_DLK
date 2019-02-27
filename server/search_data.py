import time
import pymysql
import datetime
import random
import string



def search_locker_id(location , site , locker) :
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_locker = "select DLK_Id_Locker from lockers where Location_Id = '%s' and Site_Id = '%s' and DLK_Number_Locker = '%s' " %(location,site,locker)
    cursor.execute(sql_select_locker)
    select_locker = cursor.fetchone()

    return select_locker[0]

    db.close()

def search_name(id_user) :
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_name = "select DLK_Name_User from users where DLK_Id_User = '%s' " %(id_user)
    cursor.execute(sql_select_name)
    select_name = cursor.fetchone()

    return select_name[0]

    db.close()

def search_rfid(rfid):
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_rfid = "select DLK_Id_RFID from rfid where DLK_RFID = '%s' " %(rfid)
    cursor.execute(sql_select_rfid)
    select_rfid = cursor.fetchone()

    return select_rfid[0]

    db.close()

def location_name(location_id) :
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_name = "select Location_Name from location where Location_Id = '%s' " %(location_id)
    cursor.execute(sql_select_name)
    select_location = cursor.fetchone()

    return select_location[0]

    db.close()

def site_name(site_id) :
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_name = "select Site from site where Site_Id = '%s' " %(site_id)
    cursor.execute(sql_select_name)
    select_site = cursor.fetchone()

    return select_site[0]

    db.close()

def locker_name(locker_name) :
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_name = "select Name_Locker from locker_name where DLK_Name_Locker = '%s' " %(locker_name)
    cursor.execute(sql_select_name)
    select_Locker = cursor.fetchone()

    return select_Locker[0]

    db.close()

def status_name(status) :
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_select_name = "select DLK_Status_Name from locker_status where DLK_Status_Id = '%s' " %(status)
    cursor.execute(sql_select_name)
    select_status = cursor.fetchone()

    return select_status[0]

    db.close()
    

#num = search_locker_id(1 , 1 , 2)
#num = search_name(1)
#print(num)
