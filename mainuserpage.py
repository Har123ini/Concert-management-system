import tkinter as t
from tkinter import messagebox
import pymysql
from connect import connect
import userid
from deleteuser import delete_user
from bookticket import book_ticket
from updateuser import update_user
from deletebooking import delete_ticket
from updatebooking import update_ticket
from favourite_add import favourite_performer
from deletefavourite import delete_favourite_performer
from performerschart import performance_chart
from viewbooking import view_ticket
def mainuser(root):
    new_window=t.Toplevel()
    new_window.title('Concert Page')
    new_window.geometry("500x500")
    button1 =t.Button(new_window,text="Delete User",width=16,command=lambda:delete_user(new_window,root))
    button1.pack()
    button4 =t.Button(new_window,text="Update User",width=16,command=update_user)
    button4.pack()
    button2 =t.Button(new_window,text="Book Ticket",width=16,command=book_ticket)
    button2.pack()
    button10 =t.Button(new_window,text="View Booking",width=16,command=view_ticket)
    button10.pack()
    button3 =t.Button(new_window,text="Delete booking",width=16,command=delete_ticket)
    button3.pack()
    button6 =t.Button(new_window,text="Update booking",width=16,command=update_ticket)
    button6.pack()
    button7 =t.Button(new_window,text="Add Favourite",width=16,command=favourite_performer)
    button7.pack()
    button8 =t.Button(new_window,text="Delete Favourite",width=16,command=delete_favourite_performer)
    button8.pack()
    button9 =t.Button(new_window,text="Top performers",width=16,command=performance_chart)
    button9.pack()
    def open_page():
        new_window.destroy()
        root.deiconify()
    button5 =t.Button(new_window,text="Logout",width=16,command=open_page)
    button5.pack()

    new_window.mainloop()