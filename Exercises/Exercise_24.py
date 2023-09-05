# GUI program that asks the user to enter a sentence and return him its reverse
from tkinter import *


def reverse():
    rev_sen = (en1.get())
    rev_sen = rev_sen[::-1]
    lb2.config(text=rev_sen)


window = Tk(className="REVERSE")
window.geometry('270x270')
window.resizable(False, False)

lb1 = Label(window, text='Enter a word')
lb2 = Label(window, text='')
en1 = Entry(window)
bt = Button(window, text='Validate', command=reverse)

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=1)
en1.grid(row=0, column=1)
bt.grid(row=2, column=1)

window.mainloop()
