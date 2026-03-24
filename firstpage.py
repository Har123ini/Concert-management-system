import tkinter as t
from tkinter import messagebox
from user_reg import user_registration
from login import login
from connect import connect

def open_fisrt():
    root=t.Tk()
    root.title("Concert Managment System")
    root.geometry("300x300")
    connection=connect()
    if(not(connection)):
        messagebox.showerror(title="error",message="Could not connect db")
        root.destroy()
    else:
        label = t.Label(root,text="Welcome Page")
        label.pack()
        button1 =t.Button(root,text="Sign Up",width=16,command=lambda:user_registration(root))
        button1.pack()
        button2 =t.Button(root,text="Login",width=16,command=lambda:login(root))
        button2.pack()
    root.mainloop()
if __name__=="__main__":
    open_fisrt()

