import tkinter as tk

def b1event():
    txt.insert(END,"Hello\n")

root = tk.Tk()
root.geometry("300x600")

b1= tk.Button(root, text="클릭", command=b1event)
b1.pack()

sb=tk.Scrollbar(root)
sb.pack(side="right", fill="yes")

txt = tk.Text(root)
txt.pack()


root.mainloop()
