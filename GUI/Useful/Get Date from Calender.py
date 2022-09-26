from tkinter import *
from tkcalendar import *

app=Tk()
app.geometry("900x500")
app.title("Hancie e-Learning Studio")


cal=Calendar()
cal.pack()

def date():
    lbl.config(text=cal.get_date())

btn=Button(app, text="Grab the Date", font='Verdana 16', command=date)
btn.pack()

lbl=Label(app, text="")
lbl.pack()

app.mainloop()