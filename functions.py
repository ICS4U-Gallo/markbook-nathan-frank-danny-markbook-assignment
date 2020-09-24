from markbook import create_assignment, create_classroom, calculate_average_mark, add_student_to_classroom, remove_student_from_classroom, edit_student

from typing import Dict, List

classrooms = []

def main():
    while True:
        print('Type "classroom" if you want to create a classroom')
        print('Type "list" if you want to list the classrooms')
        print('Type "exit" if you want to exit')
        # Grammar fix in case anyone wondering.
        # In a sentence, it is more proper to use " rather than ' to reference sth.

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
    # This is from Frank, so there is no "glitchless-guarantee."
    course_code = str(input("Course Code: "))
    course_name = str(input("Course Name: "))
    period = str(input("Period: "))
    teacher_name = str(input("Teacher Name: "))
    student_list = list(input("Student List: "))
    assignments_list = list(input("Assignments: ")
    # I gathered the informations of the course above.
    
    classroom = {
    "course code": course_code,
    "course name": course_name, 
    "period": period,
    "teacher name": teacher_name,
    "student list": student_list, 
    "assignments list": assignments_list
    # I listed the information into a dictionary.
    }
    new_class = json.dumps(classroom)
    # I dump the dictionary into .json file.
    return new_class

def list_classrooms_interface():
    pass
