from tkinter import *
import math
m=Tk()
m.title("Calculator")
m.geometry('354x310')
m.config(bg='black')
m.config(border=5)
m.minsize(354,310)
m.maxsize(354,310)
def btn_click(value):
    e.insert(END,value)

def evaluate():
    expression=e.get()
    e.delete(0,END)
    e.insert(0,eval(expression))

def erase():
    e.delete(0,END)

e=Entry(m,font=("Arial Black",20),border=28,width=350,background='black',fg='white')
e.place(x=0,y=0)    
e.focus()
btn_1=Button(m,text='0',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(0))
btn_1.place(x=0,y=250)
btn_2=Button(m,text='7',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(7))
btn_2.place(x=0,y=200)
btn_5=Button(m,text='8',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(8))
btn_5.place(x=70,y=200)
btn_3=Button(m,text='9',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(9))
btn_3.place(x=140,y=200)
btn_4=Button(m,text='+',font=("Arial Black",15),background='orange',width=4,command=lambda:btn_click('+'))
btn_4.place(x=210,y=250)
btn_7=Button(m,text='%',font=("Arial Black",15),background='orange',width=4,command=lambda:btn_click('%'))
btn_7.place(x=70,y=250)
btn_8=Button(m,text='.',font=("Arial Black",15),background='orange',width=4,command=lambda:btn_click('.'))
btn_8.place(x=140,y=250)
btn_10=Button(m,text='=',font=("Arial Black",15),background='orange',width=4,command=evaluate,height=4)
btn_10.place(x=280,y=155)
btn_11=Button(m,text='4',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(4))
btn_11.place(x=0,y=150)
btn_12=Button(m,text='5',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(5))
btn_12.place(x=70,y=150)
btn_13=Button(m,text='6',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(6))
btn_13.place(x=140,y=150)
btn_14=Button(m,text='1',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(1))
btn_14.place(x=0,y=100)
btn_15=Button(m,text='2',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(2))
btn_15.place(x=70,y=100)
btn_16=Button(m,text='3',font=("Arial Black",15),background='orange',width=4,command=lambda : btn_click(3))
btn_16.place(x=140,y=100)


btn_19=Button(m,text='AC',font=("Arial Black",15),background='orange',width=4,command=erase)
btn_19.place(x=280,y=100)
btn_20=Button(m,text='-',font=("Arial Black",15),background='orange',width=4,command=lambda:btn_click('-'))
btn_20.place(x=210,y=200)

btn_22=Button(m,text='x',font=("Arial Black",15),background='orange',width=4,command=lambda:btn_click('*'))
btn_22.place(x=210,y=150)

btn_24=Button(m,text='/',font=("Arial Black",15),background='orange',width=4,command=lambda:btn_click('/'))
btn_24.place(x=210,y=100)

m.mainloop()