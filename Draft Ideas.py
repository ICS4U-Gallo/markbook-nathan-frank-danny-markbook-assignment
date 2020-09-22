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
