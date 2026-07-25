import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

def load_students():
    try:
        with open(DATA_FILE, "r") as file:
            students = json.load(file)
            return students
    except FileNotFoundError:
        return []
    
def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

        
