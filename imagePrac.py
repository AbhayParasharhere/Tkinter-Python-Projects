from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Testing Images in Widget")
root.iconbitmap('icon.ico')

myImg = ImageTk.PhotoImage(Image.open("myIMG.png"))
myLabel = Label(image=myImg)

myLabel.grid(row=0, column=0, columnspan=3)

myBtn = Button(root, text="EXIT!", bg="red",
               fg="white", command=root.quit, pady=5)

btn1 = Button(root, text="<<", command=root.quit)
btn2 = Button(root, text=">>", command=root.quit)


myBtn.grid(row=1, column=1)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=2)

root.mainloop()
