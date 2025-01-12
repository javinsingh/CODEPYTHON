#importing
import tkinter
from datetime import date

#window
root = Tk()
root.title = ("getting started with widgets")
root.geometry = ('300x400')

#add widgets and label
lbl = Label(text='hey there!', fg='white', bg='#072FSF', height=1, width=300)

#user input
name_lbl = Label('text=full name', bg='#3895d3')
name_entry = Entry()

#display message 
def display():
    name = name_entry.get()
    global message 
    message = "welcome to the application! \ntodays date is:"
    greet = "hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = button(text="begin", command=display, height=1, bg="#1261A0", fg='white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

    
        


