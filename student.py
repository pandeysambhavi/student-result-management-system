from utils import calculate_result, calculate_grade
from data_handler import load_students, save_students

students = load_students()

def add_student():                                      #1 Add Student
    print()
    print("----------Add Student----------")
    print()

    # Name validation
    while True:
                name = input("Enter Student Name: ")
                if name.strip() == "":
                    print("Name cannot be empty")
                elif not name.replace(" ", "").isalpha():
                    print("Name must contain letters only.")
                else:
                    break
    
    # Rollno validation
    while True:
        rollno = input("Enter Roll No: ")
        if rollno.strip() == "":
            print("Roll number cannot be empty")

        elif not rollno.isdigit():
            print("Rollno must contain numbers only.")

        elif any(student["rollno"] == rollno for student in students):
            print("Roll number already exist. Please enter a different roll number.")
            print()
        else:
            break
    
    # Marks validation
    while True:
        try:
            marks = int(input("Enter Marks: "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    # Calculate Result & Grade

    result = calculate_result(marks)
    grade = calculate_grade(marks)
    print()

    student = {                             #Dictionary
            "name": name, 
            "rollno": rollno, 
            "marks": marks, 
            "result": result, 
            "grade": grade
    }
    students.append(student)
    save_students(students)

    print("Data saved Successfully.")
    print("Student added Successfully!")
    print()

def display_student():                                   #2 Display Result
         
    print()
    print("----------Student Result----------")
    print()

    for student in students:
        print("Name    :", student["name"])
        print("Roll No :", student["rollno"])
        print("Marks   :", student["marks"])
        print("Result  :", student["result"])
        print("Grade   :", student["grade"])
        print()

def search_student():                                     #3 Search Student

    print()
    print("----------Search Student----------")
    print()
    while True:
        search_rollno = input("Enter Roll No of Student to Search: ")
        if search_rollno.strip() == "":
            print("Roll number cannot be empty")
        elif not search_rollno.isdigit():
            print("Roll No must contain numbers only.")
        else:
            break
    
    found = False

    for student in students:
        if student["rollno"] == search_rollno:
            print()
            print("Student Found!")
            print()
            print("Name   :", student["name"])
            print("RollNo :", student["rollno"])
            print("Marks  :", student["marks"])
            print("Result :", student["result"])
            print("Grade  :", student["grade"])
            print()

            found = True
            break

    if found == False:
                print("Student Not Found.")

def update_student():                                              #4 Update Student
    print()
    print("----------Update Student----------")
    print()

    while True:
        update_rollno = input("Enter Student RollNo to Update: ")
        if update_rollno.strip() == "":
            print("Roll No cannot be empty.")
        elif not update_rollno.isdigit():
            print("Roll number must contain numbers only.")
        else:
            break

    found = False
    
    for student in students:
        if student["rollno"] == update_rollno:
            print()
            print("Student Found!")

            while True:
                new_name = input("Enter New Name: ")
                if new_name.strip() == "":
                    print("Name cannot be empty")
                elif not new_name.replace(" ", "").isalpha():
                    print("Name must contain letters only.")
                else:
                    break
            
            while True:
                try:
                    new_marks = int(input("Enter New Marks: "))
                    if 0 <= new_marks <= 100:
                        break
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            student["name"] = new_name                         #used to replace the old name & marks
            student["marks"] = new_marks

            #calculate_result & grade

            student["result"] = calculate_result(new_marks)
            student["grade"] = calculate_grade(new_marks)
            save_students(students)

            print()
            print("Student Details Updated Successfully")
            print()

            found = True
            break
    if found == False:
        print()
        print("Student not found.")
        print()

def delete_student():                                             #5 Delete Student
    print()
    print("----------Delete Student----------")
    print()

    while True:
        delete_rollno = input("Enter Student RollNo to Delete: ")
        if delete_rollno.strip() == "":
            print("Roll No cannot be empty.")
        elif not delete_rollno.isdigit():
            print("Roll number must contain numbers only.")
        else:
            break

    found = False
    for student in students:
        if student["rollno"] == delete_rollno:
            students.remove(student)
            save_students(students)
            
            print()
            print("Student Deleted Successfully")
            print()

            found = True
            break
    if found == False:
        print()
        print("Student not found.")
        print()