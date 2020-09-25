import markbook
import json

# Main Function
def main():
    while True:
        print("Type 'classroom' if you want to create a classroom")
        print("Type 'list' if you want to list the classrooms")
        print("Type 'assignment' if you want to create an assignment")
        print("Type 'assignmentlist' if you want to create an assignment")
        print("Type 'exit' if you want to exit")

        # Gets input from user for which menu option to go into
        try:
            choice = input("Select a menu option:   ").lower()
        except ValueError:
            print("Error, Please enter a string")
        
        # Handles which function to run depending on the user input
        if choice == "classroom":
            create_classroom_interface()
        elif choice == "list":
            list_classrooms_interface()
        elif choice == "assignment":
            create_assignment_interface()
        elif choice == "assignmentlist":
            list_assignment_interface()
        elif choice == "exit":
            exit()
        else:
            print("Please enter a vaid choice")

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
            course_code = input("Course Code:  ")
            course_name = input("Course Name:  ")
            period = int(input("Period:  "))
            teacher = input("Teacher Name:  ")
            break
        except ValueError:
            print("Error, please enter a string")

    classroom = markbook.create_classroom(course_code, course_name, period, teacher)
    
    add_to_data("data.json", "classrooms", classroom)


def list_classrooms_interface():
    classrooms_names = []
    
    with open("data.json", "r") as data:
        for classroom in data["classrooms"]:
            course_names = json.load(classroom["course_name"])
            classrooms_names.append(course_names)

    print(classrooms_names)

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
