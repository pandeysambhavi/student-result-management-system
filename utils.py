def calculate_result(marks):
    if marks >= 35:
        result = "Pass"
    else:
        result = "Fail"
    return result
            
def calculate_grade(marks):
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "F"
    return grade
