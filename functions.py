""" From Tianyu (GamingFrankie): I got a family activity this afternoon so I am not able to attend to group meeting (if there is any)...
    Please just delete this message if anyone see it after 3 pm.
    So What I want to do is to improve the UI, please note that I add a "*" mark in front of input()s and some print()s
    to be something like a "notification."
"""

import markbook
import json
from os import system, name 
from time import sleep 
def clear(): 
  
    # windows 
    if name == 'nt': 
        empty_screen = system('cls') 
  
    # mac and linux
    else: 
        empty_screen = system('clear') 

# Main Function
def main():
    while True:
        print(" ---------------------------------------------------------- ")
        print("|                         MARKBOOK                         |")
        print(" ---------------------------------------------------------- ")
        print('| Type "classroom" if you want to create a classroom.      |')
        print('| Type "list" if you want to list the classrooms.          |')
        print('| Type "assignment" if you want to create an assignment.   |')
        print('| Type "assignments" if you want to list the assignments.  |')
        print('| Type "exit" if you want to exit.                         |')
        print(" ---------------------------------------------------------- ")
        # Gets input from user for which menu option to go into
        try:
            print()
            choice = input("* Select a menu option:   ").lower()
            print()
        except ValueError:
            print(" ---------------------------------------------------------- ")
            print("| Error, please enter a string.                            |")
            print(" ---------------------------------------------------------- ")
            sleep(3) 
            clear()
        
        # Handles which function to run depending on the user input
        if choice == "classroom":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                     CREATE CLASSROOM                     |")
            print(" ---------------------------------------------------------- ")
            create_classroom_interface()
        elif choice == "list":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                       CLASSROOM(S)                       |")
            print(" ---------------------------------------------------------- ")
            list_classrooms_interface()
        elif choice == "assignment":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                      NEW ASSIGNMENT                      |")
            print(" ---------------------------------------------------------- ")
            create_assignment_interface()
        elif choice == "assignments":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                      ASSIGNMENT(S)                       |")
            print(" ---------------------------------------------------------- ")
            list_assignment_interface()
        elif choice == "exit":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                    THANK YOU FOR USING                   |")
            print(" ---------------------------------------------------------- ")
            exit()
        else:
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                   ERROR: INVALID CHOICE                  |")
            print(" ---------------------------------------------------------- ")

# Function for adding data to data.jsonfile
def add_to_data(file_name, list_name, data_to_add):
    try:
        with open(file_name, "r") as reader:  
            data = json.loads(reader.read())    # Stores the data file into a variable
    except FileNotFoundError:
        print(" ---------------------------------------------------------- ")
        print("| Error, file was not found.                               |")
        print(" ---------------------------------------------------------- ")
    
    # Appends the data into the specified json object's list
    data[list_name].append(data_to_add)

    with open(file_name, "w") as writer:
        # Converts the python into json strings
        data = json.dumps(data, indent=4)
        # Overwrite the current data with the new added on data
        writer.write(data)


def create_classroom_interface():
    while True:
        try:
            course_code = input("\n* Course Code:  ")
            course_name = input("\n* Course Name:  ")
            period = int(input("\n* Period:  "))
            teacher = input("\n* Teacher Name:  ")
            break
        except ValueError:
            print(" ---------------------------------------------------------- ")
            print("| Error, please enter a string.                            |")
            print(" ---------------------------------------------------------- ")


    classroom = markbook.create_classroom(course_code, course_name, period, teacher)
    
    add_to_data("data.json", "classrooms", classroom)


def list_classrooms_interface():
    classrooms_names = []
    
    with open("data.json", "r") as data:
        data = json.load(data)
        for classroom in data["classrooms"]:
            course_names = classroom["course_name"]
            classrooms_names.append(course_names)

    print("\n* Your Classes:  ")
    print(*classrooms_names, sep=", ")

    print("\n* Type the name of the class(course name) you want to view,")
    print("* Or type exit to exit the program.")

    try:
        classroom = input("\n* Please enter the name of the class you want to view (Case Sensitive):  ")
    except ValueError:
        print(" ---------------------------------------------------------- ")
        print("| Error, please enter a string.                            |")
        print(" ---------------------------------------------------------- ")

    if classroom = "exit":
        sleep(3)
        clear()
        exit()

    for classe in data["classrooms"]:
        if classe["course_name"] == classroom:
            print(classe)
            break


def create_assignment_interface():
    while True:
        try:
            name = input("* Assignment Name: ")
            due = input("* Due Date: ")
            points = int(input("* Total Score: "))
            break
        except ValueError:
            print(" ---------------------------------------------------------- ")
            print("| Error, please enter a string.                            |")
            print(" ---------------------------------------------------------- ")

        assignment = markbook.create_assignment(name, due, points)
        add_to_data("data.json", "assignments", assignment)


def list_assignment_interface():
    assignment_names = []

    with open("data.json", "r") as data:
        data = json.load(data)
        for assignment in data["assignments"]:
            names = assignment["name"]
            assignment_names.append(names)

    print("\nYour Assignments:  ")
    print(names)

    print("\n* Type the name of the assignment you want to view,")
    print("* Or type exit to exit the program.")

    try:
        assignment = input("\n* Please enter the name of the assignment you want to view (Case Sensitive):  ")
    except ValueError:
        print(" ---------------------------------------------------------- ")
        print("| Error, please enter a string.                            |")
        print(" ---------------------------------------------------------- ")

    if assignment == "exit":
        sleep(3)
        clear()
        exit()
        
    for assignment_info in data["assignments"]:
        if assignment_info["name"] == assignment:
            print(assignment_info)
            break
    
main()
