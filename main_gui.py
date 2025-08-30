import tkinter as tk
from tkinter import simpledialog, messagebox
from storage import save_student, load_students, search_student, delete_student
from student import student


# ---------- Functions ----------
def data_entry():
    name = simpledialog.askstring("Data Entry", "Enter Student Name:")
    if not name:  # cancel ya blank hua toh return
        return

    age = simpledialog.askstring("Data Entry", "Enter Student Age:")
    if not age:
        return

    s1 = student(name, age)
    save_student(s1)
    messagebox.showinfo("Success", f"Student '{name}' saved successfully!")


def display_students():
    students = load_students()
    if not students:
        messagebox.showinfo("Info", "No Students Found In Storage!")
    else:
        # yaha students ek list of strings hai
        data = "\n".join(str(s) for s in students)
        messagebox.showinfo("Students in Storage", data)


def search_students():
    name = simpledialog.askstring("Search", "Enter Name to Search:")
    if not name:
        return
    result = search_student(name)
    messagebox.showinfo("Search Result", result)


def delete_students():
    name = simpledialog.askstring("Delete", "Enter Name to Delete:")
    if not name:
        return
    result = delete_student(name)
    messagebox.showinfo("Delete Result", result)


def exit_program():
    root.destroy()


# ---------- Main Window ----------
root = tk.Tk()
root.title("Student Management System")
root.geometry("350x300")

tk.Label(root, text="Choose an Option", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="1. Data Entry", width=25, command=data_entry).pack(pady=5)
tk.Button(root, text="2. Display Students", width=25, command=display_students).pack(pady=5)
tk.Button(root, text="3. Search Student", width=25, command=search_students).pack(pady=5)
tk.Button(root, text="4. Delete Student", width=25, command=delete_students).pack(pady=5)
tk.Button(root, text="5. Exit", width=25, command=exit_program, bg="red", fg="white").pack(pady=10)

root.mainloop()
