import datetime
import uuid

class Task:
    def __init__(self, task, created_time, updated_time, completed_time, task_done, id):
        self.task = task
        self.created_time = created_time
        self.updated_time = updated_time
        self.completed_time = completed_time
        self.task_done = task_done
        self.id = id
        print("Task Created Successfuly\n")

    def update_task(self, task, updated_time):
        self.task = task
        self.updated_time = updated_time
        print("Task Updated Successfully\n")

    def complete_task(self, completed_time):
        self.completed_time = completed_time
        self.task_done = True
        print("Task Updated Successfully\n")

tasks = []

def now():
    return datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")


def init():
    print("1. Add New Task")
    print("2. Show All Tasks")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")


def create_task():
    name = input("Enter New Task: ")
    created_time = now()
    updated_time = "NA"
    completed_time = "NA"
    task_done = False
    id = uuid.uuid4()

    t = Task(name, created_time, updated_time, completed_time, task_done, id)
    tasks.append(t)


def show_task(task):
    print(f'ID - {task.id}')
    print(f'Task - {task.task}')
    print(f'Created time - {task.created_time}')
    print(f'Updated time - {task.updated_time}')
    print(f'Completed - {task.task_done}')
    print(f'Completed time - {task.completed_time}')
    print()


def show_tasks(filter):
    incompleate_tasks = [task for task in tasks if task.task_done == False]
    completed_task = [task for task in tasks if task.task_done == True]
    if filter == 'all':
        if len(tasks) == 0:
            print("No Tasks\n")
        for task in tasks:
            show_task(task)
    elif filter == "completed":
        if len(completed_task) == 0:
            print("No completed Tasks\n")
        for task in completed_task:
            show_task(task)
    elif filter == "incomplete":
        if len(incompleate_tasks) == 0:
            print("No incomplete Tasks\n")
        for task in incompleate_tasks:
            show_task(task)


def update_task():
    print("Select Which Task to Update\n")
    incompleate_tasks = [task for task in tasks if task.task_done == False]
    if len(incompleate_tasks) == 0:
        print("No incomplete task\n")
        return
    for index, task in enumerate(incompleate_tasks):
        print(f'Task No - {index+1}')
        show_task(task)
    c = int(input("Enter Task No: "))
    name = input("Enter New Task Name: ")
    updated_time = now()
    incompleate_tasks[c-1].update_task(name, updated_time)


def complete_task():
    print("Select Which Task to Complete\n")
    incompleate_tasks = [task for task in tasks if task.task_done == False]
    if len(incompleate_tasks) == 0:
        print("No incomplete task")
        return
    for index, task in enumerate(incompleate_tasks):
        print(f'Task No: {index+1}')
        show_task(task)
    c = int(input("Enter Task No: "))
    completed_time = now()
    incompleate_tasks[c-1].complete_task(completed_time)


while (True):

    init()
    c = int(input("Enter Option: "))
    print()
    if c == 1:
        create_task()
    elif c == 2:
        show_tasks("all")
    elif c == 3:
        show_tasks("incomplete")
    elif c == 4:
        show_tasks("completed")
    elif c == 5:
        update_task()
    elif c == 6:
        complete_task()
