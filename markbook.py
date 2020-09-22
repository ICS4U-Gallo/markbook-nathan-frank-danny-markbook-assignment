"""
Markbook Application
Group members: Danny, Frank, Nathan
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    return {
        "name": name,
        "due_date": due,
        "points": points
    }


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    return {
        "course_code": course_code,
        "course_name": course_name,
        "period": period,
        "teacher": teacher
    }

def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    average_mark = 0
    for i in student:
        average_mark += student[i]
    return average_mark/ len(student)


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    for i in student:
        classroom[i] = i
    return classroom


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    del classroom[student]


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
