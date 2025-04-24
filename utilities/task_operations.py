import json


def read_json(file_path="tasks.json"):
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(tasks, file_path="tasks.json"):
    with open(file_path, "w") as f:
        json.dump(tasks, f)


def find_task(id, tasks):
    for task in tasks:
        if task.get("id") == id:
            return id
    return None


def change_task(id, operation, tasks, content=None, status=None, test=False):
    id = int(id)
    for task in tasks:
        if task.get("id") == id:
            if operation == "update":
                task["content"] = content
            elif operation == "mark":
                task["status"] = status
            elif operation == "delete":
                tasks.remove(task)
            if not test:
                save_json(tasks)
            print(f"Task {operation}ed successfully (ID: {id})")
            return True

    print(f"Task with ID: {id} not found")
    return False


def add_task(content, test=False):
    tasks = read_json("tasks.json")
    id = tasks[-1].get("id") + 1 if tasks else 0
    tasks.append({"id": id, "status": "todo", "content": content})

    if not test:
        save_json(tasks)
    print(f"Task added successfully (ID: {id})")
    return True


def delete_task(id, test=False):
    tasks = read_json("tasks.json")
    return change_task(id, "delete", tasks, test=test)


def update_task(id, content, test=False):
    tasks = read_json("tasks.json")
    return change_task(id, "update", tasks, content=content, test=test)


def mark_task(id, status, test=False):
    tasks = read_json("tasks.json")
    return change_task(id, "mark", tasks, status=status, test=test)


def list_tasks(status=None):
    tasks = read_json("tasks.json")
    if not tasks:
        print("No tasks found")
    if status:
        print(
            [
                f"{task['id']}: {task['content']}"
                for task in tasks
                if task["status"] == status
            ]
        )
    else:
        print([f"{task['id']}: {task['status']}: {task['content']}" for task in tasks])
    return True