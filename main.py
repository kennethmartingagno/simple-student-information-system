from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

root = Tk()

root.title("SSIS")
root.geometry("1200x780")
frame = Frame(root, bg="#800000")
frame.place(x=0, y=0, width=1200, height=50)

header = Label(frame, text="Simple Student Information System", 
fg="#FFFFFF", bg="#800000", font=("Arial", 35, "bold"))
header.pack()

content = Frame(root, bg="#FFFFFF")
content.place(x=0, y=50, width=1200, height=400)

fname = Label(content, text="First Name:", fg="#000000", bg="#FFFFFF",
font=("Arial", 20, "bold"))
fname.place(x=20, y=0)

fentry = Entry(content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
fentry.place(x=20, y=40)

lname = Label(content, text="Last Name:", fg="#000000", bg="#FFFFFF",
font=("Arial", 20, "bold"))
lname.place(x=20, y=80)

lentry = Entry(content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
lentry.place(x=20, y=120)

idnumber = Label(content, text="ID Number:", fg="#000000", bg="#FFFFFF",
font=("Arial", 20, "bold"))
idnumber.place(x=20, y=160)

idnumberEntry = Entry(content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
idnumberEntry.place(x=20, y=200)

course = Label(content, text="Course:", fg="#000000", bg="#FFFFFF",
font=("Arial", 20, "bold"))
course.place(x=20, y=240)

courseEntry = Entry(content, font=("Arial", 18), bg="#FFFFFF", relief=RIDGE)
courseEntry.place(x=20, y=280)

year = Label(content, text="Year:", fg="#000000", bg="#FFFFFF",
font=("Arial", 20, "bold"))
year.pack()

i = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
yearEntry = ttk.Combobox(content, font=("Arial", 20), values=i)
yearEntry.pack()

gender = Label(content, text="Gender:", fg="#000000", bg="#FFFFFF",
font=("Arial", 20, "bold"))
gender.pack()

j = ["Male", "Female"]
genderEntry = ttk.Combobox(content, font=("Arial", 20), values=j)
genderEntry.pack()

def tree():
    with open("data.csv") as f:
        r = csv.DictReader(f, delimiter=",")
        for row in r:
            idnumber = row["idnumber"]
            first = row["first"]
            last = row["last"]
            course = row["course"]
            year = row["year"]
            gender = row["gender"]
            view.insert("", 0, values=(idnumber, first, last, course, year, gender))

def showall():
        view.delete(*view.get_children())
        tree()

def add():
        if fentry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif lentry.get() == "":
            messagebox.showerror("Error, All fields are required")
        elif idnumberEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif courseEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif yearEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif genderEntry.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            data = []
            data.append(idnumberEntry.get())
            data.append(fentry.get())
            data.append(lentry.get())
            data.append(courseEntry.get())
            data.append(yearEntry.get())
            data.append(genderEntry.get())

            with open("data.csv", "a", newline="") as f:
                w = csv.writer(f)
                w.writerow(data)
                view.insert("", 0,values=(data))

            fentry.delete(0, END)
            lentry.delete(0, END)
            idnumberEntry.delete(0, END)
            courseEntry.delete(0, END)
            yearEntry.delete(0, END)
            genderEntry.delete(0, END)

            showall()

def remove():
        selected = view.selection()
        values = view.item(selected, "values")
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
            view.delete(selected)
            showall()

def edit():
        fentry.delete(0, END)
        lentry.delete(0, END)
        idnumberEntry.delete(0, END),
        courseEntry.delete(0, END)
        yearEntry.delete(0, END)
        genderEntry.delete(0, END)

        selected = view.focus()
        values = view.item(selected, "values")

        remove()

        fentry.insert(0, values[0])
        lentry.insert(0, values[1])
        idnumberEntry.insert(0, values[2])
        courseEntry.insert(0, values[3])
        yearEntry.insert(0, values[4])
        genderEntry.insert(0, values[5])

def save():
        selected = view.focus()
        view.item(selected, text="", values=(fentry.get(),lentry.get(),idnumberEntry.get(), courseEntry.get(), yearEntry.get(),genderEntry.get()))
        add()

        fentry.delete(0, END)
        lentry.delete(0, END)
        idnumberEntry.delete(0, END)
        courseEntry.delete(0, END)
        yearEntry.delete(0, END)
        genderEntry.delete(0, END)

def search():
    query = searchBy.get()

    if query == "":
        messagebox.showerror("Error", "Enter Keyword")
    else:
        with open("data.csv", "r") as f:
            for row in f:
                if query in row:
                        view.delete(*view.get_children())
                        view.insert("", "end", values=(row.split(",")))

addButton = Button(content, text="Add", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=add)
addButton.place(x=1000, y=20)

deleteButton = Button(content, text="Delete", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=remove)
deleteButton.place(x=1000, y=100)

editButton = Button(content, text="Edit", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=edit)
editButton.place(x=1000, y=180)

saveButton = Button(content, text="Save", width=8, font=("Arial", 25, "bold"), fg="#FFFFFF", bg="#800000", command=save)
saveButton.place(x=1000, y=260)

subSearch = Frame(content, bg="#800000")
subSearch.place(x=0, y=340, width=1200, height=60)

displayButton = Button(subSearch, text="All", width=13, font=("Arial", 24, "bold"), fg="#000000", bg="#FFFFFF", command=showall)
displayButton.place(x=20)

searchBy = Entry(subSearch, font=("Arial", 25))
searchBy.place(x=760, height=50, width=210)

searchButton = Button(subSearch, text="Search", width=8, font=("Arial", 25, "bold"), fg="#000000", bg="#FFFFFF", command=search)
searchButton.place(x=1000)

searchContent = Frame(root, bg="#FFFFFF")
searchContent.place(x=0, y=450, width=1200, height=380)

scrollx = Scrollbar(searchContent)
scrollx.pack(side=RIGHT, fill=Y)

view = ttk.Treeview(searchContent, columns=(1,2,3,4,5,6), show="headings", height=10, yscrollcommand=scrollx.set)
style = ttk.Style()
style.configure("Treeview.Heading", foreground="#000000", font=("Arial", 10, "bold"))
style.map("Treeview", background=[("selected", "#800000")])

view.heading(1, text="ID Number")
view.heading(2, text="Frist Name")
view.heading(3, text="Last Name")
view.heading(4, text="Course")
view.heading(5, text="Year")
view.heading(6, text="Gender")

view.column(1, width=200, anchor=CENTER)
view.column(2, width=200, anchor=CENTER)
view.column(3, width=200, anchor=CENTER)
view.column(4, width=200, anchor=CENTER)
view.column(5, width=200, anchor=CENTER)
view.column(6, width=200, anchor=CENTER)

view.place(x=0, y=0, width=1185, height=330)
scrollx.config(command=view.yview)

tree()

root.mainloop()