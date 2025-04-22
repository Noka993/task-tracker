import json
import uuid

def read_json(file_path='tasks.json'):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def save_json(tasks, file_path='tasks.json'):
    with open(file_path, 'w') as f:
        json.dump(tasks, f)
    
def is_id_unique(id, tasks):
    for task in tasks:
        if task.get(id):
            return False
    return True

def add_task(content):
    tasks = read_json("tasks.json")
    id = uuid.uuid4()
    
    while not is_id_unique(id, tasks):
        id = uuid.uuid4()
        
    tasks.append(
        {
            "id": id,
            "content": content
        }
    )
    
    save_json(tasks)
    return True

def delete_task(id):
    return True

def update_task(id, content):
    return True

def mark_task(id):
    return True

def list_tasks(id=None):
    return True