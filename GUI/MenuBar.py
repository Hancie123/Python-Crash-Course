from tkinter import *

app=Tk()
app.title("Hancie Phago")
app.geometry("900x600")
app.resizable(0,0)



frame=Frame(app)
frame.pack()

mainmenu=Menu(frame)
mainmenu.add_command(label="Save")
mainmenu.add_command(label="Exit", command=app.destroy)

app.config(menu=mainmenu)

app.mainloop()