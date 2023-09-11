import tkinter
import importlib
from tkinter import messagebox
from Fee_report import Fee_details
from Student_profile import student_details
def page2():
    root = tkinter.Tk()
    root.title("Home Page")
    root.geometry('1370x760')
    root.configure(bg='light yellow')

    studenttitle = tkinter.Label(root, text="Student Management System", bg='blue', fg="white", font=("Arial", 30), relief='groove', bd=10)
    studenttitle.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
    
    def studentpropage():
        messagebox.showinfo(title="loading...", message="Transferring...")
        root.destroy()
        student_details()
    def Feereppage():
        messagebox.showinfo(title="loading...", message="Transferring...")
        root.destroy()
        Fee_details()

    page2frame = tkinter.Frame(root, bg='light yellow', cursor='star')
    page2frame.grid(row=1, column=1)
    page2frame.grid(padx=500, pady=100)
    studentpro = tkinter.Button(page2frame, text="Student Profile", bg='blue', font=("Arial", 30), relief="groove", bd=10, command=studentpropage)
    studentpro.pack()
    # studentpro.grid(row=1, column=0, sticky='w', padx=(500), pady=(200))

    Feerep = tkinter.Button(page2frame, text="Fee report", bg='blue', font=("Arial", 30), relief="groove", bd=10, command=Feereppage)
    Feerep.pack(pady=50)
    # Feerep.grid(row=2, column=0, padx=500)
    
    root.mainloop
