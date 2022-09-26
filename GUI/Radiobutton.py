from tkinter import *

root = Tk()
root.geometry("500x350")
root.title("Hancie e-Learning Studio")

frame = Frame(root)
frame.pack()

Var1 = StringVar()

RBttn = Radiobutton(frame, text="Option1", variable=Var1,value=1)
RBttn.pack(padx=5, pady=5)

RBttn2 = Radiobutton(frame, text="Option2", variable=Var1,value=2)
RBttn2.pack(padx=5, pady=5)

root.mainloop()