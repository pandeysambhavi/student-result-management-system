from student import (
    add_student,
    display_student,
    search_student,
    update_student,
    delete_student
)

print("=" * 100)                                       #multiply a string by number repeats it
print("STUDENT RESULT MANAGEMENT SYSTEM".center(100))
print("=" * 100)
print("Developer : Sambhavi Pandey")
print("Welcome!")
print()                           

#Creating & running Menu Function
def menu():                                #fun needs () now they r empty bcoz here we don't need any input
    print("1. Add Student")
    print("2. Display Result")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print()                   

while True: 
    menu()
    while True:                                         #invalid choice loop
        choice = input("Enter your choice (1-6): ")               
        if choice in ["1", "2", "3", "4", "5", "6"]:
            break
        else:
            print("Invalid Choice. Please enter a nuber between 1-6.")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":                                              #6 Exit
        print()                                         
        print("Thank you for using Student Result Managment System.")
        break



