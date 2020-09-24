classrooms = []

def main():
    while True:
        print("Type 'classroom' if you want to create a classroom")
        print("Type 'list' if you want to list the classrooms")
        print("Type 'exit' if you want to exit")

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
    pass

def list_classrooms_interface():
    pass
    
