import time
from tkinter import *

root  = Tk()
root.title("clock")
root.geometry("300x150+0+0")

root.configure(background="black")
root.resizable(0,0)

root.overrideredirect(1)

def start():
    text=time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200,start)

label=Label(root,bg="black",fg="cyan",bd=90)
label.grid(row=0,column=0)
start()
print("done")
root.mainloop()