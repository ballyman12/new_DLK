import time
import pymysql
import datetime

def update_locker_open(locker):
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    ##update locker

    sql_update_locker = "Update lockers set DLK_status_Locker = 2 where DLK_Number_Locker = '%d' " %locker ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
    try:
       # Execute the SQL command
       cursor.execute(sql_update_locker)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

def update_locker_close(locker):
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    ##update locker

    sql_update_locker = "Update lockers set DLK_status_Locker = 1 where DLK_Number_Locker = '%d' " %locker ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
    try:
       # Execute the SQL command
       cursor.execute(sql_update_locker)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

def update_locker_busy(locker):
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_update_locker = "Update lockers set DLK_status_Locker = 4 where DLK_Number_Locker = '%d' " %locker ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
    try:
       # Execute the SQL command
       cursor.execute(sql_update_locker)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

def update_locker_empty(locker):
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_update_locker = "Update lockers set DLK_status_Locker = 3 where DLK_Number_Locker = '%d' " %locker ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
    try:
       # Execute the SQL command
       cursor.execute(sql_update_locker)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

def update_locker_disable(locker):
    # Open database connection
    db = pymysql.connect("localhost","pi","1234","locker" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql_update_locker = "Update lockers set DLK_status_Locker = 5 where DLK_Number_Locker = '%d' " %locker ## เหลือเปลี่ยนสถานะ ล็อคเกอร์
    try:
       # Execute the SQL command
       cursor.execute(sql_update_locker)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
