"""Lets put what we think in here, Delete this when we are done"""

"""Add Student to Classroom"""
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

"""Remove Student to Classroom"""
def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    students = classroom["student_list"]
    students.remove(student)    # Based on the logic above, remove the student dictionary into the student list inside the classroom dictionary
    
