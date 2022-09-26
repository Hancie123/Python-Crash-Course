from tkinter import *

app=Tk()
app.geometry("500x500")
app.title("Hancie e-Learning Studio")

font=('Verdana',16)
label = Label(app,text = "A list of friends name.", font=font)
label.pack()

listbox=Listbox(app, font=font)
listbox.insert(0,"Hancie")
listbox.insert(1,"Nitesh")
listbox.insert(2,"Ajaya")
listbox.insert(3,"Aveshesh")
listbox.insert(4,"Nishav")
listbox.insert(5,"Suprasiddha")

listbox.pack()


app.mainloop()