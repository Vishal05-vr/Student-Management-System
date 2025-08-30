from student import student
import os
import pickle

file_name = "student.pkl"

def save_student(s):
    students = []
    # Agar file exist karti hai to purane students load kar lo
    if os.path.exists(file_name):
        with open(file_name,"rb") as f:
            students = pickle.load(f)   #load means READ
    students.append(s)
    # Ab updated list ko wapas file me save karo
    with open(file_name,"wb") as f:  
        pickle.dump(students,f)     #dump means WRITE

# s1 = student("Vish",22)
# s2 = student("Raj",45)
# save_student(s1)
# save_student(s2)

def load_students():
    if os.path.exists(file_name):
        with open(file_name,"rb") as f:
            data = pickle.load(f)
            if len(data) == 0:
                return []    # empty list 
            return[student.display() for student in data]
    else:
        return[]
    
# print("Students in storage: ")
# print(load_students())

def search_student(name):
    if os.path.exists(file_name):
        with open(file_name,"rb") as f:
            students = pickle.load(f)
            for student in students:
                if student.name.strip().lower() == name.strip().lower():
                    return student.display()
    return "Student Not Found!"

def delete_student(name):
    if os.path.exists(file_name):
        with open(file_name,"rb") as f:
            students = pickle.load(f)
        
        #clean name
        name = name.strip().lower()
        new_students = [student for student in students if student.name.strip().lower() != name]

        with open(file_name, "wb") as f:
            pickle.dump(new_students, f)

        if len(new_students) < len(students):
            return f"Student '{name.title()}' deleted successfully!"
        else:
            return f"Student '{name.title()}' not found!"
    else:
        return "No student records found!"
               



 