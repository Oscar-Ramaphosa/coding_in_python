#import all the neccesary modules
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
from tkinter import ttk

#creating a gui interface
root = Tk()
root.title("Fault Management")


#the database connection
conn = sq.connect('Faults.db')
c = conn.cursor()

#the first name label and the entry for the first name
firstNameLbl = Label(root,text= "Fist Name:").grid(row = 1, column=0)
NameEntry = Entry(root,width=40)
NameEntry.grid(row = 1, column=2, )

#the last name label and the entry for last name
lastNameLbl = Label(root,text= "Last Name:").grid(row = 2, column=0)
lastNameEntry = Entry(root,width=40)
lastNameEntry.grid(row = 2, column=2)

#the contact label and the entry for contact
contactLbl = Label(root, text= "Contact:").grid(row = 3, column=0)
contactEntry = Entry(root,width=40)
contactEntry.grid(row = 3, column=2)

#the apartment label and the entry for apartment
apartmentLbl = Label(root, text = "Apartment:").grid(row = 4, column=0)
apartmentEntry = Entry(root,width=40)
apartmentEntry.grid(row = 4, column=2)

#the date label and the entry for date
DateLbl = Label(root, text= "Report Date:").grid(row = 5, column=0)
dateEntry = Entry(root,width=40)
dateEntry.grid(row = 5, column=2)

#the Unit label and the entry for Unit
unitLbl = Label(root, text= "Unit:").grid(row=6, column=0)
unitEntry = Entry(root,width=40)
unitEntry.grid(row = 6, column=2)

#the gender label
genderLbl = Label(root,text = "Gender:").grid(row = 7, column= 0)

#the check button for the gender
gendercheck1 = Checkbutton(root,text ="Male")
gendercheck1.grid(row = 7, column=2)

#second check button for gender
gendercheck2 = Checkbutton (root,text ="Female")
gendercheck2.grid(row = 7, column=3)

#the fault label and the entry of the fault label
faultLbl = Label(root,text = "Fault").grid(row = 8, column = 0)
faultEntry = Entry(root,width=40, )
faultEntry.grid(  row = 8, column=2)

#creating a database table
c.execute("""CREATE TABLE IF NOT EXISTS FaultManagement(First_name TEXT,
                                                        Last_name TEXT,
                                                        Contact INTEGER,
                                                        Apartment TEXT,
                                                        Date DATE,
                                                        Unit INTEGER,
                                                        Fault TEXT)""")

def submit(): # the submit function

    #creating a connection to the database
    conn = sq.connect('Faults.db')
    c = conn.cursor()

    #getting all the entries from the database
    name = NameEntry.get()
    lastNam = lastNameEntry.get()
    cont = contactEntry.get()
    app = apartmentEntry.get()
    dat = dateEntry.get()
    uni = unitEntry.get()

    #an if statement that checks if the entry is empty or not
    if len(name) == 0:
        msg = 'name can\'t be empty'
    else:
        #the try and check exeption handle that vaidate the entries
        try:
            if any(ch.isdigit() for ch in name):
                messagebox.showerror("Error", "First Name can't be number.")
            elif any(l.isdigit() for l in lastNam):
                messagebox.showerror("Error", "Last name an not be a number.")
            elif any(c.isalpha() for c in cont):
                messagebox.showerror("Error", "Contacts can not be a alphabet.")
            elif any(a.isdigit() for a in app ):
                messagebox.showerror("Error", "Apartment can not be a number.")
            elif any(d.isalpha() for d in dat):
                messagebox.showerror("Error", "Date can not be alphabet.")
            elif any(u.isalpha() for u in uni):
                messagebox.showerror("Error", "Unit can not be an alphabet.")
            else:
                #insert the all the entries from the user if the are all valid
                c.execute("INSERT INTO FaultManagement VALUES(:First_name, :Last_name, :Contact, :Apartment,:Date, :Unit,:Fault)",
                    {
                        'First_name': NameEntry.get(),
                        'Last_name': lastNameEntry.get(),
                        'Contact': contactEntry.get(),
                        'Apartment': apartmentEntry.get(),
                        'Date': dateEntry.get(),
                        'Unit': unitEntry.get(),
                        'Fault': faultEntry.get()
                    })
                messagebox.showinfo("Add infor", "Your fault has been submitted")# a message box for entries entered
        except Exception as ep: #catching an exeption
            messagebox.showerror('error', "Please enter the invalid input")
    conn.commit()#database commit
    conn.close()#close the database

    # this empty the entry fields after the user clicks the submit button
    NameEntry.delete(0, END)
    lastNameEntry.delete(0, END)
    contactEntry.delete(0, END)
    apartmentEntry.delete(0, END)
    dateEntry.delete(0, END)
    unitEntry.delete(0, END)
    faultEntry.delete(0, END)


def listFaults():
    #creating the new page interface
    roo = Tk()
    roo.title("Fault Management")

    #creating the frame for the table to desplay all the entries entered by the user
    table_frame = Frame(roo)
    table_frame.pack()
    my_frame = ttk.Treeview(table_frame)

    #creating the column for frame
    my_frame['column'] = ("First_name", "Last_name", "Contact", "Apartment", "Date", "Unit", "Fault")
    my_frame.column("#0", width=0, stretch=NO)
    my_frame.column("First_name", anchor=CENTER, width=80)
    my_frame.column("Last_name", anchor=CENTER, width=80)
    my_frame.column("Contact", anchor=CENTER, width=80)
    my_frame.column("Apartment", anchor=CENTER, width=80)
    my_frame.column("Date", anchor=CENTER, width=80)
    my_frame.column("Unit", anchor=CENTER, width=80)
    my_frame.column("Fault", anchor=CENTER, width=80)

    # Creating all the heading on the table
    my_frame.heading("#0", text="", anchor=CENTER)
    my_frame.heading("First_name", text="Name", anchor=CENTER)
    my_frame.heading("Last_name", text="Last Name", anchor=CENTER)
    my_frame.heading("Contact", text="Contact", anchor=CENTER)
    my_frame.heading("Apartment", text="Apartment", anchor=CENTER)
    my_frame.heading("Date", text="Date", anchor=CENTER)
    my_frame.heading("Unit", text="Unit", anchor=CENTER)
    my_frame.heading("Fault", text="Fault", anchor=CENTER)
    my_frame.pack()


    conn = sq.connect('Faults.db')
    c = conn.cursor()
    count = 0

    # this select all the datas that are entered on the frame and print out the results
    c.execute("SELECT * FROM FaultManagement ")
    m= c.fetchall()

    # the for loop that place all the records
    for record in m:
        my_frame.insert(parent='', index='end', iid=str(count), text='', values=(record[0], record[1], record[2],
                                                                                 record[3], record[4], record[5],
                                                                                 record[6]))
        count += 1
    conn.commit() #database commit
    conn.close()#close the database

#the save button that saves the input from the user to the database
Submit_btn = Button(root, text = "Submit now", command = submit)
Submit_btn.grid(row = 12, column= 3)

#the submit button to view all the information entered by the user
list_btn = Button(root, text= "List faults", command= listFaults)
list_btn.grid(row = 12, column=2)

root.mainloop()