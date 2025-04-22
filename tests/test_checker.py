import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utilities import checker


def test_incorrect_arg0():
    args = "sdsadsada blblabla blablabla".split(" ")
    assert not checker.checker(args)


def test_incorrect_arg1():
    args = "task-cli blblabla blablabla".split(" ")
    assert not checker.checker(args)


def test_too_many_args():
    args = "task-cli blblabla blablabla bladadada".split(" ")
    assert not checker.checker(args)


def test_correct_add_input():
    args = 'task-cli add "blblabla blablabla"'.split(" ")
    assert checker.checker(args)


def test_incorrect_number_of_args_add():
    args = "task-cli add".split(" ")
    assert not checker.checker(args)


def test_correct_update_input():
    args = 'task-cli update 1 "blblabla blablabla"'.split(" ")
    assert checker.checker(args)


def test_correct_delete_input():
    args = 'task-cli add "blblabla blablabla"'.split(" ")
    assert checker.checker(args)


def test_non_numeric_id_delete():
    args = "task-cli delete eweqeqewq".split(" ")
    assert not checker.checker(args)


def test_incorrect_number_of_args_delete():
    args = "task-cli delete".split(" ")
    assert not checker.checker(args)


def test_correct_list_inputs():
    args0 = "task-cli list".split(" ")
    args1 = args0.copy()
    args1.append("1")
    assert checker.checker(args0) and checker.checker(args1)


def test_correct_mark_progress_input():
    args0 = "task-cli mark-in-progress 1".split(" ")
    assert checker.checker(args0)


def test_non_numeric_id_mark_progress():
    args = "task-cli mark-in-progress eweqeqewq".split(" ")
    assert not checker.checker(args)


def test_incorrect_number_of_args_mark_progress():
    args = "task-cli mark-in-progress".split(" ")
    assert not checker.checker(args)


def test_correct_mark_done_input():
    args0 = "task-cli mark-done 1".split(" ")
    assert checker.checker(args0)


def test_non_numeric_id_mark_done():
    args = "task-cli mark-done eweqeqewq".split(" ")
    assert not checker.checker(args)


def test_incorrect_number_of_args_mark_done():
    args = "task-cli mark-done".split(" ")
    assert not checker.checker(args)
