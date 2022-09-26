from tkinter import *
from tkcalendar import *

app=Tk()
app.geometry("600x500")
app.title("Hancie Phago")

cal=Calendar(app, selectmode="day")
cal.pack()

app.mainloop()