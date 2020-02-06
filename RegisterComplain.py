from tkinter import *
from tkinter.font import Font

root = Tk()

root.title("Compalin Registration")

titleframe = Frame(root, width=30, height=30)

title_font = Font(family="Times New Roman", size=14)

title_name = Label(titleframe, text="Register Complain", font=title_font)
title_name.pack()

titleframe.pack()

# ---------STATION INFORMATION-----


frame1 = Frame(root, width=30, height=30, pady=15)
frame1.pack()
label_font = Font(family="Times New Roman", size=13)

station_name = Label(frame1, text="Station Name  ", font=label_font).grid(row=0, column=0)
enter_station_name = Entry(frame1).grid(row=0, column=1)

Label(frame1).grid(row=1, column=1)

station_state = Label(frame1, text="Station State  ", font=label_font).grid(row=2, column=0)
enter_station_name = Entry(frame1).grid(row=2, column=1)

Label(frame1).grid(row=3, column=3)

station_area = Label(frame1, text="Station Area  ", font=label_font).grid(row=4, column=0)
enter_station_area = Entry(frame1).grid(row=4, column=1)

Label(frame1).grid(row=5, column=5)

station_postalcode = Label(frame1, text="Station Postal Code  ", font=label_font).grid(row=6, column=0)
enter_station_postalcode = Entry(frame1).grid(row=6, column=1)

# -----RegisterComplain


frame2 = Frame(root)
frame2.pack()

label_font = Font(family="Times New Roman", size=14)

vname = Label(frame2, text="enter victim name ", font=label_font, anchor=NW)
vname.grid(row=0, column=0)
enter_victim_name = Entry(frame2).grid(row=0, column=1)

lab2 = Label(frame2, anchor=NW).grid(row=1, column=1)

wname = Label(frame2, text="enter witness name", font=label_font, anchor=NW)
wname.grid(row=3, column=0)
enter_victim_name = Entry(frame2).grid(row=3, column=1)

lab2 = Label(frame2, anchor=NW).grid(row=4, column=4)

comp = Label(frame2, text="enter your complain statement", font=label_font, anchor=NW)
comp.grid(row=5, column=0)
f4 = Frame(root)
f4.pack()
txt_font = Font(family="Times New Roman", size=10)
enter_your_complain_statement = Text(f4, width=90, height=12, wrap=WORD,
                                     padx=7, pady=7, bd=5, font=txt_font)
enter_your_complain_statement.pack()

root.geometry("600x650+180+10")
root.mainloop()
