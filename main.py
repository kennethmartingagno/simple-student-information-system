from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

root = Tk()

class Main():
    def __init__(self):
        self.root = root
        self.root.title("SSIS")
        self.root.geometry("1200x780")
        self.frame = Frame(self.root, bg="#800000")
        self.frame.place(x=0, y=0, width=1200, height=50)

        self.header = Label(self.frame, text="Simple Student Information System", 
        fg="#FFFFFF", bg="#800000", font=("Arial", 35, "bold"))
        self.header.pack()

        self.content = Frame(self.root, bg="#FFFFFF")
        self.content.place(x=0, y=50, width=1200, height=400)

        self.fname = Label(self.content, text="First Name:", fg="#000000", bg="#FFFFFF",
        font=("Arial", 20, "bold"))
        self.fname.place(x=20, y=0)

        self.fentry = Entry(self.content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
        self.fentry.place(x=20, y=40)

        self.lname = Label(self.content, text="Last Name:", fg="#000000", bg="#FFFFFF",
        font=("Arial", 20, "bold"))
        self.lname.place(x=20, y=80)

        self.lentry = Entry(self.content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
        self.lentry.place(x=20, y=120)

        self.idnumber = Label(self.content, text="ID Number:", fg="#000000", bg="#FFFFFF",
        font=("Arial", 20, "bold"))
        self.idnumber.place(x=20, y=160)

        self.idnumberEntry = Entry(self.content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
        self.idnumberEntry.place(x=20, y=200)

        self.course = Label(self.content, text="Course:", fg="#000000", bg="#FFFFFF",
        font=("Arial", 20, "bold"))
        self.course.place(x=20, y=240)

        self.courseEntry = Entry(self.content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
        self.courseEntry.place(x=20, y=280)

        self.year = Label(self.content, text="Year:", fg="#000000", bg="#FFFFFF",
        font=("Arial", 20, "bold"))
        self.year.pack()

        i = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        self.yearEntry = ttk.Combobox(self.content, font=("Arial", 20), values=i)
        self.yearEntry.pack()

        self.gender = Label(self.content, text="Gender:", fg="#000000", bg="#FFFFFF",
        font=("Arial", 20, "bold"))
        self.gender.pack()

        j = ["Male", "Female"]
        self.genderEntry = ttk.Combobox(self.content, font=("Arial", 20), values=j)
        self.genderEntry.pack()

        self.addButton = Button(self.content, text="Add", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=lambda:self.add())
        self.addButton.place(x=1000, y=20)

        self.deleteButton = Button(self.content, text="Delete", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=lambda:self.remove())
        self.deleteButton.place(x=1000, y=100)

        self.editButton = Button(self.content, text="Edit", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=lambda:self.edit())
        self.editButton.place(x=1000, y=180)

        self.saveButton = Button(self.content, text="Save", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=lambda:self.save())
        self.saveButton.place(x=1000, y=260)

        self.searchContent = Frame(self.root, bg="#FFFFFF")
        self.searchContent.place(x=0, y=380, width=1200, height=380)

        self.subSearch = Frame(self.searchContent, bg="#800000")
        self.subSearch.place(x=0, y=0, width=1200, height=50)

        self.displayButton = Button(self.subSearch, text="All", width=13, font=("Arial", 24, "bold"), fg="#000000", bg="#FFFFFF", command=lambda:self.showall())
        self.displayButton.place(x=20)

        self.searchBy = Entry(self.subSearch, font=("Arial", 25))
        self.searchBy.place(x=760, height=50, width=210)

        self.searchButton = Button(self.subSearch, text="Search", width=8, font=("Arial", 25, "bold"), fg="#000000", bg="#FFFFFF", command=lambda:self.search())
        self.searchButton.place(x=1000)

        self.scrollx = ttk.Scrollbar(self.searchContent, orient=VERTICAL)
        self.view = ttk.Treeview(self.searchContent, columns=(1,2,3,4,5,6), show="headings", height=10, xscrollcommand=self.scrollx.set)
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", foreground="#000000", font=("Arial", 10, "bold"))
        self.style.map("Treeview", background=[("selected", "#800000")])

        self.view.heading(1, text="ID Number")
        self.view.heading(2, text="Frist Name")
        self.view.heading(3, text="Last Name")
        self.view.heading(4, text="Course")
        self.view.heading(5, text="Year")
        self.view.heading(6, text="Gender")

        self.view.column(1, width=200, anchor=CENTER)
        self.view.column(2, width=200, anchor=CENTER)
        self.view.column(3, width=200, anchor=CENTER)
        self.view.column(4, width=200, anchor=CENTER)
        self.view.column(5, width=200, anchor=CENTER)
        self.view.column(6, width=200, anchor=CENTER)

        self.view.place(x=0, y=50, width=1200, height=330)
        self.tree()

    def tree(self):
        with open("data.csv") as f:
            r = csv.DictReader(f, delimiter=",")
            for row in r:
                idnumber = row["idnumber"]
                first = row["first"]
                last = row["last"]
                course = row["course"]
                year = row["year"]
                gender = row["gender"]
                self.view.insert("", 0, values=(idnumber, first, last, course, year, gender))

    def add(self):
        if self.fentry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.lentry.get() == "":
            messagebox.showerror("Error, All fields are required")
        elif self.idnumberEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.courseEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.yearEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.genderEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            self.data = []
            self.data.append(self.idnumberEntry.get())
            self.data.append(self.fentry.get())
            self.data.append(self.lentry.get())
            self.data.append(self.courseEntry.get())
            self.data.append(self.yearEntry.get())
            self.data.append(self.genderEntry.get())

            with open("data.csv", "a", newline="") as f:
                w = csv.writer(f)
                w.writerow(self.data)
                self.view.insert("", 0,values=(self.data))

            self.fentry.delete(0, END)
            self.lentry.delete(0, END)
            self.idnumberEntry.delete(0, END)
            self.courseEntry.delete(0, END)
            self.yearEntry.delete(0, END)
            self.genderEntry.delete(0, END)

            self.showall()

    def remove(self):
        selected = self.view.selection()
        values = self.view.item(selected, "values")
        query = values[0]

        if bool(query) is False:
            pass
        else:
            data = open("data.csv", "r").readlines()
            with open("data.csv", "w") as csv_file:
                for row in data:
                    if query in row:
                        pass
                    else:
                        csv_file.write(f"{row}")            
            self.view.delete(selected)
            self.showall()

    def edit(self):
        self.fentry.delete(0, END)
        self.lentry.delete(0, END)
        self.idnumberEntry.delete(0, END),
        self.courseEntry.delete(0, END)
        self.yearEntry.delete(0, END)
        self.genderEntry.delete(0, END)

        selected = self.view.focus()
        values = self.view.item(selected, "values")

        self.fentry.insert(0, values[0])
        self.lentry.insert(0, values[1])
        self.idnumberEntry.insert(0, values[2])
        self.courseEntry.insert(0, values[3])
        self.yearEntry.insert(0, values[4])
        self.genderEntry.insert(0, values[5])

    def save(self):
        selected = self.view.focus()

        self.view.item(selected, text="", values=(self.fentry.get(),self.lentry.get(),self.idnumberEntry.get(), self.courseEntry.get(), self.yearEntry.get(),self.genderEntry.get()))

        self.fentry.delete(0, END)
        self.lentry.delete(0, END)
        self.idnumberEntry.delete(0, END)
        self.courseEntry.delete(0, END)
        self.yearEntry.delete(0, END)
        self.genderEntry.delete(0, END)

        self.showall()
    def search(self):
        query = self.searchBy.get()

        if query == "":
            messagebox.showerror("Error", "Enter Keyword")
        else:
            with open("data.csv", "r") as f:
                for row in f:
                    if query in row:
                            self.view.delete(*self.view.get_children())
                            self.view.insert("", "end", values=(row.split(",")))

    def showall(self):
        self.view.delete(*self.view.get_children())
        self.tree()

run = Main()
root.mainloop()