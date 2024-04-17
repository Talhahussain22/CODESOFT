import random
import time
from tkinter import *
from PIL import Image,ImageTk
m=Tk()
m.title("Rock-Paper-Scissor")
m.config(background='teal')
m.geometry(f'{m.winfo_screenwidth()}x{m.winfo_screenheight()}')

computer_wins=0
user_wins=0

lbl=Label(m,fg='orange',bg='teal',font=("Arial black",25))
lbl.place(x=10,y=450)
w_lbl=Label(m,font=("Arial black",28),fg='orange',bg='teal')
w_lbl.place(x=10,y=600)
def Rock():
 
    global computer_wins,user_wins
    user='ROCK'
    l=['ROCK','PAPER','SCISSOR']
    computer=random.choice(l)
    if user==computer:
        lbl.config(text="\t\t\tDraw!")
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")
        
    elif computer=='PAPER':
        lbl.config(text=f"Computer:PAPER\t\t\t\tUser:ROCK\n\tCOMPUTER WON!\n")
        computer_wins+=1
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")

    elif computer=='SCISSOR':
        lbl.config(text=f"Computer:SCISSOR\t\t\t\tUser:ROCK\n\tYOU WON!\n")
        user_wins+=1
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")

def Scissor():
 
    global computer_wins,user_wins
    user='SCISSOR'
    l=['ROCK','PAPER','SCISSOR']
    computer=random.choice(l)
    if user==computer:
        lbl.config(text="\t\t\tDraw!")
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")
        
    elif computer=='ROCK':
        lbl.config(text=f"Computer:ROCK\t\t\t\tUser:SCISSOR\n\tCOMPUTER WON!\n")
        computer_wins+=1
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")
     

    elif computer=='PAPER':
        user_wins+=1
        lbl.config(text=f"Computer:PAPER\t\t\t\tUser:SCISSOR\n\tYOU WON!\n")
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")

def Paper():
    global computer_wins,user_wins
    user='PAPER'
    l=['ROCK','PAPER','SCISSOR']
    computer=random.choice(l)
    if user==computer:
        lbl.config(text="\t\t\tDraw!")
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")
        
    elif computer=='SCISSOR':
        lbl.config(text=f"Computer:SCISSPR\t\t\t\tUser:PAPER\n\tCOMPUTER WON!\n")
        computer_wins+=1
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")
     

    elif computer=='ROCK':
        user_wins+=1
        lbl.config(text=f"Computer:ROCK\t\t\t\tUser:PAPER\n\tYOU WON!\n")
        w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\tUser Win:{user_wins}")
       


def Reset():
    global computer_wins,user_wins
    computer_wins=0
    user_wins=0
    w_lbl.config(text=f"Computer Win:{computer_wins}\t\t\t\tUser Win:{user_wins}")
paper_image=Image.open('paper1.png')
for_resize=paper_image.resize((150,150))
resized=ImageTk.PhotoImage(for_resize)
b1=Button(m,image=resized,command=Paper,background='black')
b1.place(x=50,y=150)

rock_image=Image.open('ROCK.png')
for_resize1=rock_image.resize((150,150))
resized1=ImageTk.PhotoImage(for_resize1)
b2=Button(m,image=resized1,command=Rock,background='black')
b2.place(x=600,y=150)

scissor_image=Image.open('scissor.jpeg')
for_resize2=scissor_image.resize((150,150))
resized2=ImageTk.PhotoImage(for_resize2)
b3=Button(m,image=resized2,command=Scissor,background='black')
b3.place(x=1150,y=150)

b4=Button(m,text="RESET",command=Reset,font=("Arial black",20),background='orange',fg='black')
b4.place(x=600,y=620)
m.mainloop()

    
