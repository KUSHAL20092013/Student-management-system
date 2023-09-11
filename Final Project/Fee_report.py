import tkinter
from tkinter import messagebox
from tkinter import *

def Fee_details():
    pg = Tk()
    pg.title("Student Profile")
    pg.geometry('1370x760')
    pg.configure(bg='light green')
    page4frame = Frame(pg, bg='light yellow', cursor='star')
    page4frame.grid(row=1, column=0)
    banner = Label(pg, text="Fee Report", bg='light green', fg='black', relief="groove", bd=10)
    banner.grid(row=0, column=0, padx=550, pady=50)
    infoframe = LabelFrame(page4frame, text="Information", bg='light yellow')
    infoframe.grid(row=0, column=0)
    innerframe1 = Frame(infoframe, bg='light yellow')
    innerframe1.grid(row=0, column=0)

    receipt = Label(innerframe1, text="Receipt No.: ")
    studentname = Label(innerframe1, text="Student Name: ")
    addnum = Label(innerframe1, text="Admission No.: ")
    date = Label(innerframe1, text="Date: ")
    branch = Label(innerframe1, text="Branch: ")
    
    receipt.grid(row=0, column=0, sticky=W)
    semester = Label(innerframe1, text="Semester: ")
    studentname.grid(row=1, column=0, sticky=W)
    addnum.grid(row=2, column=0, sticky=W)
    date.grid(row=3, column=0, sticky=W)
    branch.grid(row=4, column=0, sticky=W)
    semester.grid(row=5, column=0, sticky=W)
    

    receiptentry = Entry(innerframe1, font=("Arial", 16), bg="light yellow", fg="black")
    studentnameentry = Entry(innerframe1, font=("Arial", 16), bg="light yellow", fg="black")
    addnumentry = Entry(innerframe1, font=("Arial", 16), bg="light yellow", fg="black")
    dateentry = Entry(innerframe1, font=("Arial", 16), bg="light yellow", fg="black")
    y= StringVar()
    y.set("-Select Branch-")
    branchentry= OptionMenu(innerframe1, y,"Hyderabad", "Pune","Banglore","Delhi")
    x = StringVar()
    x.set('-Select Semester-')
    semesterentry = OptionMenu(innerframe1, x, "Semester 1", "Semester 2")

    receiptentry.grid(row=0, column=1, sticky=E)
    studentnameentry.grid(row=1, column=1, sticky=E)
    addnumentry.grid(row=2, column=1, sticky=E)
    dateentry.grid(row=3, column=1, sticky=E)
    branchentry.grid(row=4, column=1,sticky=E)
    semesterentry.grid(row=5, column=1, sticky=E)

    innerframe2 = Frame(infoframe, bg='light yellow')
    innerframe2.grid(row=0, column=1)

    totalamt = Label(innerframe2, text="TOTAL AMOUNT: ")
    paidamt = Label(innerframe2, text="PAID AMOUNT: ")
    balance = Label(innerframe2, text="BALANCE: ")

    totalamt.grid(row=0, column=0, sticky=W)
    paidamt.grid(row=1, column=0, sticky=W)
    balance.grid(row=2, column=0, sticky=W)

    totalamtentry = Entry(innerframe2, font=("Arial", 16), bg="light yellow", fg="black")
    paidamtentry = Entry(innerframe2, font=("Arial", 16), bg="light yellow", fg="black")
    balanceentry = Entry(innerframe2, font=("Arial", 16), bg="light yellow", fg="black")

    totalamtentry.grid(row=0, column=1, sticky=E)
    paidamtentry.grid(row=1, column=1, sticky=E)
    balanceentry.grid(row=2, column=1, sticky=E)

    feereceipt = LabelFrame(page4frame, text="Fee Receipt", relief=GROOVE, bd=10, bg="white")
    feereceipt.grid(row=0, column=1)
    frame2 = Frame(pg, bg="white", relief=GROOVE, bd=10)
    frame2.grid(row=2, column=0)

    buttonframe = tkinter.LabelFrame(pg, text="Options: ", bg='light yellow', fg="Black", cursor='star', bd=10, relief="groove")
    buttonframe.grid(row=3, column=0)
    save = tkinter.Button(buttonframe, text="Save", bg="light yellow", fg="black")
    display = tkinter.Button(buttonframe, text="Display", bg="light yellow", fg="black")
    reset = tkinter.Button(buttonframe, text="Reset", bg="light yellow", fg="black")
    update = tkinter.Button(buttonframe, text="Update", bg="light yellow", fg="black")
    delete = tkinter.Button(buttonframe, text="Delete", bg="light yellow", fg="black")
    search = tkinter.Button(buttonframe, text="Search", bg="light yellow", fg="black")
    exit = tkinter.Button(buttonframe, text="Exit", bg="light yellow", fg="black")

    save.grid(row=0, column=0)
    display.grid(row=0, column=1)
    reset.grid(row=0, column=2)
    update.grid(row=0, column=3)
    delete.grid(row=0, column=4)
    search.grid(row=0, column=5)
    exit.grid(row=0, column=6)

    pg.mainloop()