import tkinter as t
from tkinter import messagebox
from connect import connect
import pymysql
import userid
import re

def update_user():
    new_window=t.Toplevel()
    new_window.title('Update User')
    new_window.geometry("500x500")
    try:
        connection=connect()
        c1=connection.cursor()
        query='select user_name ,password,first_name,last_name,date_of_birth,email,phone_number from user where user_id=(%s);'
        c1.execute(query,(userid.userid,))
        ans=c1.fetchone()
        t.Label(new_window,text="First_name:").pack()
        first_name=t.Entry(new_window)
        first_name.insert(0,ans['first_name'])
        first_name.pack()
        t.Label(new_window,text="Last_name:").pack()
        last_name=t.Entry(new_window)
        last_name.insert(0,ans['last_name'])
        last_name.pack()
        t.Label(new_window,text="Date of Birth:(YYYY-MM-DD)").pack()
        dob=t.Entry(new_window)
        dob.insert(0,ans['date_of_birth'])
        dob.pack()
        t.Label(new_window,text="email:").pack()
        email=t.Entry(new_window)
        email.insert(0,ans['email'])
        email.pack()
        t.Label(new_window,text="phone:").pack()
        phone=t.Entry(new_window)
        phone.insert(0,ans['phone_number'])
        phone.pack()
        def update():
            firstname=first_name.get().strip()
            lastname=last_name.get().strip()
            dateofbirth=dob.get().strip()
            email1=email.get().strip()
            phone1=phone.get().strip()
            if firstname=="":
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
            elif(len(firstname)>64):
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
                        query = 'call update_user(%s,%s,%s,%s,%s,%s)'
                        c1.execute(query,(userid.userid,firstname,lastname,dateofbirth,email1,phone1,))
                        connection.commit()
                        messagebox.showinfo(title="success",message="Update Success")
                        new_window.destroy()
                except pymysql.Error as e:
                        messagebox.showerror(str(e))
        t.Button(new_window,text="Update",command=update).pack()
    except pymysql.Error as e:
        messagebox.showerror(str(e))
        new_window.destroy()