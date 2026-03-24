import tkinter as t
from tkinter import messagebox
import pymysql
from connect import connect
import userid
import mainuserpage
username=""
password=""
def login(root):
    root.withdraw()
    new_window=t.Toplevel()
    new_window.title('Login')
    new_window.geometry("500x500")
    t.Label(new_window,text="Username:").pack()
    username=t.Entry(new_window)
    username.pack()
    t.Label(new_window,text="Password:").pack()
    password=t.Entry(new_window)
    password.pack()
    def user_login():
           user_name=username.get().strip()
           password1=password.get().strip()
           try:
              if user_name.strip()=="":
                    messagebox.showerror(title="error",message="username cannot be empty")
                    return
              elif password1.strip()=="":
                    messagebox.showerror(title="error",message="password cannot be empty")
                    return
              else:
                  connection=connect()
                  if(connection):
                     c1=connection.cursor()
                     query = 'call login(%s,%s)'
                     c1.execute(query,(user_name,password1,))
                     ans=c1.fetchone()
                     userid.userid=ans['user_id']
                     connection.commit()
                     messagebox.showinfo(title="success",message="Logged in")
                     new_window.destroy()
                     root.withdraw()
                     mainuserpage.mainuser(root)
                  else:
                        messagebox.showerror(title="error",message="Could not connect to DB")
           except pymysql.Error as e:
                  messagebox.showerror(title="error",message=str(e))
                  new_window.destroy()
                  root.deiconify()
    t.Button(new_window,text="Login",command=user_login).pack(pady=10)
    new_window.mainloop()



