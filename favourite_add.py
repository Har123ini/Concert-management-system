import tkinter as t
from tkinter import Listbox
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def favourite_performer():
    new_window=t.Toplevel()
    new_window.title('favourite')
    new_window.geometry("500x500")
    try:
        connection=connect()
        c1=connection.cursor()
        listb=Listbox(new_window,width=200)
        listb.pack()
        c1.execute('call list_performer()')
        ans=c1.fetchall()
        list1=[]
        for a in ans:
            list1.append(a)
            g="Performer ID: "+str(a['performer_id'])+" Performer name: "+str(a['full_name'])+"\n";
            listb.insert(t.END,g)
        t.Label(new_window,text="performer_id").pack()
        performer_id=t.Entry(new_window)
        performer_id.pack()
        connection.commit()
        def add():
            try:
                if performer_id.get().strip()=="":
                    messagebox.showerror(title="error",message="performer id cannot be empty")
                    return
                else:
                    connection=connect()
                    c2=connection.cursor()
                    query = 'call add_favourite(%s,%s)'
                    c2.execute(query,(userid.userid,int(performer_id.get().strip()),))
                    connection.commit()
                    messagebox.showinfo(title="success",message="Added")
                    new_window.destroy()
            except pymysql.Error as e:
                messagebox.showerror(title="error",message=str(e))
        t.Button(new_window,text="add",command=add).pack()
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))