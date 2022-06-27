from tkinter import *

root = Tk()
root.title("Learning Radio Buttons using loop")
root.iconbitmap("icon.ico")

keyVal = StringVar()
keyVal.set("Luffy")


def displayKey():
    resKey = Label(root, text=keyVal.get()).pack()


ITEMS = [("Pythagoras", "Theorem"),
         ("Perpendicular", "line"),
         ("Monkey D", "Luffy"),
         ("Vinsmoke", "Sanji")]

for fName, LName in ITEMS:
    Radiobutton(root, text=fName, variable=keyVal, value=LName).pack(anchor=W)

displayButton = Button(root, text="REVEAL!", command=displayKey).pack()

root.mainloop()
