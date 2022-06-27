from cProfile import label
from cgitb import text
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

i = 0  # current index

# Fetching al images
img1 = ImageTk.PhotoImage(Image.open("img/a (1).png"))
img2 = ImageTk.PhotoImage(Image.open("img/a (2).png"))
img3 = ImageTk.PhotoImage(Image.open("img/a (3).png"))
img4 = ImageTk.PhotoImage(Image.open("img/a (4).png"))
img5 = ImageTk.PhotoImage(Image.open("img/a (5).png"))

images = [img1, img2, img3, img4, img5]

# fx to forward images

status_label = Label(root, text="Image 1 of " +
                     str(len(images)), bd=1, relief=SUNKEN, anchor=E)
status_label.grid(row=2, column=0, columnspan=3, sticky=E+W)


def goForward():
    global status_label
    global i
    i = i + 1

    if i >= len(images):
        i = 0

    status_label.grid_forget()
    status_label = Label(root, text="Image " +
                         str(i+1) + " of "+str(len(images)), bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=E+W)

    global imgHolder
    # imgHolder.destroy()
    imgHolder.grid_forget()
    imgHolder = Label(image=images[i], height=images[i].height() - 300)
    imgHolder.grid(row=0, column=0, columnspan=3)


def goBackward():
    global status_label
    global i
    i = i - 1

    if i < 0:
        i = 4

    status_label.grid_forget()
    status_label = Label(root, text="Image " +
                         str(i+1) + " of "+str(len(images)), bd=1, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=E+W)

    global imgHolder
    # imgHolder.destroy()
    imgHolder.grid_forget()
    imgHolder = Label(image=images[i], height=images[i].height() - 300)
    imgHolder.grid(row=0, column=0, columnspan=3)


imgHolder = Label(image=images[0], height=img1.height() - 300)

forwardBtn = Button(root, text=">>", command=goForward)
exitBtn = Button(root, text="Exit Here!", command=root.quit)
backBtn = Button(root, text="<<", command=goBackward)

# Place widgets
imgHolder.grid(row=0, column=0, columnspan=3)
backBtn.grid(row=1, column=0)
exitBtn.grid(row=1, column=1)
forwardBtn.grid(row=1, column=2, pady=10)


root.mainloop()
