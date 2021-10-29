from math import *
from time import *
from tkinter import *

def update():
    h,m,s=int(strftime("%I")),int(strftime("%M")),int(strftime("%S"))
    canvas.coords(hours,250,250,250+130*cos((h-3)*pi/6),250+130*sin((h-3)*pi/6))
    canvas.coords(minutes,250,250,250+150*cos((m-15)*pi/30),250+150*sin((m-15)*pi/30))
    canvas.coords(seconds,250,250,250+170*cos((s-15)*pi/30),250+170*sin((s-15)*pi/30))
    win.after(1000,update)

win=Tk()
win.title("Clock")
win.geometry("500x500")
canvas=Canvas(win,width=500,height=500)
canvas.place(x=0,y=0)
canvas.create_oval(50,50,450,450,width=15,fill="white")
canvas.create_oval(240,240,260,260,fill="black")
for i in range(1,13):
    canvas.create_text(250+180*cos((i-3)*pi/6),250+180*sin((i-3)*pi/6),text=str(i),font=("Arial",15))
hours=canvas.create_line(250,250,250,250,width=10)
minutes=canvas.create_line(250,250,250,250,width=7)
seconds=canvas.create_line(250,250,250,250,width=4)
update()
win.mainloop()
