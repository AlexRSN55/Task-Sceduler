today = list()  # today = []
tomorrow = list()  # tomorrow = []
later = list()  # later = []

# Helper
HELP = """
help - print program information.
add - add task in list (user input name of task)
show - print all tasks in list.
"""


# project code for implementation
while True:
    command = input("Enter your command: ")
    if command == "help":
        print(HELP)

    elif command == "add":
        date = input("Enter date: ")
        task = input("Enter name of task: ")

        if date == "Today" or "today":
            today.append(task)
        elif date == "Tomorrow" or "tomorrow":
            tomorrow.append(task)
        else:
            later.append(task)
        print(f"Task {task} add")

    elif command == "show":
        print("Today", today)
        print("Tomorrow", tomorrow)
        print("Later", later )

    elif command == "exit":
        print("Спасибо за использование! До свидания!")
    else:
        print("Unknown command")
        break
