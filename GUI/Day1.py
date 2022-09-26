from tkinter import *
from tkinter import messagebox

hancie=Tk()
hancie.geometry("999x300")
hancie.minsize(400,400)
hancie.maxsize(400,400)

var=Label(text="My name is Hancie Phago")
var.pack()

def phago():
    messagebox.showerror("Hancie Phago","Hancie")

b=Button(hancie, text="Hello",bg="#30336b", fg="#dff9fb", width=15,font=("Times New Roman", 15) ,command=phago)
b.pack(side=BOTTOM)

check=Checkbutton(hancie, text="Check Button")
check.pack()

text=Entry(hancie, width=20).place(x=190, y=50)


hancie.mainloop()
