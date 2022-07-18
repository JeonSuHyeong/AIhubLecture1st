from tkinter import *
from tkinter import filedialog
from urllib import request
from bs4 import BeautifulSoup

def Load():
    for location in soup.select("location"):
        #print("도시 : ", location.select_one("city").string)
        a = "도시 : " + location.select_one("city").string + "\t, 날씨 : " + location.select_one("wf").string +"\n"
        txt.insert(END,a)

target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108")
soup = BeautifulSoup(target, "html.parser")
root = Tk()

menubar=Menu(root)

filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu= filemenu)
filemenu.add_command(label="Open", command = Load)

root.config(menu=menubar)

txt = Text(root)
txt.pack()

root.mainloop()

"""
editmenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu= filemenu)

formatmenu = Menu(menubar)
menubar.add_cascade(label="Format", menu= filemenu)

Runmenu = Menu(menubar,text="Run")
menubar.add_cascade(label="File", menu= filemenu)

Optionmenu = Menu(menubar)
menubar.add_cascade(label="File", menu= filemenu)
"""