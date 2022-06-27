from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learning databases')
root.geometry("400x600")

# create a connect var by connecting the database
connVar = sqlite3.connect("address_book.db")

# create a cursor that points to the current row in db we are in
cur = connVar.cursor()

# create table using exectute on cursor
# We will use SQL lite3 commands inside
cur.execute(""" CREATE TABLE IF NOT EXISTS addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    zipcode integer
)""")

# Create submit function to save rec to database


def submit():

    # create a connect var by connecting the database
    connVar = sqlite3.connect("address_book.db")

    # create a cursor that points to the current row in db we are in
    cur = connVar.cursor()

    if f_name.get() != "":
        # insert into table
        cur.execute(
            "INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :zipCode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'zipCode': zipCode.get()
            }

        )

    # commit changes
    connVar.commit()

    # close connection
    connVar.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    zipCode.delete(0, END)

# Create show records function


def show_records():
    # create a connect var by connecting the database
    connVar = sqlite3.connect("address_book.db")

    # create a cursor that points to the current row in db we are in
    cur = connVar.cursor()

    # Query the database
    cur.execute("SELECT *,oid FROM addresses")
    records = cur.fetchall()

    # print(records)

    # loop and print
    printRec = ""

    for record in records:
        printRec += str(record[0]) + " " + str(record[1]) + " with address " + str(
            record[2]) + " in " + str(record[3]) + " " + str(record[4]) + "\t" + str(record[5])+"\n"
        queryLabel = Label(root, text=printRec)
        queryLabel.grid(row=12, column=0, columnspan=2)

    # commit changes
    connVar.commit()

    # close connection
    connVar.close()


def delete():
    # create a connect var by connecting the database
    connVar = sqlite3.connect("address_book.db")

    # create a cursor that points to the current row in db we are in
    cur = connVar.cursor()

    del_oid = selectOID.get()

    # delete a rec
    cur.execute("DELETE FROM addresses WHERE oid = " + str(del_oid))

    # commit changes
    connVar.commit()

    # close connection
    connVar.close()


def editRec(id):
    # create a connect var by connecting the database
    connVar = sqlite3.connect("address_book.db")

    # create a cursor that points to the current row in db we are in
    cur = connVar.cursor()

    # Edit the specified record
    cur.execute(""" UPDATE addresses SET
        first_name = :fname,
        last_name = :lname,
        address = :address,
        city = :city,
        zipcode = :zipCode
    WHERE oid =:oid  """,

                {'fname': f_name_update.get(),
                 'lname': l_name_update.get(),
                 'address': address_update.get(),
                 'city': city_update.get(),
                 'zipCode': zipCode_update.get(),
                 'oid': id})

    # commit changes
    connVar.commit()

    # close connection
    connVar.close()

    newWin.destroy()


def update():
    select_ID = selectOID.get()

    if select_ID != "":
        # create a connect var by connecting the database
        connVar = sqlite3.connect("address_book.db")

        # create a cursor that points to the current row in db we are in
        cur = connVar.cursor()

        cur.execute("SELECT * FROM addresses WHERE oid = " + str(select_ID))

        records = cur.fetchall()

        global newWin
        # Create a new Window
        newWin = Toplevel()
        newWin.title('Update a record')
        newWin.geometry("350x300")

        # create global vars for text box names
        global f_name_update
        global l_name_update
        global address_update
        global city_update
        global zipCode_update

        # Create text boxes
        f_name_update = Entry(newWin, width=30)
        f_name_update.grid(row=0, column=1, padx=10, pady=(10, 0))

        l_name_update = Entry(newWin, width=30)
        l_name_update.grid(row=1, column=1)

        address_update = Entry(newWin, width=30)
        address_update.grid(row=2, column=1)

        city_update = Entry(newWin, width=30)
        city_update.grid(row=3, column=1)

        zipCode_update = Entry(newWin, width=30)
        zipCode_update.grid(row=4, column=1)

        # create labels

        f_name_lab = Label(newWin, text="First Name")
        f_name_lab.grid(row=0, column=0, padx=10, pady=(10, 0))

        l_name_lab = Label(newWin, text="Last Name")
        l_name_lab.grid(row=1, column=0)

        address_lab = Label(newWin, text="Address")
        address_lab.grid(row=2, column=0)

        city_lab = Label(newWin, text="City")
        city_lab.grid(row=3, column=0)

        zipCode_lab = Label(newWin, text="Zip Code")
        zipCode_lab.grid(row=4, column=0)

        # Create submit button
        update_btn = Button(newWin, text="Update Record",
                            command=lambda: editRec(select_ID))
        update_btn.grid(row=5, column=0, columnspan=2,
                        pady=10, padx=10, ipadx=100)

        # Loop and fill boxes with existing record data
        for record in records:
            f_name_update.insert(0, record[0])
            l_name_update.insert(0, record[1])
            address_update.insert(0, record[2])
            city_update.insert(0, record[3])
            zipCode_update.insert(0, record[4])

        # commit changes
        connVar.commit()

        # close connection
        connVar.close()


# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=10, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

zipCode = Entry(root, width=30)
zipCode.grid(row=4, column=1)

selectOID = Entry(root, width=30)
selectOID.grid(row=9, column=1, pady=5)

# create labels

f_name_lab = Label(root, text="First Name")
f_name_lab.grid(row=0, column=0, padx=10, pady=(10, 0))

l_name_lab = Label(root, text="Last Name")
l_name_lab.grid(row=1, column=0)

address_lab = Label(root, text="Address")
address_lab.grid(row=2, column=0)

city_lab = Label(root, text="City")
city_lab.grid(row=3, column=0)

zipCode_lab = Label(root, text="Zip Code")
zipCode_lab.grid(row=4, column=0)

select_lab = Label(root, text="Select ID")
select_lab.grid(row=9, column=0, pady=5)

# Create submit button
submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Create a show records button
show_records_btn = Button(root, text="Show Records", command=show_records)
show_records_btn.grid(row=6, column=0, columnspan=2,
                      pady=10, padx=10, ipadx=127)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2,
                pady=10, padx=10, ipadx=127)

update_btn = Button(root, text="Update Record", command=update)
update_btn.grid(row=11, column=0, columnspan=2,
                pady=10, padx=10, ipadx=127)
# commit changes
connVar.commit()

# close connection
connVar.close()

root.mainloop()
