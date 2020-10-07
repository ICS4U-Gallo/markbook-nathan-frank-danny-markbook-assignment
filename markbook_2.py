# Based on markbook.py

"""
MANUAL

class added:
- class Assignments
- class Students

Changes:
- added __init__

"""
from typing import Dict 

class Assignment:
    
    def __init__(self):
        name: str = None
        due: str = None
        points: int = None
        self.name = name
        self.due = due
        self.points = points

    def create_assignment(self, name: str, due: str, points: int) -> Dict:
        """Creates an assignment represented as a dictionary
    
        Args:
            name: the name of the assignmeyo nt.
            due: the due date for the assignment.
            points: what the assignment is out of (denominator).
        Returns:
            Assignment as a dictionary.
        """

        self.name = name
        self.due = due
        self.points = points
        assignment = {
            "name": self.name, 
            "due": self.due, 
            "points": self.points
        }
        return assignment


class Student:

    def __init__(self, first_name: str, last_name: str, gender: str, image: str, student_number: str, grade: int, email: str, marks: list, comments: str):
        student: Dict = {
            "first_name": first_name, 
            "last_name": last_name, 
            "gender": gender, 
            "image": image, 
            "student_number": student_number, "grade": grade, 
            "email": email, 
            "marks": marks, 
            "comments": comments
            }
        self.student = student


    def calculate_average_mark(self, student: Dict) -> float:
        """Calculates the average mark of a student"""
        total_marks = 0
        student_marks = self.student["marks"]
    
        for mark in student_marks:
            total_marks += mark

        average_mark = total_marks / len(student_marks)
        return average_mark

    def edit_student(self, student: Dict, **kwargs: Dict):
        """Edits the student's info with the provided key/value pairs
        Args:
            student: The student whose data needs to be udated.
            **kwargs: KeyWordARGumentS. The key/value pairs of the
                data that needs to be changed. Can come in the form of a dictionary.
    """
        for key, value in kwargs.items():
            self.student[key] = value
    
