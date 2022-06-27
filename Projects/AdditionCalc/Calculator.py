from tkinter import *

root = Tk()
root.title('My Calc')

myInput = Entry(root, text="", width=40, borderwidth=3)


def putText(m):
    #myInput.delete(0, END)
    myInput.insert(INSERT, m)


def clearField():
    myInput.delete(0, END)


def addNum():
    global op1
    op1 = int(myInput.get())
    clearField()


def resultFunc():
    global op2
    op2 = int(myInput.get())
    result = op1 + op2
    clearField()
    myInput.insert(0, op1+op2)


number7 = Button(root, text="7", width=10, height=4,
                 borderwidth=3, command=lambda m="7": putText(m))
number8 = Button(root, text="8", width=10, height=4,
                 borderwidth=3, command=lambda m="8": putText(m))
number9 = Button(root, text="9", width=10, height=4,
                 borderwidth=3, command=lambda m="9": putText(m))
number4 = Button(root, text="4", width=10, height=4,
                 borderwidth=3, command=lambda m="4": putText(m))
number5 = Button(root, text="5", width=10, height=4,
                 borderwidth=3, command=lambda m="5": putText(m))
number6 = Button(root, text="6", width=10, height=4,
                 borderwidth=3, command=lambda m="6": putText(m))
number1 = Button(root, text="1", width=10, height=4,
                 borderwidth=3, command=lambda m="1": putText(m))
number2 = Button(root, text="2", width=10, height=4,
                 borderwidth=3, command=lambda m="2": putText(m))
number3 = Button(root, text="3", width=10, height=4,
                 borderwidth=3, command=lambda m="3": putText(m))
number0 = Button(root, text="0", width=10, height=4,
                 borderwidth=3, command=lambda m="0": putText(m))

clearBtn = Button(root, text="Clear", width=20, height=4,
                  borderwidth=3, command=clearField)
addBtn = Button(root, text="+", width=10, height=4,
                borderwidth=3, command=addNum)
resultBtn = Button(root, text="=", width=20, height=4,
                   borderwidth=3, command=resultFunc)


myInput.grid(row=0, column=0)
number7.grid(row=1, column=0)
number8.grid(row=1, column=1)
number9.grid(row=1, column=2)

number4.grid(row=2, column=0)
number5.grid(row=2, column=1)
number6.grid(row=2, column=2)

number1.grid(row=3, column=0)
number2.grid(row=3, column=1)
number3.grid(row=3, column=2)

number0.grid(row=4, column=0)
clearBtn.grid(row=4, column=1)


addBtn.grid(row=5, column=0)
resultBtn.grid(row=5, column=1)


root.mainloop()
