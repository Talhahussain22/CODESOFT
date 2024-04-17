import random
import  string
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
m=Tk()
m.title("Password Generator")
WIDTH,HEIGHT=600,600
m.geometry(f'{WIDTH}x{HEIGHT}')
m.minsize(WIDTH,HEIGHT)
m.maxsize(WIDTH,HEIGHT)
icon_photo=PhotoImage(file='output.png')
m.iconphoto(False,icon_photo)
m.config(background='black')

def copy_text():
    m.clipboard_clear()
    m.clipboard_append(l3["text"])
    messagebox.showinfo("Successfully Copied ")
def generate():
    length=int(e.get())
    password=main(length)
    l3.config(text=password)

def reset():
    l3.config(text='')

val=[2,3,4,5,6,7,8,9]
e=ttk.Combobox(m,width=10,font=("Arial black",20),values=val,state='readonly',style="Custom.TCombobox")

e.place(x=300,y=200)
e.focus()

l1=Label(m,text="Length",width=10,font=('Arial black',20),background='teal')
l1.place(x=50,y=200)
l2=Label(m,text="Password",width=10,font=('Arial black',20),background='teal')
l2.place(x=50,y=300)
l3=Label(m,width=13,font=('Arial black',17),background='grey',height=1)
l3.place(x=300,y=300)

screen_image=Image.open('output.png')
resize=screen_image.resize((200,150))
corn=ImageTk.PhotoImage(resize)
l4=Label(m,image=corn)
l4.place(x=200,y=30)
b=Button(m,text="GENERATE",width=10,font=('Arial black',20),background='teal',command=generate)
b.place(x=200,y=400)

b1=Button(m,text="RESET",width=10,font=('Arial black',20),background='teal',command=reset)
b1.place(x=200,y=500)

copy_image=PhotoImage(file='download (1).png')



b2=Button(m,image=copy_image,background='teal',command=copy_text)
b2.place(x=517,y=305)

def main(length):
    l = []
    a=list(string.ascii_lowercase)
    b=list(string.ascii_uppercase)
    c=list(string.digits)
    l.extend(a)
    l.extend(b)
    l.extend(c)
    password=random.sample(l,length)
    return password
m.mainloop()



