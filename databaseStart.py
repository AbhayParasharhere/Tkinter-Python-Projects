from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learning databases')
root.geometry("400x400")

# create a connect var by connecting the database
connVar = sqlite3.connect("address_book.db")

# create a cursor that points to the current row in db we are in
cur = connVar.cursor()

# create table using exectute on cursor
# We will use SQL lite3 commands inside
cur.execute(""" CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    zipcode integer
)""")

# commit changes
connVar.commit()

# close connection
connVar.close()

root.mainloop()
