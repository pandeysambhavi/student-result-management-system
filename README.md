# Student Result Management System

A Python-based console application to manage student academic records.

This project allows users to add, display, search, update, and delete student records. Student data is stored permanently in a JSON file, so the data remains available even after the program is closed.

## Features

- Add new student records
- Display all student results
- Search students using Roll Number
- Update student details
- Delete student records
- Calculate Pass/Fail result automatically
- Calculate grades automatically
- Validate user input
- Prevent duplicate Roll Numbers
- Store student data permanently using JSON file handling
- Modular code organization using multiple Python files

## Technologies Used

- Python
- JSON
- File Handling
- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- Modules and Imports

## Project Structure

Student_Result_Management_System/
│
├── main.py
├── student.py
├── utils.py
├── data_handler.py
├── data.json
└── README.md

## File Description:

### main.py

The entry point of the application.
It displays the project heading, runs the main menu, accepts the user's choice, and calls the required function.

### student.py

Contains the main student management functions:
1. Add Student
2. Display Student
3. Search Student
4. Update Student
5. Delete Student

It also contains input validation logic.

### utils.py

Contains reusable functions for calculating:
Student Result
Student Grade

### data_handler.py

Handles file operations:
Loading student data from data.json
Saving student data to data.json

### data.json
Stores student records permanently in JSON format.

## Input Validation :
The project validates user input to prevent invalid data.

### Examples:
- Student name cannot be empty
- Student name must contain letters only
- Roll Number cannot be empty
- Roll Number must contain numbers only
- Duplicate Roll Numbers are not allowed
- Marks must be between 0 and 100
- Marks must contain numbers only
- Menu choice must be between 1 and 6

## Grade Calculation:
The program calculates grades automatically based on marks

Marks : 90 - 100    80 - 89    70 - 79     60 - 69     35-59    Below 35 

Grade :    A+          A          B          C          D          F

## Result Calculation:

Marks greater than or equal to 35 → Pass
Marks below 35 → Fail

### How to Run the Project:
- Clone or download the project.
- Open the project folder in VS Code.
- Open the terminal inside the project folder.
Run:
python main.py
or:
py main.py
Select an option from the menu.

Data Storage
Student data is stored in data.json.

### When the program starts:
data.json
     ↓
load_students()
     ↓
students list
When a student is added, updated, or deleted:
students list
     ↓
save_students(students)
     ↓
data.json
This allows student records to remain saved even after the program is closed.

## Future Improvements

- Possible future improvements include:
- Adding a graphical user interface
- Adding database support using SQLite or MySQL
- Adding user login and authentication
- Adding subject-wise marks
- Adding percentage calculation
- Adding class-wise student management
- Exporting results to CSV or Excel files

## Author
### Sambhavi Pandey
Python Project — Student Result Management System
