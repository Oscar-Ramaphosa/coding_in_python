#import all the modules
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
from tkinter import ttk
import re

#database connection
con= sq.connect('Contact.db')
c = con.cursor()

#creating a Gui Tkinter
window = Tk()
window.title("Contact List")

#creating a table on the database
c.execute("""CREATE TABLE IF NOT EXISTS ContactTable(First_name TEXT,
                                                     Last_name TEXT,
                                                     Gender TEXT,
                                                     Age INTEGER,
                                                     Address TEXT,
                                                     Contact INTEGER )""")

#all the labes that are on the GUi

title2ldb = Label(window, text="Adding New Contacts.").grid(row = 0, column=2 ) #label for tittle
first_nameLbl = Label(window, text= "First Name: ").grid(row = 1, column= 0 ) #label for first name
last_namelbl = Label(window, text = "Last Name: ").grid(row= 2 , column=0) #label for last name
genderLbl = Label(window,text = "Gender: ").grid(row= 3, column=0) #label for Gender
ageLbl = Label(window, text = "Age: ").grid(row = 4, column=0) #label for Age
AdressLbl = Label(window, text = "Adress: ").grid(row = 5, column=0) #label for Address
contactLbl = Label(window, text="Contact: ").grid (row = 6,column=0) #label for Contact

#the first name entry
first_name = Entry(window, width= 40)
first_name.grid(row= 1, column=2)

#the entry for last name
last_name = Entry(window, width= 40)
last_name.grid(row= 2, column=2)

#the entry for gender
gender = Entry(window, width= 40)
gender.grid(row= 3, column=2)

#entry for age
age = Entry(window, width= 40)
age.grid(row= 4, column=2)

#entry for address
address = Entry(window, width=40)
address.grid(row = 5, column=2)

#entry for contact
contact = Entry(window, width= 40)
contact.grid(row= 6, column=2)



def save(): #a function for that save entry

    #the connection to the database
    con = sq.connect('Contact.db')
    c = con.cursor()

    nextPage = Tk() #creating an interface for the new page
    nextPage.title("Fault Management")

    #the Label for the new page
    titlelbl = Label(nextPage, text = "Contact Management System.").grid(row= 0, column= 0)
    addnewBtn = Button(nextPage, command=lambda: nextPage.destroy(), text="+ Add New")# a button that destroy a new page
    addnewBtn.grid(row=1, column=0)

    #inserting data in the contact table
    c.execute("INSERT INTO ContactTable VALUES(:First_name, :Last_name, :Gender, :Age, :Address, :Contact)",
              {
                  'First_name': first_name.get(),
                  'Last_name': last_name.get(),
                  'Gender': gender.get(),
                  'Age': age.get(),
                  'Address': address.get(),
                  'Contact': contact.get(),
              })

    #creating a table frame that print out all the data entered
    table = Frame(nextPage)
    table.grid()
    frame = ttk.Treeview(table)

    #creating the column for frame
    frame['column'] = ("First_name", "Last_name", "Gender", "Age", "Address", "Contact")
    frame.column("#0", width=0, stretch=NO)
    frame.column("First_name", anchor=CENTER, width=80)
    frame.column("Last_name", anchor=CENTER, width=80)
    frame.column("Gender", anchor=CENTER, width=80)
    frame.column("Age", anchor=CENTER, width=80)
    frame.column("Address", anchor=CENTER, width=80)
    frame.column("Contact", anchor=CENTER, width=80)

    #Creating all the heading on the table
    frame.heading("#0", text="", anchor=CENTER)
    frame.heading("First_name", text="Name", anchor=CENTER)
    frame.heading("Last_name", text="Last Name", anchor=CENTER)
    frame.heading("Gender", text="Gender", anchor=CENTER)
    frame.heading("Age", text="Age", anchor=CENTER)
    frame.heading("Address", text="Address", anchor=CENTER)
    frame.heading("Contact", text="Contact", anchor=CENTER)
    frame.pack()

    count = 0

    #this select all the datas that are entered on the frame and print out the results
    c.execute("SELECT * FROM ContactTable")
    i = c.fetchall()
    #the for loop that place all the records
    for record in i:
        frame.insert(parent='', index='end', iid=str(count), text='', values=(record[0], record[1], record[2],
                                                                              record[3], record[4], record[5],))
        count += 1

    con.commit()
    con.close()

    #this empty the entry fields after the user clicks the submit button
    first_name.delete(0, END)
    last_name.delete(0, END)
    gender.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    contact.delete(0, END)

    #Creating the delete button
    deletebtn = Button(nextPage,command = delete, text="Delete")
    deletebtn.grid(row=1, column=2,)

def delete(): #the delete function that delete a field

    delPage = Tk()#Creating a new page for the delete function
    delPage.title("Delete Record.")#the tittle for the new page

    #all the labels that are on the new page
    titlelb = Label(delPage, text="Contact Management System.").grid(row=0, column=0)
    labelDel = Label(delPage,text="Enter the contact number of the person you want to delete")
    labelDel.grid(row=1, column=0)

    #the entry where a user will enter the contact number for the field to delete
    delEntry = Entry(delPage,width=40)
    delEntry.grid(row = 2 , column= 0)


    def deleted():# the new function that completely delete records
        con = sq.connect('Contact.db')
        c = con.cursor()

        #an if statement for the entry that is equal to the contact
        if delEntry == contact:
            c.execute("DELETE FROM ContactTable WHERE Contact = " + str(delEntry))#delete from the table
            con.commit()
        messagebox.showinfo("Deleted", "Record deleted")# the message box that show that the entry is deleted

    #a submiting button to delete
    buttonSubmit = Button(delPage, text="Submit", command=deleted)
    buttonSubmit.grid(row=3, column=0)

#the save button that saves the input from the user to the database
saveBtn = Button(window , text = "Save", command= save)
saveBtn.grid(row= 7 , column=2)


window.mainloop()
