import random
# Helper
HELP = """
help - print program information.
add - add task in list (user input name of task)
show - print all tasks in list.
random - add random task on date "today"
"""
RANDOM_TASKS = ["Python", "Linux", "Kubernetes", "Docker", "Ansible"]

tasks = {}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    # if list have not date, create date
    else:
        tasks[date] = []
        tasks[date].append(task)
    print(f"The task {task} was added on the {date} ")

# project code for implementation
while True:
    command = input("Enter your command: ")
    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("Enter date for your task: ")
        task = input("Enter name of the task: ").capitalize()
        add_todo(date, task)

    elif command == "show":
        date = input("Enter date for show tasks list ")
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print('No such date')

    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo('today', task)
    else:
        print("Unknown command")
        break
print("Goodbye!")