import tkinter as t
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def delete_user(new_window,root):
    try:
        connection=connect()
        c1=connection.cursor()
        query = 'call delete_user(%s)'
        c1.execute(query,(userid.userid,))
        connection.commit()
        messagebox.showinfo(title="success",message="Deleted")
        new_window.destroy()
        root.deiconify()
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))
