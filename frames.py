from tkinter import *

root = Tk()
root.title("LEARNING frames")
myFrame = LabelFrame(root, text="First Frame", padx=40,
                     pady=50)  # INTERNAL PADDING

myFrame.pack(padx=80, pady=80)  # EXTERNAL PADDING

myBtn = Button(myFrame, text="Click HERE!")
label2 = Label(myFrame, text="IM A LABEL", anchor=E)

myBtn.grid(row=0, column=0, pady=20)
label2.grid(row=1, column=1, sticky=W+E)

root.mainloop()
