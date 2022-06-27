from tkinter import *

root = Tk()
root.title("Learning Radio Buttons")
root.iconbitmap("icon.ico")

learnSeq = IntVar()
# learnSeq.set(4)


def updateLabel(val):
    global valueCheck
    # valueCheck.destroy()
    valueCheck = Label(root, text=str(val)).pack()


Radiobutton(root, text=("C++"), variable=learnSeq, value=1,
            command=lambda: updateLabel(learnSeq.get())).pack()
Radiobutton(root, text=("JS"), variable=learnSeq, value=2,
            command=lambda: updateLabel(learnSeq.get())).pack()

valueCheck = Label(root, text=str(learnSeq.get())).pack()

root.mainloop()
