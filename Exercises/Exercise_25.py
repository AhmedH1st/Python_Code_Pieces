# Desktop Calculator
from tkinter import *

ls = []
val_calculated = 0
label_string = ''
prev_op_flag = False


def Write_Frame2(but_pressed):
    global ls
    global val_calculated
    global label_string
    global prev_op_flag

    if but_pressed == '=':
        op = ''.join(ls)

        if (op[0]) not in [*'123456789']:
            op = str(val_calculated)+op

        try:
            op = eval(op)
            val_calculated = op
            label_string += but_pressed + str(val_calculated)
            lb1.config(text=str(label_string))
            prev_op_flag = True

        except:
            lb1.config(text="Wrong Entries")
            label_string = ''
            print("Wrong Entries")
            val_calculated = 0

        finally:
            ls.clear()
            label_string = str(val_calculated)

    elif but_pressed == 'D':
        ls.clear()
        val_calculated = 0
        label_string = ''
        lb1.config(text=str(label_string))
        prev_op_flag = False

    else:
        ls.append(but_pressed)
        if ((prev_op_flag == True) and (but_pressed in [*'123456789'])):
            label_string = ''

        prev_op_flag = False
        label_string += but_pressed
        lb1.config(text=str(label_string))

    print(ls)


# main window
window = Tk(className="PY Calculator")
window.geometry('320x450')
window.resizable(False, False)

# Frames Init
f1 = Frame(window, width=320, height=100, background='#ff8')
f2 = Frame(window, width=320, height=80, background='white')
f3 = Frame(window, width=320, height=250, background='blue')
# Frames Placing
f1.place(x=0, y=0)
f2.place(x=0, y=100)
f3.place(x=0, y=180)

#### Widgets ####
# Labels Init
lb1 = Label(f2, text='', background='white')
lb2 = Label(f1, text='PY Calculator', fg='#f00',
            bg='white', font=("Arial", 22))
# Labels Placing
lb1.place(x=0, y=35)
lb2.place(x=70, y=33)

# Buttons Init
bt0 = Button(f3, text='=', command=lambda: Write_Frame2(
    '='), width=6, height=3)
bt1 = Button(f3, text='D', command=lambda: Write_Frame2(
    'D'), width=6, height=3)
bt2 = Button(f3, text='+', command=lambda: Write_Frame2('+'),
             width=6, height=3)
bt3 = Button(f3, text='x', command=lambda: Write_Frame2(
    '*'), width=6, height=3)
bt4 = Button(f3, text='7', command=lambda: Write_Frame2(
    '7'), width=6, height=3)
bt5 = Button(f3, text='8', command=lambda: Write_Frame2(
    '8'), width=6, height=3)
bt6 = Button(f3, text='9', command=lambda: Write_Frame2(
    '9'), width=6, height=3)
bt7 = Button(f3, text='/', command=lambda: Write_Frame2('/'),
             width=6, height=3)
bt8 = Button(f3, text='4', command=lambda: Write_Frame2(
    '4'), width=6, height=3)
bt9 = Button(f3, text='5', command=lambda: Write_Frame2(
    '5'), width=6, height=3)
bt10 = Button(f3, text='6', command=lambda: Write_Frame2(
    '6'), width=6, height=3)
bt11 = Button(f3, text='-', command=lambda: Write_Frame2('-'),
              width=6, height=3)
bt12 = Button(f3, text='0', command=lambda: Write_Frame2(
    '0'), width=6, height=3)
bt13 = Button(f3, text='1', command=lambda: Write_Frame2(
    '1'), width=6, height=3)
bt14 = Button(f3, text='2', command=lambda: Write_Frame2(
    '2'), width=6, height=3)
bt15 = Button(f3, text='3', command=lambda: Write_Frame2(
    '3'), width=6, height=3)

# Buttons Placing
bt0.grid(row=0, column=0)
bt1.grid(row=0, column=1)
bt2.grid(row=0, column=2)
bt3.grid(row=0, column=3)

bt4.grid(row=1, column=0)
bt5.grid(row=1, column=1)
bt6.grid(row=1, column=2)
bt7.grid(row=1, column=3)

bt8.grid(row=2, column=0)
bt9.grid(row=2, column=1)
bt10.grid(row=2, column=2)
bt11.grid(row=2, column=3)

bt12.grid(row=3, column=0)
bt13.grid(row=3, column=1)
bt14.grid(row=3, column=2)
bt15.grid(row=3, column=3)


window.mainloop()
