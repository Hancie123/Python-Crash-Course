from tkinter import *

app=Tk()
app.title("Hancie Phago")
app.geometry("900x500")
app.state("zoomed")

f1=Frame(app, bg="red")
f1.pack(side="top", fill="x")

lbl=Label(f1, text="Welcome to my application", bg="grey", pady=25, padx=30, font="Tahoma 18 bold")
lbl.pack(padx=20, pady=30)

f2=Frame(app, bg="grey")
f2.pack(side=LEFT, fill=Y)

lbl2=Label(f2, text="Vertical Menu", padx=50, font="Tahoma 16 underline normal")
lbl2.pack(pady=290)


app.mainloop()