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
            choice = input("Select a menu option:   ").lower()
            print()
        except ValueError:
            print(" ---------------------------------------------------------- ")
            print("| Error, Please enter a string.                            |")
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
        print("Error, data.json file was not found")
    
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
            course_code = input("\nCourse Code:  ")
            course_name = input("\nCourse Name:  ")
            period = int(input("\nPeriod:  "))
            teacher = input("\nTeacher Name:  ")
            break
        except ValueError:
            print("Error, please enter a string")

    classroom = markbook.create_classroom(course_code, course_name, period, teacher)
    
    add_to_data("data.json", "classrooms", classroom)


def list_classrooms_interface():
    classrooms_names = []
    
    with open("data.json", "r") as data:
        data = json.load(data)
        for classroom in data["classrooms"]:
            course_names = classroom["course_name"]
            classrooms_names.append(course_names)

    print("\nYour Classes:  ")
    print(*classrooms_names, sep=", ")

    print("\nType the name of the class(course name) you want to view")
    print("Or type exit to exit the program")

    try:
        classroom = input("\nPlease enter the name of the class you want to view(Case Sensitive):  ")
    except ValueError:
        print("Error, please enter a string")

    if classroom == "exit":
        exit()

    for classe in data["classrooms"]:
        if classe["course_name"] == classroom:
            print(classe)
            break

def create_assignment_interface():
    while True:
        try:
            name = input("Assignment Name: ")
            due = input("due: ")
            points = int(input("points: "))
        except ValueError:
            print("Error, please enter a string")

        assignment = markbook.create_assignment(name, due, points)
        new_assignment = json.dumps(assignment)
        return new_assignment
    
def list_assignment_interface():
    assignment_names_list = []

    with open("data.json", "r") as data:
        for assignment in data["assignments"]:
            assignment_names = json.load(assignment["name"])
            assignment_names_list.append(assignment_names)
    
    print(assignment_names_list)
    
main()
