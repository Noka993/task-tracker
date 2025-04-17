import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utilities import split


@pytest.fixture
def correct_value():
    input_string = "task-cli blblabla blablabla"
    return input_string

@pytest.fixture
def correct_quotes():
    quotes = 'task-cli "blblabla blablabla"'
    return quotes

@pytest.fixture
def incorrect_quotes():
    quotes = 'task-cli "blblabla blablabla'
    return quotes


def test_correct_input(correct_value):
    output = split.split_string(correct_value)
    assert output == correct_value.split()

def test_whitespaces_input(correct_value):
    value_arr = correct_value.split()
    correct_value += "              "
    correct_value = "               " + correct_value
    output = split.split_string(correct_value)
    assert output == value_arr

def test_correct_input_with_quotes(correct_quotes):
    output = split.split_string(correct_quotes)
    assert len(output) == 2


def test_invalid_input_with_quotes(incorrect_quotes):
    output = split.split_string(incorrect_quotes)
    assert not output