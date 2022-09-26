from tkinter import *

app=Tk()
app.title("Hancie e-Learning Studio")
app.geometry("500x500")

font=('Verdana', 17,'bold')
btn=Button(app, text="Submit", font=font, bg="blue", fg="white")
btn.pack()


app.mainloop()