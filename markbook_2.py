# Based on markbook.py

"""
MANUAL

class added:
- class Assignments
- class Students

"""
from typing import Dict 

class Assignments:

    def create_assignment(name: str, due: str, points: int) -> Dict:
        """Creates an assignment represented as a dictionary
    
        Args:
            name: the name of the assignmeyo nt.
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

class Students:

    def calculate_average_mark(student: Dict) -> float:
        """Calculates the average mark of a student"""
        total_marks = 0
        student_marks = student["marks"]
    
        for mark in student_marks:
            total_marks += mark      

    def edit_student(student: Dict, **kwargs: Dict):
        """Edits the student's info with the provided key/value pairs
        Args:
            student: The student whose data needs to be udated.
            **kwargs: KeyWordARGumentS. The key/value pairs of the
                data that needs to be changed. Can come in the form of a dictionary.
    """
        for key, value in kwargs.items():
            student[key] = value
        return student
