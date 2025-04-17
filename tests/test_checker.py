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
    
    
def test_correct_update_input():
    args = 'task-cli update 1 "blblabla blablabla"'.split(" ")
    assert checker.checker(args)
    
    
def test_correct_delete_input():
    args = 'task-cli add "blblabla blablabla"'.split(" ")
    assert checker.checker(args)
    
    
def test_correct_list_inputs():
    args0 = 'task-cli list'.split(" ")
    args1 = args0.append("1")
    assert checker.checker(args0) and checker.checker(args1)
    

def test_correct_mark_progress_input():
    args0 = 'task-cli mark-in-progress 1'.split(" ")
    assert checker.checker(args0)


def test_correct_mark_done_input():
    args0 = 'task-cli mark-done 1'.split(" ")
    assert checker.checker(args0)
    
    
# def test_whitespaces_input(correct_value):
#     value_arr = correct_value.split()
#     correct_value += "              "
#     correct_value = "               " + correct_value
#     output = split.split_string(correct_value)
#     assert output == value_arr

# def test_correct_input_with_quotes(correct_quotes):
#     output = split.split_string(correct_quotes)
#     assert len(output) == 2


# def test_invalid_input_with_quotes(incorrect_quotes):
#     output = split.split_string(incorrect_quotes)
#     assert not output
