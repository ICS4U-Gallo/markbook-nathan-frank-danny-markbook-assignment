"""
Markbook Application
Group members: Danny, Frank, Nathan
"""
from typing import Dict, List

classrooms = []

def main():
    while True:
        print("Type 'classroom' if you want to create a classroom")
        print("Type 'list' if you want to list the classrooms")
        print("Type 'exit' if you want to exit")

        try:
            choice = input("Select a menu option:   ").lower()
        except ValueError:
            print("Error. Please enter a string")
        
        if choice == "classroom":
            create_classroom_interface()
        elif choice == "list":
            list_classrooms_interface()
        elif choice == "exit":
            exit()
        else:
            print("Please enter a vaid choice")
        

def create_classroom_interface():
    pass

def list_classrooms_interface():
    pass
    

def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    assignment = {"name": name, 
                  "due": due, 
                  "points": points
                }
    return assignment


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {
        "course_code": course_code,
        "course_name": course_name,
        "period": period,
        "teacher": teacher,
        "student_list": [],
        "assignment_list": []
    }

    return classroom

def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    total_marks = 0
    student_marks = student["marks"]
    
    for mark in student_marks:
        total_marks += mark      
             

    average_mark = total_marks / len(student_marks)
    return average_mark

def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    
    # Add 
    students = classroom["student_list"]
    students.append(student)    # Append the student dictionary into the student list inside the classroom dictionary

    return classroom


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    students = classroom["student_list"]
    students.remove(student)    # Remove the student dictionary into the student list inside the classroom dictionary
    
    return classroom


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    for key, value in kwargs.items():
        student[key] = value
    return student


if __name__ == "__main__":
    main()
