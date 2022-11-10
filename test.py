import index
import pytest


sentence = "Trying to master the use of GitHub Classroom."
@pytest.fixture

def input_value():
    input = sentence
    return input

# First test function test_length()
def test_word_count(input_value):
    assert index.word_count(input_value) == 8


# Second test function test_struc()
def test_index_count(input_value):
    assert index.char_count(input_value) == 45


# third test function test_struc()
def test_first_char(input_value):
    assert index.first_char(input_value) == "T"
  

# fourth test function test_struc()
def test_last_char(input_value):
    assert index.last_char(input_value) == "."

# Run these tests with `python3 -m pytest test.py`