from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("LEARNING SLIDERS")
root.iconbitmap("icon.ico")
root.geometry("700x500")


def updateWindow():
    myLabel = Label(root, text=str(horiSlider.get()) +
                    "x" + str(vertical.get())).pack()
    root.geometry(str(horiSlider.get()) +
                  "x" + str(vertical.get()))


vertical = Scale(root, from_=0, to=700, length=250,
                 bg="yellow", fg="red")
vertical.set(700)
horiSlider = Scale(root, from_=0, to=500, length=250, orient=HORIZONTAL)

vertical.pack(anchor=W)
horiSlider.pack(anchor=SE)

changeWindowSize = Button(root, text="Change window size",
                          padx=50, pady=70, command=updateWindow).pack()

root.mainloop()
