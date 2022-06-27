from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("This is the main window")
root.iconbitmap("icon.ico")


def crWindow():
    global myImg
    newWindow = Toplevel()
    myLabel1 = Label(root, text="You created a new window").pack()
    myLabel2 = Label(newWindow, text="WOW THIS IS THE NEW WINDOW").pack()
    newWindow.title("2ND WIndow")

    closeWindow = Button(newWindow, text="CLOSE WINDOW",
                         command=newWindow.destroy).pack()

    myFrame = LabelFrame(newWindow, text="SampleFrame", padx=40, pady=40)
    myFrame.pack(padx=80, pady=80)

    myImg = ImageTk.PhotoImage(Image.open("img/a (3).png"))
    myIMG = Label(myFrame, image=myImg).pack()


createWindow = Button(root, text="CREATE WINDOW", command=crWindow).pack()


root.mainloop()
