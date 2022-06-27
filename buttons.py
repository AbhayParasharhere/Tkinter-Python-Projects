from tkinter import *

root = Tk()

rootSecond = Tk


def myFunc():
    label1 = Label(root, text="YAY Got a CLICK! LOL!", fg="blue")
    #label1.grid(row=1, column=1)
    label1.pack()


myButton = Button(root, text="LOL!", padx=20, pady=14,
                  command=myFunc, fg="purple", bg="yellow")

#myButton.grid(row=0, column=1)
myButton.pack()

root.mainloop()
