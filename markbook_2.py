# Based on markbook.py

"""
MANUAL

class added:
- class Assignments
- class Students
- class Classroom
- class Teacher (working on it)
- class Person (working on it)

Changes:
- added __init__

"""
from typing import Dict 


# class Assignment

class Assignment:
    
    def __init__(self):

        self.assignment = None


    def create_assignment(self, name: str, due: str, points: int) -> Dict:
        """Creates an assignment represented as a dictionary"""

        assignment: Dict = {
            "name": name, 
            "due": due, 
            "points": points
        }
        self.assignment = assignment


# class Student

class Student:

    def __init__(self, first_name: str, last_name: str, gender: str, image: str, student_number: str, grade: int, email: str, marks: list, comments: str):
        """Create a student entry"""

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
            
            
# class Classroom

class Classroom:

    def __init__(self):
        self.classroom = None


    def create_classroom(self, course_code: str, course_name: str, period: int, teacher: str) -> Dict:
        """Creates a classroom dictionary"""

        classroom: Dict = {
            "course_code": course_code,
            "course_name": course_name,
            "period": period,
            "teacher": teacher,
            "student_list": [],
            "assignment_list": []
        }
        self.classroom = classroom
    

    def add_student_to_classroom(self, student: Dict, classroom: Dict):
        """Adds student to a classroom"""

        self.classroom["student_list"].append(student)


    def remove_student_from_classroom(self, student: Dict, classroom: Dict):
        """Removes student from classroom"""

        self.classroom["student_list"].remove(student)

# class Teacher (nothing yet)

class Teacher:
    None
    
    
# class Person (unfinished)

class Person:

    def __init__(self, person: Dict):
        self.person = person
        
