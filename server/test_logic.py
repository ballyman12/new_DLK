import search_data
import pymysql

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
    
#res = search_data.location_name(1)
res = locker_name(1)
print(res)
