import math
import tkinter as tk
import time

my_w = tk.Tk()
# my_w.tk.call('tk', 'scaling',200)
width, height = 620, 620  # set the variables
c_width, c_height = width - 5, height - 5  # canvas width height
d = str(width) + "x" + str(height)
my_w.geometry(d)
c1 = tk.Canvas(my_w, width=c_width, height=c_height, bg='lightgreen')
c1.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
dial = c1.create_oval(10, 10, 600, 600, width=15, outline='#FF0000', fill='#FFFFFF')
x, y = 305, 305  # center
x1, y1, x2, y2 = x, y, x, 10  # second needle
center = c1.create_oval(x - 8, y - 8, x + 8, y + 8, fill='#c0c0c0')
r1 = 280  # dial lines for one minute
r2 = 210  # for hour numbers  after the lines
rs = 210  # length of second needle
rm = 180  # length of minute needle
rh = 160  # lenght of hour needle
in_degree = 0
in_degree_s = int(time.strftime('%S')) * 6  # local second
in_degree_m = int(time.strftime('%M')) * 6  # local minutes
in_degree_h = int(time.strftime('%I')) * 30  # 12 hour format
if (in_degree_h == 360):
    in_degree_h = 0  # adjusting 12 O'clock to 0
h = iter(['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
# second=c1.create_line(x1,y1,x2,y2,arrow='last',width=1)
for i in range(0, 60):
    in_radian = math.radians(in_degree)
    if (i % 5 == 0):
        ratio = 0.85  # Long marks ( lines )
        t1 = x + r2 * math.sin(in_radian)  # coordinate to add text ( hour numbers )
        t2 = x - r2 * math.cos(in_radian)  # coordinate to add text ( hour numbers )
        c1.create_text(t1, t2, fill='blue', font="Times 30  bold", text=next(h))  # number added
    else:
        ratio = 0.9  # small marks ( lines )

    x1 = x + ratio * r1 * math.sin(in_radian)
    y1 = y - ratio * r1 * math.cos(in_radian)
    x2 = x + r1 * math.sin(in_radian)
    y2 = y - r1 * math.cos(in_radian)
    c1.create_line(x1, y1, x2, y2, width=1)  # draw the line for segment
    in_degree = in_degree + 6  # increment for next segment
# End of Marking on the dial with hour numbers
# Initialize the second needle based on local seconds value
in_radian = math.radians(in_degree_s)
x2 = x + rs * math.sin(in_radian)
y2 = y - rs * math.cos(in_radian)
second = c1.create_line(x, y, x2, y2, fill='red', width=2)  # draw the second needle


def my_second():
    global in_degree_s, second
    in_radian = math.radians(in_degree_s)
    c1.delete(second)  # delete the needle
    x2 = x + rs * math.sin(in_radian)  # Horizontal coordinate of outer edge
    y2 = y - rs * math.cos(in_radian)  # vertical coordinate of outer adge
    second = c1.create_line(x, y, x2, y2, arrow='last', fill='red', width=2)
    if (in_degree_s >= 360):  # one rotattion is over if reached 360
        in_degree_s = 0  # start from zero angle again
        my_minute()  # call the minute needle to move one segment.
    in_degree_s = in_degree_s + 6  # increment of one segment is 6 degree
    c1.after(1000, my_second)  # timer calling recrusive after 1 second


# End of second
# Initialize Minutes needle based on local time minute value
in_radian = math.radians(in_degree_m)
x2 = x + rm * math.sin(in_radian)
y2 = y - rm * math.cos(in_radian)
minute = c1.create_line(x, y, x2, y2, width=4, fill='green')


def my_minute():
    global in_degree_m, minute
    in_degree_m = in_degree_m + 6  # increment for each segment
    in_radian = math.radians(in_degree_m)  # coverting to radian
    c1.delete(minute)  # delete the previous needle
    x2 = x + rm * math.sin(in_radian)  # Horizontal coordinate of outer edge
    y2 = y - rm * math.cos(in_radian)  # vertical coordinate of outer dege
    minute = c1.create_line(x, y, x2, y2, width=4, fill='green')
    my_hour()  # calling hour needle to move
    if (in_degree_m >= 360):  # One rotation of 360 degree is over
        in_degree_m = 0


# initialize hour needle based on local hour
# Adding extra hour needle  movment based on local minute value
# For 7 Hour 45 minutes, hour needle need to move beyond 7
in_degree_h = in_degree_h + (in_degree_m * 0.0833333)
in_radian = math.radians(in_degree_h)
x2 = x + rh * math.sin(in_radian)
y2 = y - rh * math.cos(in_radian)
hour = c1.create_line(x, y, x2, y2, width=6, fill='#a83e32')


def my_hour():
    global in_degree_h, hour
    in_degree_h = in_degree_h + 0.5  # increment in each step
    in_radian = math.radians(in_degree_h)  # in radian
    c1.delete(hour)  # deleting hour needle
    x2 = x + rh * math.sin(in_radian)  # Horizontal coordinate for outer edge
    y2 = y - rh * math.cos(in_radian)  # vertical coordinate for outer adge
    hour = c1.create_line(x, y, x2, y2, width=6, fill='#a83e32')
    if (in_degree_h >= 360):
        in_degree_h = 0


my_second()  # calling to start
my_w.mainloop()
