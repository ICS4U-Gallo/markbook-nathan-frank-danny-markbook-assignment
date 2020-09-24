import markbook
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

    classroom = markbook.create_classroom(course_code, course_name, period, teacher)

    with open("data.json", "r") as reader:
        json_object = json.loads(reader.read())

    classrooms = json_object["classrooms"]
    classrooms.append(classroom)

    with open("data.json", "w") as writer:
        json_object = json.dumps(json_object, indent=4)
        reader.write(json_object)

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

main()
