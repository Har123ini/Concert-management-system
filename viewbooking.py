import tkinter as t
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def view_ticket():
    new_window=t.Toplevel()
    new_window.title('View booking')
    new_window.geometry("500x500")
    try:
        connection=connect()
        c1=connection.cursor()
        c1.execute('call delete_select(%s)',userid.userid)
        ans=c1.fetchall()
        k=t.Text(new_window,width=100)
        k.pack()
        for a in ans:
            g="Booking ID: "+str(a['booking_id'])+" Seat count: "+str(a['seats_count'])+" Concert ID: "+str(a['concert_id'])+"\n"
            k.insert(t.END,g)
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))