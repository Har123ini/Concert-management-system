import tkinter as t
from tkinter import messagebox
import pymysql
import connect
import userid
import re

def user_registration(root):
    try:
            connection = connect.connect()
    except pymysql.Error as e:
            code, msg = e.args
            print("Cannot connect to the database", code, msg)
    root.withdraw()
    new_window=t.Toplevel()
    new_window.title('Registration')
    new_window.geometry("500x500")
    t.Label(new_window,text="Username:").pack()
    username=t.Entry(new_window)
    username.pack()
    t.Label(new_window,text="Password:").pack()
    password=t.Entry(new_window)
    password.pack()
    t.Label(new_window,text="First_name:").pack()
    first_name=t.Entry(new_window)
    first_name.pack()
    t.Label(new_window,text="Last_name:").pack()
    last_name=t.Entry(new_window)
    last_name.pack()
    t.Label(new_window,text="Date of Birth(YYYY-MM-DD):").pack()
    dob=t.Entry(new_window)
    dob.pack()
    t.Label(new_window,text="email:").pack()
    email=t.Entry(new_window)
    email.pack()
    t.Label(new_window,text="phone:").pack()
    phone=t.Entry(new_window)
    phone.pack()
    def reg_user():
           user_name=username.get().strip()
           password1=password.get().strip()
           firstname=first_name.get().strip()
           lastname=last_name.get().strip()
           dateofbirth=dob.get().strip()
           email1=email.get().strip()
           phone1=phone.get().strip()
           if user_name=="":
                    messagebox.showerror(title="error",message="username cannot be empty")
                    return
           elif password1=="":
                    messagebox.showerror(title="error",message="password cannot be empty")
                    return
           elif firstname=="":
                    messagebox.showerror(title="error",message="firstname cannot be empty")
                    return
           elif lastname=="":
                    messagebox.showerror(title="error",message="lastname cannot be empty")
                    return
           elif dateofbirth=="":
                    messagebox.showerror(title="error",message="Date of birth cannot be empty")
                    return
           elif email1=="":
                  messagebox.showerror(title="error",message="email cannot be empty")
                  return
           elif phone1=="":
                  messagebox.showerror(title="error",message="phone cannot be empty")
                  return
           elif(len(user_name)>64):
                  messagebox.showinfo(title="error",message="Username too long")
                  return
           elif(len(password1)>64):
                  messagebox.showinfo(title="error",message="password too long")
                  return
           if(len(firstname)>64):
                 messagebox.showinfo(title="error",message="first name too long")
                 return
           elif(len(lastname)>64):
                  messagebox.showinfo(title="error",message="lastname too long")
                  return
           elif not re.match(r"^[^@]+@[^@]+\.[a-zA-Z]+$",email1):
                 messagebox.showinfo(title="error",message='invalid email')
                 return
           elif not re.match(r"^\d{10}$",phone1):
                 messagebox.showinfo(title="error",message='invalid phone')
                 return
           elif(len(phone1)>10):
                  messagebox.showinfo(title="error",message="number too long")
                  return
           else:
                try:
                        c1=connection.cursor()
                        query = 'call insert_user(%s,%s,%s,%s,%s,%s,%s)'
                        c1.execute(query,(user_name,password1,firstname,lastname,dateofbirth,email1,phone1,))
                        query = 'call login(%s,%s)'
                        c1.execute(query,(user_name,password1,))
                        ans=c1.fetchone()
                        print(ans)
                        userid.userid=ans['user_id']
                        connection.commit()
                        messagebox.showinfo(title="success",message="Success")
                        new_window.destroy()
                        root.deiconify()
                except pymysql.Error as e:
                        messagebox.showerror(str(e))
                        root.deiconify()
    t.Button(new_window,text="Register",command=reg_user).pack(pady=10)
    new_window.mainloop()
