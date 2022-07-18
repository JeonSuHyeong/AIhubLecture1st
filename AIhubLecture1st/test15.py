from tkinter import *

def b1event():
    #txt.insert(END,"Hello\n")
    #구구단으로 변환
    for i in range(1,10):
        txt.insert(END,f"2*{i}={i*2}\n")
        #다른방법
        """
        a='{} {} {} {} {} {}'.format(2,'*',i,'=',2*i,'\n')
        txt.insert(END,a)
        """


root = Tk()
root.geometry("300x600")

b1= Button(root, text="클릭", command=b1event)
b1.pack()

sb=Scrollbar(root)
sb.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=sb.set)
txt.pack(side= "right", fill = "both", expand= True)
sb.config(command=txt.yview)



root.mainloop()