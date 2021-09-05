from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("My_Clock")

def clock():
    current_time = strftime('%H:%M:%S %p')
    lable.config(text = current_time)
    lable.after(1000, clock)

lable = Label(root, font = (" ", 200), background = "black", foreground = "red")
lable.pack(anchor='center')

clock()

mainloop()