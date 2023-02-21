today = list()  # today = []
tomorrow = list()  # tomorrow = []
later = list()  # later = []

# Helper
HELP = """
help - print program information.
add - add task in list (user input name of task)
show - print all tasks in list.
"""
# tasks listsceduler
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
    # elif command == "exit":
    #     print("Спасибо за использование! До свидания!")
    else:
        print("Unknown command")
        break
print("Goodbye!")