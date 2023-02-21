# Helper
HELP = """
help - print program information.
add - add task in list (user input name of task)
show - print all tasks in list.
"""
tasks = {}

# project code for implementation
while True:
    command = input("Enter your command: ")
    if command == "help":
        print(HELP)

    elif command == "add":
        date = input("Enter date for your task: ")
        task = input("Enter name of the task: ")
        # if list have date, add task in list
        if date in tasks:
            tasks[date].append(task)
        # if list have not date, create date
        else:
            tasks[date] = []
            tasks[date].append(task)
        print(f"The task {task} was added on the {date} ")

    elif command == "show":
        print(tasks)

    else:
        print("Unknown command")
        break
    print("Goodbye!")