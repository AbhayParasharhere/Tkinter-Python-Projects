from tkinter import *

root = Tk()

rootSecond = Tk()

myEntryField = Entry(root, text="Enter your name", bg="white",
                     fg="purple", width=25, borderwidth=15)

myEntryField.insert(0, "Enter your full name: ")

myEntryField.pack()


def myFunc():
    label1 = Label(root, text="OH HELLO " +
                   myEntryField.get(), fg="blue")
    #label1.grid(row=1, column=1)
    label1.pack()


myButton = Button(root, text="LOL!", padx=20, pady=14,
                  command=myFunc, fg="purple", bg="yellow")

#myButton.grid(row=0, column=1)
myButton.pack()

root.mainloop()
