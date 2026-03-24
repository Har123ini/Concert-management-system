import tkinter as t
from tkinter import Listbox
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def book_ticket():
    new_window=t.Toplevel()
    new_window.title('Book Tickets')
    new_window.geometry("1000x500")
    try:
        connection=connect()
        c1=connection.cursor()
        listb=Listbox(new_window,width=200)
        listb.pack()
        c1.execute('call select_concert()')
        ans=c1.fetchall()
        list1=[]
        for a in ans:
            list1.append(a)
            g="Concert ID: "+str(a['concert_id'])+" Concert name: "+a['concert_name']+" Concert date: "+str(a['concert_date'])+" Venue_name: "+a['venue_name']+" start_time: "+str(a['start_time'])+" available_tickets: "+str(a['available_tickets'])+" performers "+str(a['performers'])
            listb.insert(t.END,g)
        t.Label(new_window,text="Number of Tickets").pack()
        num_ticekts=t.Entry(new_window)
        num_ticekts.pack()
        connection.commit()
        def book():
            select=listb.curselection()
            try:
                connection=connect()
                c2=connection.cursor()
                if not select:
                    messagebox.showerror(title="error",message="Please choose a concert to book")
                    return
                elif num_ticekts.get().strip()=="":
                    messagebox.showerror(title="error",message="Please enter number of tickets to book")
                    return
                else:
                    query = 'call add_booking(%s,%s,%s)'
                    c2.execute(query,(userid.userid,list1[select[0]]['concert_id'],int(num_ticekts.get().strip()),))
                    connection.commit()
                    messagebox.showinfo(title="success",message="Booked")
                    new_window.destroy()
            except pymysql.Error as e:
                messagebox.showerror(title="error",message=str(e))
        t.Button(new_window,text="Book",command=book).pack()
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))