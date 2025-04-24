import pytest
from unittest.mock import mock_open, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utilities')))

import task_operations as to


# Sample tasks to use in multiple tests
mock_tasks = [
    {"id": 0, "status": "todo", "content": "Buy milk"},
    {"id": 1, "status": "done", "content": "Walk dog"},
]


# --- read_json ---
@patch("builtins.open", new_callable=mock_open)
@patch("json.load", return_value=mock_tasks)
def test_read_json(mock_json_load, mock_file):
    tasks = to.read_json()
    assert tasks == mock_tasks


# --- save_json ---
@patch("builtins.open", new_callable=mock_open)
@patch("json.dump")
def test_save_json(mock_json_dump, mock_file):
    to.save_json(mock_tasks)
    mock_json_dump.assert_called_once_with(mock_tasks, mock_file())


# --- find_task ---
def test_find_task_found():
    assert to.find_task(0, mock_tasks) == 0

def test_find_task_not_found():
    assert to.find_task(999, mock_tasks) is None


# --- change_task ---
@patch("task_operations.save_json")
def test_change_task_update(mock_save_json):
    tasks = mock_tasks.copy()
    result = to.change_task(0, "update", tasks, content="New content", test=True)
    assert result is True
    assert tasks[0]["content"] == "New content"

@patch("task_operations.save_json")
def test_change_task_mark(mock_save_json):
    tasks = mock_tasks.copy()
    result = to.change_task(1, "mark", tasks, status="todo", test=True)
    assert result is True
    assert tasks[1]["status"] == "todo"

@patch("task_operations.save_json")
def test_change_task_delete(mock_save_json):
    tasks = mock_tasks.copy()
    result = to.change_task(0, "delete", tasks, test=True)
    assert result is True
    assert len(tasks) == 1
    assert all(task["id"] != 0 for task in tasks)

@patch("task_operations.save_json")
def test_change_task_not_found(mock_save_json):
    tasks = mock_tasks.copy()
    result = to.change_task(999, "delete", tasks, test=True)
    assert result is False


# --- add_task ---
@patch("task_operations.read_json", return_value=mock_tasks)
@patch("task_operations.save_json")
def test_add_task(mock_save_json, mock_read_json):
    result = to.add_task("Do laundry", test=True)
    assert result is True
    mock_save_json.assert_called_once()
    new_task = mock_save_json.call_args[0][0][-1]
    assert new_task["content"] == "Do laundry"
    assert new_task["status"] == "todo"


# --- delete_task ---
@patch("task_operations.read_json", return_value=mock_tasks.copy())
@patch("task_operations.save_json")
def test_delete_task(mock_save_json, mock_read_json):
    result = to.delete_task(0, test=True)
    assert result is True


# --- update_task ---
@patch("task_operations.read_json", return_value=mock_tasks.copy())
@patch("task_operations.save_json")
def test_update_task(mock_save_json, mock_read_json):
    result = to.update_task(0, "Updated content", test=True)
    assert result is True


# --- mark_task ---
@patch("task_operations.read_json", return_value=mock_tasks.copy())
@patch("task_operations.save_json")
def test_mark_task(mock_save_json, mock_read_json):
    result = to.mark_task(1, "todo", test=True)
    assert result is True

def test_list_tasks_filtered(capsys):
    with patch("task_operations.read_json", return_value=mock_tasks):
        result = to.list_tasks("todo")
        assert result is True

def test_list_tasks_empty(capsys):
    with patch("task_operations.read_json", return_value=[]):
        result = to.list_tasks()
        assert result is True