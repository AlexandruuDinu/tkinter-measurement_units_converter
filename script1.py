from tkinter import *

window = Tk()


def convert_units():
    grams = float(entry_val.get()) * 1000
    text_grams.insert(END, grams)
    pounds = float(entry_val.get()) * 2.20462
    text_pounds.insert(END, pounds)
    ounces = float(entry_val.get()) * 35.274
    text_ounces.insert(END, ounces)


label_unit = Label(window, text='Insert number of kilograms:')
label_unit.grid(row=0, column=0)

label_unit1 = Label(window, text='Grams')
label_unit1.grid(row=1, column=0)
label_unit2 = Label(window, text='Pounds')
label_unit2.grid(row=1, column=1)
label_unit3 = Label(window, text='Ounces')
label_unit3.grid(row=1, column=2)

btn1 = Button(window, text='Convert', command=convert_units)
btn1.grid(row=0, column=2)

entry_val = StringVar()
entry1 = Entry(window, textvariable=entry_val)
entry1.grid(row=0, column=1)

text_grams = Text(window, height=1, width=20)
text_grams.grid(row=2, column=0)

text_pounds = Text(window, height=1, width=20)
text_pounds.grid(row=2, column=1)

text_ounces = Text(window, height=1, width=20)
text_ounces.grid(row=2, column=2)

window.mainloop()
