import time
import pymysql
import datetime
import random
import string

def insert_log_server(rfid_id, location, site, locker_name, locker, status_locker, time, MQTT_Mass) :
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","serverlocker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    # Prepare SQL query to INSERT a record into the database.
    sql_insert_log = "INSERT INTO log_open(DLK_Id_RFID , \
       location_Id, Site_Id ,DLK_Name_Locker ,DLK_Number_Locker, DLK_Status_Locker , Time_open , MQTT_Mas) \
       VALUES ('%d', '%s', '%d', '%d', '%d' )" % \
       (rfid_id,location,site,locker_name,locker,status_locker,time,MQTT_Mass)
    try:
       # Execute the SQL command
       cursor.execute(sql_insert_log)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    db.close()
