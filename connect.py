import pymysql
from tkinter import messagebox
def connect():
    try:
        connection= pymysql.connect(host='localhost',
                                         user='root',password='Harini@123',
                                         database='project_harini',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         autocommit=True)
        return connection
    except:
        return None
