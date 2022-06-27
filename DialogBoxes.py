from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("LEARNING DIALOG BOXES")
root.iconbitmap("icon.ico")


def getImg():
    global newLevel
    global reqImage
    newLevel = Toplevel()
    imgLocation = filedialog.askopenfilename(
        initialdir="C:\pythonProjects\Tkinter\img", filetypes=(("PNG images", "*.png"), ("JPG Pics", "*.jpg"), ("All files", "*.*")), title="Opening your image")
    reqImage = ImageTk.PhotoImage(Image.open(str(imgLocation)))
    reqImgPlaceHolder = Label(newLevel, image=reqImage).pack()


chooseImg = Button(root, text="Open any Image",
                   command=getImg, padx=50, pady=50).pack()
# closeImg = Button(root, text="CLose Window",
#                   command=newLevel.destroy, padx=50, pady=50).pack()
root.mainloop()
