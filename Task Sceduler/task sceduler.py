# Helper
HELP = """
help - print program information.
add - add task in list (user input name of task)
show - print all tasks in list.
"""
# tasks list
tasks = []

run = True
# project code for implementation
while run:
    command = input("Enter your command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Enter name of task: ")
        tasks.append(task)
        print("Task add in list")
    else:
        print("Unknown command")
        break
print("Goodbye!")