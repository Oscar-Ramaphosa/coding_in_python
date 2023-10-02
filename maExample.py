
from tkinter import *
import sqlite3 as sq

window = Tk()
window.title("COVRI Training")
window.geometry('750×550')
header = Label(window, text='Available courses', font=('arial' ,30 ,'bold'), fg='goldenrod').pack()

L1 = Label(window, text = "Select Course", font=('arial', 18)).place(x=10 ,y=100)
L2 = Label(window, text = "Duration(months)", font=("arial" ,18)).place(x=10 ,y=150)
L3 = Label(window, text = "Want Projects(Y/N) ?", font=("arial" ,18)).place(x=10 ,y=200)

planguages = {'Python', 'Java', 'PHP' ,'Javascript'}
lvar = StringVar(window)
lvar .set('Plea')

langd= OptionMenu(window, lvar, *planguages)
langd.place(x=220 ,y=105)

duration = StringVar(window)
wpro = StringVar(window)

durationT = Entry(window, textvariable=duration)
durationT.place(x=220 ,y=155)

wproT = Entry(window, textvariable=wpro)
wproT.place(x=220 ,y=205)

con = sq.connect('mycourses.db')
c = con.cursor()

def get():

    c.execute('CREATE TABLE IF NOT EXISTS ' +lvar.get() + ' (Duration INTEGER, PROJECTS TEXT)')  # SQL syntax
    c.execute('INSERT INTO ' + lvar.get() + ' (Duration, PROJECTS) VALUES (?, ?)',
              (duration.get(), wpro.get()))  # Insert record into database.
    con.commit()
    lvar.set('—-')
    duration.set('')
    wpro.set('')


button_1 = Button(window, text='Submit', command=get)
button_1.place(x=100, y=300)


def clear():
    lvar.set('—-')
    #    compdb.set('—-')

    duration.set('')
    wpro.set("")


button_2 = Button(window, text='Clear', command=clear)
button_2.place(x=10, y=300)


def record():
    c.execute('SELECT * FROM ' + lvar.get())  # Select from which ever language is selected'''

    frame = Frame(window)
    frame.place(x=400, y=150)

    Lb = Listbox(frame, height=8, width=25, font=('arial', 12))
    Lb.pack(side=LEFT, fill=Y)

    scroll = Scrollbar(frame, orient=VERTICAL)
    scroll.config(command=Lb.yview)
    scroll.pack(side=RIGHT, fill=Y)
    Lb.config(yscrollcommand=scroll.set)
    Lb.insert(0, 'Duration, Projects')

    data = c.fetchall()

    for row in data:
        Lb.insert(1, row)  # Inserts record row by row in list box
        L4 = Label(window, text=lvar.get() + '      ', font=('arial', 16)).place(x=400, y=100)
        L5 = Label(window, text='Details for selected course', font=('arial', 16)).place(x=400, y=350)
        con.commit()


button_3 = Button(window, text='View', command=record)
button_3.place(x=10, y=350)
window.mainloop()
