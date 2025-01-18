from  tkinter import *
root = Tk
root.title("ur birth year")
root.geometry('400x400')
lbl = Label(text='enter your age', fg='white', bg='#0000FF')
age_lbl = Label(text='age', fg="#000000")
age_entry = Entry()
age = age_entry.get()
result = age - 2025
lbl = Label(text=(result), fg='#FF0000')

