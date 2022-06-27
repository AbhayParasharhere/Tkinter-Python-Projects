from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("LEARNING Message Box")
root.iconbitmap("icon.ico")

# showinfo, showwarning, showerror, askyesno, askokcancel, askquestion


def showInfo():
    response = messagebox.showinfo(
        "This is the title IMP", "Hello there !")
    responseLabel = Label(root, text=str(response)).pack(anchor=W)


def showWarning():
    response = messagebox.showwarning(
        "This is the title IMP", "Hello there !")
    responseLabel = Label(root, text=str(response)).pack(anchor=W)


def showError():
    response = messagebox.showerror(
        "This is the title IMP", "Hello there !")
    responseLabel = Label(root, text=str(response)).pack(anchor=W)
    if response == 1:
        messagebox.showinfo("You clicked YES with value " +
                            str(response), str(response))
    else:
        messagebox.showinfo("You clicked NO with value " +
                            str(response), str(response))


def yesNo():
    response = messagebox.askyesno(
        "This is the title IMP", "Hello there !")
    responseLabel = Label(root, text=str(response)).pack(anchor=W)
    if response == 1:
        messagebox.showinfo("You clicked YES with value " +
                            str(response), str(response))
    else:
        messagebox.showinfo("You clicked NO with value " +
                            str(response), str(response))


def okCancel():
    response = messagebox.askretrycancel(
        "This is the title IMP", "Hello there !")
    responseLabel = Label(root, text=str(response)).pack(anchor=W)
    if response == 1:
        messagebox.showinfo("You clicked YES with value " +
                            str(response), str(response))
    else:
        messagebox.showinfo("You clicked NO with value " +
                            str(response), str(response))


def question():
    response = messagebox.askquestion(
        "This is the title IMP", "Hello there !")
    responseLabel = Label(root, text=str(response)).pack(anchor=W)
    if response == 1:
        messagebox.showinfo("You clicked YES with value " +
                            str(response), str(response))
    else:
        messagebox.showinfo("You clicked NO with value " +
                            str(response), str(response))


myInfo = Button(root, text="Show info", command=showInfo).pack()
myInfo = Button(root, text="Show warning", command=showWarning).pack()
myInfo = Button(root, text="Show error", command=showError).pack()
myInfo = Button(root, text="Show yes or no", command=yesNo).pack()
myInfo = Button(root, text="Show ok or cancel", command=okCancel).pack()
myInfo = Button(root, text="Show question", command=question).pack()


root.mainloop()
