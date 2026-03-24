import tkinter as t
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def performance_chart():
    new_window=t.Toplevel()
    new_window.title('Performace chart')
    new_window.geometry("500x500")
    try:
        connection=connect()
        c1=connection.cursor()
        c1.execute('call select_fav_chart()',)
        ans=c1.fetchall()
        k=t.Text(new_window,width=60)
        k.pack()
        for a in ans:
            g="Performer: "+str(a['full_name'])+" Count: "+str(a['fav'])+"\n"
            k.insert(t.END,g)
        connection.commit()
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))