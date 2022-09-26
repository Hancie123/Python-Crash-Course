from tkinter import *



app=Tk()
app.geometry("990x500")
app.minsize(400,400)
app.maxsize(900,900)
app.title("Hancie Phago")

photo=PhotoImage(file="1.png")

lbl=Label(image=photo)
lbl.pack()




app.mainloop()

