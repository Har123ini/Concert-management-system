import tkinter as t
from tkinter import messagebox
from connect import connect
import pymysql
import userid

def delete_favourite_performer():
    new_window=t.Toplevel()
    new_window.title('delete favourite')
    new_window.geometry("500x500")
    try:
        connection=connect()
        c1=connection.cursor()
        listb=t.Text(new_window,width=100)
        listb.pack()
        c1.execute('call delete_fave(%s)',(userid.userid,))
        ans=c1.fetchall()
        for a in ans:
            g="Performer ID: "+str(a['performer_id'])+"\n"
            listb.insert(t.END,g)
        t.Label(new_window,text="performer_id").pack()
        performer_id=t.Entry(new_window)
        performer_id.pack()
        connection.commit()
        def delete():
            try:
                if performer_id.get().strip()=="":
                    messagebox.showerror(title="error",message="performer id cannot be empty")
                    return
                else:
                    connection=connect()
                    c2=connection.cursor()
                    query = 'call delete_favourite(%s,%s)'
                    c2.execute(query,(userid.userid,int(performer_id.get().strip()),))
                    connection.commit()
                    messagebox.showinfo(title="success",message="Deleted")
                    new_window.destroy()
            except pymysql.Error as e:
                messagebox.showerror(str(e))
        t.Button(new_window,text="Delete",command=delete).pack()
    except pymysql.Error as e:
        messagebox.showerror(title="error",message=str(e))