from tkinter import *

window = Tk
window.geometry('100x100')

def calculate(event):
    print(result)

inches_lbl = Label(text='enter inches', bg='#000000')
inches_entry = Entry()
inches = inches_entry.get
result = inches / 2.54
button = Button(text='show answer')
button.pack()
button.place(y=40, x=80)
button.bind("<button-1>", calculate)
window.mainloop()
