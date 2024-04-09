# from tkinter import *
# from tkinter import messagebox
# from PIL import Image,ImageTk
# from tkinter import ttk
# from tkinter import filedialog
# m=Tk()
# m.config(background='black')
# m.geometry("750x600")
# m.title("To-do-list")
# m.maxsize(750,600)
# m.minsize(750,600)
# image=Image.open('tick.png')
# resize=image.resize((50,50))
# resized=ImageTk.PhotoImage(resize)

# def add():
#     content=e.get()
#     if content!="":
#         tree.insert('',index='end',text=content)
#     else:
#         messagebox.showinfo("Enter Something!")

# def delete():
#     content=tree.focus()
#     if content!='':
#         tree.delete(content)
#     else:
#         messagebox.showinfo("Select Something!")

# def update():
#     content=tree.focus()
#     if content!='':
#         new_content=e.get()
#         tree.item(content,text=new_content)
#     else:
#         messagebox.showinfo("Select Something!")
# def clear():
#      tree.delete(*tree.get_children())
#      messagebox.showinfo("Successfully Deleted!")

# def review():
#     menu=Menu(m,tearoff=0)
#     menu.add_command(label="Completed",command=task_completed)
#     menu.add_command(label="Postponded",command=postponded)
#     try:
#         menu.tk_popup(m.winfo_pointerx(), m.winfo_pointery())
#     finally:
#         menu.grab_release()
# def task_completed():
#     task=tree.focus()
#     if task!="":
#             tree.set(task,'#2',value='Done')
#             tree.tag_configure('colored',background='green')
#             tree.item(task,tags=('colored',))
#     else:
#         messagebox.showinfo("Select Something!")
# def postponded():
#     task=tree.focus()
#     if task!="":
#             tree.set(task,'#2',value='Postponded')
#             tree.tag_configure('colored1',background='red')
#             tree.item(task,tags=('colored1',))
# def save_to_file():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
#     if file_path:
#         with open(file_path, "w") as file:
#             for item in tree.get_children():
#                 value = tree.item(item, "values")
#                 text=tree.item(item,'text')
#                 try:
#                     file.write(f"{text}-->{value[1]}\n") 
#                 except:    
#                     file.write(f"{text}\n")       
# style = ttk.Style(m)
# style.theme_use("clam")
# style.configure("Treeview", background="pink", 
#                 fieldbackground="pink", foreground="black",font=("Helvitica",13))

# tree=ttk.Treeview(m,columns=('','Name','Image'))
# vsb = ttk.Scrollbar(m, orient="vertical", command=tree.yview)
# vsb.pack(side="right", fill="y")
# tree.configure(yscrollcommand=vsb.set)

# hsb = ttk.Scrollbar(m, orient="horizontal", command=tree.xview)
# hsb.pack(side="bottom", fill="x")
# tree.configure(xscrollcommand=hsb.set)
# tree.place(x=20,y=300,width=700,bordermode='outside')


# l=Label(m,text='Enter the task:',font=('Arial black',15),fg='white',background='black')
# l.place(x=20,y=47)
# e=Entry(m,font=('Helvitica',15),width=47)
# e.place(x=200,y=50)
# b1=Button(m,text='Add Task',fg='black',background='#CCA01D',font=('Arial black',15),width=13,command=add)
# b1.place(x=18,y=100)
# b2=Button(m,text='Update Task',fg='black',background='#CCA01D',font=('Arial black',15),width=13,command=update)
# b2.place(x=280,y=100)
# b3=Button(m,text='Delete Task',fg='black',background='#CCA01D',font=('Arial black',15),width=13,command=delete)
# b3.place(x=538,y=100)
# b4=Button(m,text='Review Task',fg='black',background='#CCA01D',font=('Arial black',15),width=13,command=review)
# b4.place(x=18,y=200)
# b5=Button(m,text='Clear Tasks',fg='black',background='#CCA01D',font=('Arial black',15),width=13,command=clear)
# b5.place(x=280,y=200)
# b6=Button(m,text='Save Tasks',fg='black',background='#CCA01D',font=('Arial black',15),width=13,command=save_to_file)
# b6.place(x=538,y=200)

# m.mainloop()






