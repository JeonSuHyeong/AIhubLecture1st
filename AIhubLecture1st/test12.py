import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.geometry("300x200")
label = tk.Label(window, text="안녕")
#label.pack()
label.place(x=50,y=100)
def b1event():
    a= "hello"
    print(a)
    messagebox.showinfo("예제",a)
button = tk.Button(window, text="누르기",command=b1event)
button.place(x=150,y=100)

window.mainloop()
