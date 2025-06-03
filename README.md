# Task Tracker CLI

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![CLI](https://img.shields.io/badge/CLI-Task%20Tracker-green.svg)

A command-line task management system written in Python for tracking and organizing your tasks.

## Features

- ✅ Add, update, and delete tasks
- 📋 List all tasks or filter by status
- 🏷️ Mark tasks as "todo", "in-progress", or "done"
- 📂 JSON-based storage for persistence
- 🔍 Input validation and error handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Noka993/task-tracker.git
cd task-tracker
pip install -r requirements.txt
```
2. Run the application:
```bash
python taskt.py
```
## Usage/Basic Commands

| Command | Description | Usage Example | Required Arguments |
|---------|-------------|---------------|---------------------|
| `add` | Add a new task | `task-cli add "Buy groceries"` | `[task_content]` |
| `update` | Update task content | `task-cli update 1 "Buy milk"` | `[task_id] [new_content]` |
| `delete` | Delete a task | `task-cli delete 1` | `[task_id]` |
| `list` | List all tasks | `task-cli list` | None |
| `list [status]` | Filter tasks by status | `task-cli list done` | Optional: `[status]` |
| `mark-in-progress` | Mark task as in-progress | `task-cli mark-in-progress 1` | `[task_id]` |
| `mark-done` | Mark task as done | `task-cli mark-done 1` | `[task_id]` |

**Status Options**: `todo`, `in-progress`, `done`
## Project Structure
```
task-tracker/
├── taskt.py                # Main application entry point
├── tests/
|   ├── test_checker.py
|   ├── test_checker.py
|   ├── test_input.py
|   ├── test_split.py
|   ├── test_task_operations.py
├── utilities/
│   ├── checker.py          # Command validation and routing
│   ├── message.py          # User message templates
│   ├── split.py            # Input string parsing
│   └── task_operations.py  # Core task operations
└── tasks.json              # Task storage (auto-created)
```

## License

This project is licensed under the [MIT License](LICENSE).
