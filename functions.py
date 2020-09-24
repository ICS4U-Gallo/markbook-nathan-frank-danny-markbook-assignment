from markbook import *
from typing import Dict, List
import json

classrooms = []

def main():
    while True:
        print("Type 'classroom' if you want to create a classroom")
        print("Type 'list' if you want to list the classrooms")
        print("Type 'exit' if you want to exit")

        try:
            choice = input("Select a menu option:   ").lower()
        except ValueError:
            print("Error, Please enter a string")
        
        if choice == "classroom":
            create_classroom_interface()
        elif choice == "list":
            list_classrooms_interface()
        elif choice == "exit":
            exit()
        else:
            print("Please enter a vaid choice")
        

def create_classroom_interface():
    while True:
        try:
            course_code = input("Course Code:  ")
            course_name = input("Course Name:  ")
            period = input("Period:  ")
            teacher = input("Teacher Name:  ")
        except ValueError:
            print("Error, please enter a string")


    classroom = {
    "course code": course_code,
    "course name": course_name, 
    "period": period,
    "teacher name": teacher,
    }

    classroom = json.dumps(classroom)

    with open("data.json", "w") as writer:
        json.dump(classroom, writer)

    new_class = json.dumps(classroom)
    return new_class

def list_classrooms_interface():
    pass

main()
