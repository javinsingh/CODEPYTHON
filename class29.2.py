from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x300')

messagebox.showwarning("Window name", "text to be displayed")
def msg():
    messagebox.showwarning("alert!", "stop! virus found")
button = Button(root, text="scan for virus", command=msg)
button.place(x=40, y=80)
root.mainloop()