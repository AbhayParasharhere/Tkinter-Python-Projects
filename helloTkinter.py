from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World")

my2Label = Label(root, text="HEY Tkinter")

# Pack and grid arefor positioning our widget
# myLabel.pack()
# my2Label.pack()

myLabel.grid(row=0, column=0)

my2Label.grid(row=1, column=1)

# This is relative so this have the same effect
# myLabel.grid(row=0, column=3)


root.mainloop()
