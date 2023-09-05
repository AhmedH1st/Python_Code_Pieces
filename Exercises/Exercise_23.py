# GUI Basic Button example
from tkinter import *
from functools import partial


def ShowName(name):
    print(str(name))


window = Tk(className="Basic ex")
# window.geometry('500x500+1000+250')
window.resizable(False, False)

bt1 = Button(window, fg='black', bg='white',
             text='Button1', command=lambda: ShowName('Yakeen'))
bt2 = Button(window, fg='black', bg='white',
             text='Button2', command=partial(ShowName, 'Ahmed'))
bt3 = Button(window, fg='black', bg='white',
             text='Button3', command=lambda: ShowName('Hesham'))
bt4 = Button(window, fg='black', bg='white',
             text='Button4', command=partial(ShowName, 'Mohamed'))


bt1.grid(row=0, column=1)
bt2.grid(row=2, column=1)
bt3.grid(row=1, column=0)
bt4.grid(row=1, column=3)

window.mainloop()
