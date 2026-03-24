import tkinter as t
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def update_ticket():
    new_window=t.Toplevel()
    new_window.title('Update booking')
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
        t.Label(new_window,text="Number of seats").pack()
        seats=t.Entry(new_window)
        seats.pack()
        connection.commit()
        def update():
            try:
                if Booking_id.get().strip()=="":
                    messagebox.showerror(title="error",message="booking id cannot be empty")
                    return
                elif seats.get().strip()=="":
                    messagebox.showerror(title="error",message="seats cannot be empty")
                    return
                else:
                    connection=connect()
                    c2=connection.cursor()
                    query = 'call update_booking(%s,%s,%s)'
                    c2.execute(query,(int(Booking_id.get().strip()),userid.userid,int(seats.get().strip())))
                    connection.commit()
                    messagebox.showinfo(title="success",message="Updated Booking")
                    new_window.destroy()
            except pymysql.Error as e:
                messagebox.showerror(title="error",message=str(e))
        t.Button(new_window,text="Update",command=update).pack()
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))