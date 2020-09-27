
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
        print('Type "add student" if you want to add a student to a class.   ')
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
        elif choice == "add student":
            clear()
            add_student_to_classroom_interface()
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
            data = json.loads(reader.read())  # Stores the data file into a variable
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
        data = json.loads(data.read())
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

    if classroom == "exit":
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
        data = json.load(data.read())
        for assignment in data["assignments"]:
            names = assignment["name"]
            assignment_names.append(names)

    print("\nYour Assignments:  ")
    print(*assignment_names, sep=", ")

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
            
def add_student_to_classroom_interface():
    classrooms_names = []

    with open("data.json", "r") as data:
        data = json.loads(data.read())
        for classroom in data["classrooms"]:
            course_names = classroom["course_name"]
            classrooms_names.append(course_names)

    print(*classrooms_names, sep=", ")

    while True:
        try:
            choice_classroom = input("\n Which class would you like to add a student to?(Course name) ")
            first_name = input("What is the student's first name?  ")
            last_name = input("What is the student's last name?    ")
            gender = input("What is the student's gender?   ")
            student_number = int(input("What is the student's student number?   "))
            grade = int(input("What is the student's current grade?   "))
            email = input("What is the student's email?    ")
            marks = list(map(int, input("What is the student's marks?  ").split()))
            comments = input("What comments do you have for this student?   ")
            break
        except ValueError:
            print("Error, please enter the correct form, either a number or a word")

    student = {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "student_number": student_number,
        "grade": grade,
        "email": email,
        "marks": marks,
        "comments": comments
    }

    for classroom in data["classrooms"]:
        if choice_classroom == classroom["course_name"]:
            added_student = markbook.add_student_to_classroom(student, classroom)
            
            classroom = added_student

            with open("data.json", "w") as writer:
                # Converts the python into json strings
                data = json.dumps(data, indent=4)
                # Overwrite the current data with the new added on data
                writer.write(data) 
            break



main()
