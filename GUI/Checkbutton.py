from tkinter import *

app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x500")

Var1 = IntVar()
Var2 = IntVar()

check=Checkbutton(app, text="Male", variable = Var1)
check.pack(padx=5, pady=5)

check2=Checkbutton(app, text="Female", variable = Var2)
check2.pack(padx=5, pady=10)

app.mainloop()