from tkinter import *
from tkinter import ttk

app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x500")

data=["Hancie","Nitesh","Aveshesh","Ajaya"]

combo=ttk.Combobox(app, value=data, font=('Verdana', 14, 'normal'))
combo.set("Pick from option")
combo.pack(padx = 5, pady = 50)

app.mainloop()