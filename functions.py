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
            period = int(input("Period:  "))
            teacher = input("Teacher Name:  ")
            break
        except ValueError:
            print("Error, please enter a string")

    classroom = create_classroom(course_code, course_name, period, teacher)

    with open("data.json", "r") as reader:
        json_object = json.loads(reader.read())

    classrooms = json_object["classrooms"]
    classrooms.append(classroom)

    with open("data.json", "w") as writer:
        json_object = json.dumps(json_object, indent=4)
        reader.write(json_object)

def list_classrooms_interface():
    with open("data.json", "r") as data:
        classroom_info = json.load(data)
        print(classroom_info)


main()
