from tkinter.colorchooser import askcolor
from tkinter import *

root =Tk()
root.title("Hancie e-Learning Studio")
root.geometry("500x500")

def callback():
    result = askcolor(title="Tkinter Color Chooser")
    label.configure(fg=result[1])
    print(result[1])

btn=Button(root, text='Choose Color', command=callback).pack(pady=20)

label = Label(root, text="Color", fg="black")
label.pack()

root.mainloop()