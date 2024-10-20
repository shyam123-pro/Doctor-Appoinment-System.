import tkinter
import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from eshu import *
t=tkinter.Tk()
t.geometry('800x800')
t.title('login screen')
c1=Canvas(t,height=1080,width=1280,bg='light green')
c1.place(x=0,y=0)
def login():
    aa=b.get()
    bb=d.get()
    db=mysql.connector.connect(host='localhost',user='root',password='root',db='das')
    cur=db.cursor()
    
    sql="select count(*) from login where userid='%s'and password='%s'"%(aa,bb)
    cur.execute(sql)
    data=cur.fetchone()
    if data[0]==0:
        messagebox.showerror('hii','login not found')
    else:
        messagebox.showinfo('hii','login success')
        mainscreen()
def cl():
    t.destroy()
c3=IntVar()
def show():
    if(c3.get()==1):
        d.config(show='')
    else:
        d.config(show='*')
p=Label(t,text='SIGN IN / lOGIN',width=15,font='Algerian',bg='peru')
p.place(x=320,y=20)
a=Label(t,text='userid')
a.place(x=200,y=100)
b=Entry(t,width=30)
b.place(x=300,y=100)
c=Label(t,text='password')
c.place(x=200,y=150)
d=Entry(t,width=30,show='*')
b3=IntVar()
b3=Checkbutton(t,text='showpassword',variable=c3,command=show)
b3.place(x=500,y=150)

d.place(x=300,y=150)
f=Button(t,text='forget password')
f.place(x=400,y=180)
bt=Button(t,text='login',command=login,bg='light blue',width=10,font='Algerian')
bt.place(x=300,y=230,width=100)
bt=Button(t,text='Cancel',command=cl,bg='light blue',width=10,font='Algerian')
bt.place(x=420,y=230,width=100)
p=Label(c1,text='plz enter your details')
p.place(x=320,y=50)

t.mainloop()
