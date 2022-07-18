import tkinter as tk

def cal():
    val1 = int(e1.get())
    val2 = int(e2.get())
    result = val1+ val2
    e3.delete(0,len(e3.get()))
    e3.insert(0, result)
    e3.focus()

def sub():
    val1 = int(e1.get())
    val2 = int(e2.get())
    result = val1- val2
    e3.delete(0,len(e3.get()))
    e3.insert(0, result)
    e3.focus()

def mul():
    val1 = int(e1.get())
    val2 = int(e2.get())
    result = val1* val2
    e3.delete(0,len(e3.get()))
    e3.insert(0, result)
    e3.focus()

def div():
    val1 = int(e1.get())
    val2 = int(e2.get())
    result = val1/ val2
    e3.delete(0,len(e3.get()))
    e3.insert(0, result)
    e3.focus()

def clear():
    e1.delete(0,len(e1.get()))
    e2.delete(0,len(e2.get()))
    e3.delete(0,len(e3.get()))
    e1.focus()

root = tk.Tk()
root.geometry("300x600")


l1 = tk.Label(root, text="계산기", fg = "orange", font = "helvetica 16 bold")
num1 = tk.Label(root, text = "값1: ")
num2 = tk.Label(root, text = "값2: ")
num3 = tk.Label(root, text = "결과: ")

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)


l1.place(x=5, y=10)
num1.place(x=20, y=50)
num2.place(x=20, y=80)
num3.place(x=20, y=110)

e1.place(x=75, y=50)
e2.place(x=75, y=80)
e3.place(x=75, y=110)


b1 = tk.Button(root,text="+",command=cal,width=3)
b2 = tk.Button(root,text="-",command=sub,width=3)
b3 = tk.Button(root,text="*",command=mul,width=3)
b4 = tk.Button(root,text="/",command=div,width=3)
b5 = tk.Button(root,text="Clear",command=clear)


b1.place(x=20, y=140)
b2.place(x=60, y=140)
b3.place(x=100, y=140)
b4.place(x=140, y=140)

b5.place(x=180, y=140)

root.mainloop()