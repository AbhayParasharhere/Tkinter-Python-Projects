from tkinter import *

root = Tk()
root.title("Learning CheckBoxes")
root.iconbitmap("icon.ico")

myVal = StringVar()


def reveal():
    mylab = Label(root, text=str(myVal.get())).pack()


check1 = Checkbutton(root, text="CHECK QUEST", variable=myVal,
                     onvalue="Sike", offvalue="Wrong Number")
check1.deselect()
check1.pack()

checkButton = Button(root, text="Reveal answer", command=reveal).pack()

root.mainloop()
