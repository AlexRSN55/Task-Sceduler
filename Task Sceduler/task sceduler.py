# Helper
HELP = """
help - print program information.
add - add task in list (user input name of task)
show - print all tasks in list.
random - add random task on date "today"
"""
RANDOM_TASK = "Learning Python"

tasks = {

}

# project code for implementation
while True:
    command = input("Enter your command: ")
    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("Enter date for your task: ")
        task = input("Enter name of the task: ").capitalize()
# if list have date, add task in list
        if date in tasks:
            tasks[date].append(task)
# if list have not date, create date
        else:
            tasks[date] = []
            tasks[date].append(task)
        print(f"The task {task} was added on the {date} ")

    elif command == "show":
        date = input("Enter date for show tasks list ")
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print('No such date')

    elif command == "random":
        if "today" in tasks:
            tasks["today"].append(RANDOM_TASK)
        else:
            tasks["today"] = []
            tasks["today"].append(RANDOM_TASK)
    else:
        print("Unknown command")
        break
print("Goodbye!")