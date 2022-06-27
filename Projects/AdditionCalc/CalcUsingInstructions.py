from tkinter import *

root = Tk()
root.title('My Calc')

myInput = Entry(root, text="", width=48, borderwidth=3)
myInput.grid(row=0, column=0, columnspan=3)


def putText(m):
    #myInput.delete(0, END)
    # current = myInput.get()
    # myInput.delete(0, END)
    # myInput.insert(0, str(current) + m)
    myInput.insert(INSERT, m)


def clearField():
    myInput.delete(0, END)


def addNum():
    global op1
    global operationDone
    op1 = int(myInput.get())
    clearField()
    operationDone = "add"


def resultFunc():
    global op2
    op2 = int(myInput.get())
    result = op1 + op2
    clearField()
    if operationDone == "add":
        myInput.insert(0, op1+op2)
    elif operationDone == "sub":
        myInput.insert(0, op1 - op2)
    elif operationDone == "mul":
        myInput.insert(0, op1*op2)
    else:
        myInput.insert(0, op1 / op2)


def subNum():
    global op1
    global operationDone
    op1 = int(myInput.get())
    clearField()
    operationDone = "sub"


def mulNum():
    global op1
    global operationDone
    op1 = int(myInput.get())
    clearField()
    operationDone = "mul"


def divNum():
    global op1
    global operationDone
    op1 = int(myInput.get())
    clearField()
    operationDone = "div"


number7 = Button(root, text="7", padx=40,  pady=20,
                 command=lambda m="7": putText(m))
number8 = Button(root, text="8", padx=40,  pady=20,
                 command=lambda m="8": putText(m))
number9 = Button(root, text="9", padx=40,  pady=20,
                 command=lambda m="9": putText(m))
number4 = Button(root, text="4", padx=40,  pady=20,
                 command=lambda m="4": putText(m))
number5 = Button(root, text="5", padx=40,  pady=20,
                 command=lambda m="5": putText(m))
number6 = Button(root, text="6", padx=40,  pady=20,
                 command=lambda m="6": putText(m))
number1 = Button(root, text="1", padx=40,  pady=20,
                 command=lambda m="1": putText(m))
number2 = Button(root, text="2", padx=40,  pady=20,
                 command=lambda m="2": putText(m))
number3 = Button(root, text="3", padx=40,  pady=20,
                 command=lambda m="3": putText(m))
number0 = Button(root, text="0", padx=40,  pady=20,
                 command=lambda m="0": putText(m))

clearBtn = Button(root, text="Clear", padx=78,  pady=20, command=clearField)
addBtn = Button(root, text="+", padx=39,  pady=20, command=addNum)
resultBtn = Button(root, text="=", padx=88,  pady=20, command=resultFunc)

mulBtn = Button(root, text="*", padx=40,  pady=20, command=mulNum)
subBtn = Button(root, text="-", padx=40,  pady=20, command=subNum)
divBtn = Button(root, text="/", padx=40,  pady=20, command=divNum)


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
clearBtn.grid(row=4, column=1, columnspan=2)


addBtn.grid(row=5, column=0)
resultBtn.grid(row=5, column=1, columnspan=2)

subBtn.grid(row=6, column=0)
mulBtn.grid(row=6, column=1)
divBtn.grid(row=6, column=2)


root.mainloop()
