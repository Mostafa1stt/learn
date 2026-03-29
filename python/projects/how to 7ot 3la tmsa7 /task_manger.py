class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.status = "planning"

def add_task(obj_arr, name, due_date):
    obj_arr.append(Task(name, due_date))

def delete_task(obj_arr, name):
    for i,x in enumerate(obj_arr):
        if x.name == name:
            del obj_arr[i]
            return

def mark_done(obj_arr, name, status):
    for x in obj_arr:
        if x.name == name:
            x.status = status
            return

def save_to_file(obj_arr):
    with open("task_file.txt","w") as f:
        for task in obj_arr:
            f.write(f"{task.name},{task.due_date},{task.status}\n")
