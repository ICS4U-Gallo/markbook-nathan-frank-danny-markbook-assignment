"""
Markbook Application
Group members: Danny, Frank, Nathan
"""
from typing import Dict, List


# Students Dictionary 
"""
first_name: str
last_name: str
Gender
image
student number
grade: int
email
marks: List[float]
Comments
"""

# class dictionary
"""
course code
course name
period
teacher name
student list
assignments list
"""

# assignments dictionary
"""
Due
name
points
"""

def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    assignment = {
        "name": name,
        "due_date": due,
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

def add_student_to_classroom(student: Dict, classroom: Dict):a
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
    


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    classroom[student] = kwargs
    return classroom
