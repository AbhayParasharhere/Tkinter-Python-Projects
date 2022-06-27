from tkinter import *

root = Tk()
root.title("Learning dropdown")
root.geometry("800x800")

weekDays = ["Mon", "Tue", "Wed", "thur"]

clicked = StringVar()
clicked.set(weekDays[0])


def show():
    myLabel = Label(root, text=str(clicked.get())).pack()

# Without a py list
#dropBox = OptionMenu(root, clicked, "Mon", "Tue", "Wed", "thur").pack()


# With a py list
dropBox = OptionMenu(root, clicked, *weekDays).pack()

showButton = Button(root, text="SHOW SELECTION", command=show).pack(anchor=W)

root.mainloop()
