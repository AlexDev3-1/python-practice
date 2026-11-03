import json

def load_tasks():
    with open("tasks.json", "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def add_task():
    task = input("what's the task? ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("task added :)")

def view_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. {t['task']} [{status}]")

def task_mark():
    tasks = load_tasks()
    view_tasks
    Number = int(input("which task number? ")) - 1
    tasks[Number]["done "] = True
    save_tasks(tasks)
    print("marked as done :)")
    
    
    
    

while True:
    message = input("\nadd / view / q / mark: ")
    if message == "add":
        add_task()
    elif message == "view":
        view_tasks()
    elif message == "mark":
        task_mark()
    elif message == "q":
        break