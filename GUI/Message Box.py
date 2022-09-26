from tkinter import *
from tkinter import messagebox

app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x500")

def error():
    promt = messagebox.showinfo(title="Error!", message="Error is found!")

btn=Button(app, text="Submit", command=error)
btn.pack()

app.mainloop()