from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("Calculator")

e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    global f_num
    global math
    math = "add"
    current_1=e.get()
    f_num = int(current_1)
    e.delete(0,END)
def button_equal():
    second=e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0,f_num + int(second))
    elif math == "sub":
        e.insert(0,f_num - int(second))
    elif math == "mul":
        e.insert(0,f_num * int(second))
    elif math == "div":
        e.insert(0,f_num / int(second))
def button_sub():
    global f_num
    global math
    math = "sub"
    current_1=e.get()
    f_num = int(current_1)
    e.delete(0,END)
def button_mul():
    global f_num
    global math
    math = "mul"
    current_1=e.get()
    f_num = int(current_1)
    e.delete(0,END)
def button_div():
    global f_num
    global math
    math = "div"
    current_1=e.get()
    f_num = int(current_1)
    e.delete(0,END)
    
    
    
bt_1=Button(root,text="1",padx=40,pady=20,command= lambda: button_click(1))
bt_2=Button(root,text="2",padx=40,pady=20,command= lambda: button_click(2))
bt_3=Button(root,text="3",padx=40,pady=20,command= lambda: button_click(3))
bt_4=Button(root,text="4",padx=40,pady=20,command= lambda: button_click(4))
bt_5=Button(root,text="5",padx=40,pady=20,command= lambda: button_click(5))
bt_6=Button(root,text="6",padx=40,pady=20,command= lambda: button_click(6))
bt_7=Button(root,text="7",padx=40,pady=20,command= lambda: button_click(7))
bt_8=Button(root,text="8",padx=40,pady=20,command= lambda: button_click(8))
bt_9=Button(root,text="9",padx=40,pady=20,command= lambda: button_click(9))
bt_0=Button(root,text="0",padx=40,pady=20,command= lambda: button_click(0))
bt_add=Button(root,text="+",padx=39,pady=20,command=button_add)
bt_equal=Button(root,text="=",padx=81,pady=20,bg="green",command=button_equal)
bt_clear=Button(root,text="Clear",padx=71,pady=20,bg="red",command=button_clear)
bt_sub=Button(root,text="-",padx=40,pady=20,command=button_sub)
bt_div=Button(root,text="/",padx=40,pady=20,command=button_div)
bt_mul=Button(root,text="*",padx=40,pady=20,command=button_mul)

bt_1.grid(row=3,column=0)
bt_2.grid(row=3,column=1)
bt_3.grid(row=3,column=2)

bt_4.grid(row=2,column=0)
bt_5.grid(row=2,column=1)
bt_6.grid(row=2,column=2)

bt_7.grid(row=1,column=0)
bt_8.grid(row=1,column=1)
bt_9.grid(row=1,column=2)

bt_0.grid(row=4,column=0)

bt_add.grid(row=5,column=0)
bt_equal.grid(row=5,column=1,columnspan=2)
bt_clear.grid(row=4,column=1,columnspan=2)

bt_sub.grid(row=6,column=0)
bt_mul.grid(row=6,column=1)
bt_div.grid(row=6,column=2)




root.mainloop()