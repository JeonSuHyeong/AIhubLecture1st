import tkinter as tk
from tkinter import messagebox
import time

def clock():
    T= time.strftime("%H:%M:%S")
    label1.config(text=T)
    label1.after(200, clock)

root = tk.Tk()
root.title("Clock")
root.geometry("400x200")
label = tk.Label(root, text="현재시간", font="맑은고딕 16 bold")
label.pack()

label1 = tk.Label(root, font="boulder 68 bold", bg = "white", bd = 8)
label1.pack()
clock()

root.mainloop()