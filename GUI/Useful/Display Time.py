import tkinter as tk
from tkinter import ttk

my_w = tk.Tk()
my_w.geometry("405x270")
from time import strftime


def my_time():
    time_string = strftime('%I:%M:%S %p \n %A \n %x') # time format
    l1.config(text=time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds


my_font = ('times', 52, 'bold')  # display size and style

l1 = tk.Label(my_w, font=my_font, bg='yellow')
l1.grid(row=1, column=1, padx=5, pady=25)

my_time()
my_w.mainloop()