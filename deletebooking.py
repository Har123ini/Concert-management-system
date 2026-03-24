import tkinter as t
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def delete_ticket():
    new_window=t.Toplevel()
    new_window.title('Delete booking')
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
        t.Label(new_window,text="Booking id").pack()
        Booking_id=t.Entry(new_window)
        Booking_id.pack()
        connection.commit()
        def delete():
            try:
                connection=connect()
                c2=connection.cursor()
                if Booking_id.get().strip()=="":
                    messagebox.showerror(title="error",message="Bookind id should not be empty")
                    return
                else:
                    query = 'call delete_booking(%s,%s)'
                    c2.execute(query,(Booking_id.get().strip(),userid.userid))
                    connection.commit()
                    messagebox.showinfo(title="success",message="Deleted Booking")
                    new_window.destroy()
            except pymysql.Error as e:
                messagebox.showerror(title="error",message=str(e))
        t.Button(new_window,text="Delete",command=delete).pack()
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))