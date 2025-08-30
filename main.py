from storage import save_student, load_students, search_student, delete_student
from student import student
def menu():
    while True:
        print('''
    1. Press 1 for Data Entry          
    2. Press 2 for Display
    3. Press 3 for Search
    4. Press 4 for Delete 
    5. Press 5 for Exit
                        ''' )
        choice = input("Enter Your Choice:")
        if choice == "1":
            name = input("Enter Name Of Student:")
            age = input("Enter Age Of Student:")
            s1 = student(name,age)
            save_student(s1)
            print("Student Saved Successfully!")
        elif choice == "2":
            students = load_students()
            if not students:     #empty list
                print("No Students Found In Storage!")
            else:
                print("Students in Storage:")
                for s in students:
                    print(s)
        elif choice == "3":
            name = input("Enter Name To Search:")
            print(search_student(name))
        elif choice == "4":
            name = input("Enter Name To Delete:")
            print(delete_student(name))
        elif choice == "5":
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice, please try again.")

menu()

        
        






