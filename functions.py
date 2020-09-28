
from markbook import create_classroom, create_assignment, calculate_average_mark, add_student_to_classroom, remove_student_from_classroom, edit_student
import json
from os import system, name
from time import sleep

# Clears terminal
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
        print('| Type "create classroom" if you want to create a classroom.   |')
        print('| Type "list classrooms" if you want to list the classrooms.   |')
        print('| Type "create assignment" if you want to create an assignment.|')
        print('| Type "list assignments" if you want to list the assignments. |')
        print('Type "add student" if you want to add a student to a class.    |')
        print('| Type "exit" if you want to exit.                             |')
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
        if choice == "create classroom" or choice == "create classrooms":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                     CREATE CLASSROOM                     |")
            print(" ---------------------------------------------------------- ")
            create_classroom_interface()
        elif choice == "list classrooms" or choice == "list classroom":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                       CLASSROOM(S)                       |")
            print(" ---------------------------------------------------------- ")
            list_classrooms_interface()
        elif choice == "create assignment" or choice == "create assignments":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                      NEW ASSIGNMENT                      |")
            print(" ---------------------------------------------------------- ")
            create_assignment_interface()
        elif choice == "list assignments" or choice == "list assignment":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                      ASSIGNMENT(S)                       |")
            print(" ---------------------------------------------------------- ")
            list_assignment_interface()
        elif choice == "add student" or choice =="add students":
            clear()
            print(" ---------------------------------------------------------- ")
            print("|                     ADD STUDENT                          |")
            print(" ---------------------------------------------------------- ")
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


# Function for creating a classroom
def create_classroom_interface():
    while True:
        # Takes input from user
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

    # Gets data back from API function
    classroom = create_classroom(course_code, course_name, period, teacher)

    # Send the data to be added to the data file
    add_to_data("data.json", "classrooms", classroom)


# Function for listing the classrooms
def list_classrooms_interface():
    classrooms_names = []

    with open("data.json", "r") as data:
        data = json.loads(data.read())
        for classroom in data["classrooms"]:    # Iterates through the data file to list the classroom names
            course_names = classroom["course_name"]
            classrooms_names.append(course_names)

    print("\n* Your Classes:  ")
    print(*classrooms_names, sep=", ")

    print("\n* Type the name of the class(course name) you want to view,")
    print("* Or type exit to exit the program.")

    try:
        choice_classroom = input("\n* Please enter the name of the class you want to view (Case Sensitive):  ")    # Takes input from user
    except ValueError:
        print(" ---------------------------------------------------------- ")
        print("| Error, please enter a string.                            |")
        print(" ---------------------------------------------------------- ")

    if classroom == "exit":
        sleep(3)
        clear()
        exit()


    for classroom in data["classrooms"]:    # Iterates through classroom list in data file
        if classroom["course_name"] == choice_classroom:    # If the iteration reaches the user input's specifictation, then print out that classroom's info
            print(classroom)
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

    assignment = create_assignment(name, due, points)

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

# Function for adding students to a classroom    
def add_student_to_classroom_interface():
    classrooms_names = []

    with open("data.json", "r") as data:    
        data = json.loads(data.read())
        for classroom in data["classrooms"]:    # Iterates through classroom to print out all classroom names
            course_names = classroom["course_name"]
            classrooms_names.append(course_names)

    print(*classrooms_names, sep=", ")

    while True:
        # Takes input from user 
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

    # Dictionary for an individual student
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

    for classroom in data["classrooms"]:        # Iterate through the data files classroom
        if choice_classroom == classroom["course_name"]:    # Check to see if the user's selected classroom is the current iteration
            # Gets data from the API function
            added_student = add_student_to_classroom(student, classroom)
            
            # Set the classroom as the data returned from the API
            classroom = added_student
            
            with open("data.json", "w") as writer:
                # Converts the python into json strings
                data = json.dumps(data, indent=4)
                # Overwrite the current data with the new added on data
                writer.write(data) 
            break
