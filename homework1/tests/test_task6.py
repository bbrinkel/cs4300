# Importing pytest and open_file() from task6 source file
import pytest
from task6 import open_file

@pytest.mark.parametrize("filename, expected", [('task6_read_me.txt', 104), ('example1.txt', 7),
('example2.txt', 13)])
def test_word_count_accuracy(filename, expected):
    """
    Parameterized test for verifying the expected output of getting the word count for different text files
    
    Args:
        filename: string
        expected: int
    
    """

    word_count = open_file(filename)

    assert word_count == expected, f'Expected word count of {expected}'

def test_word_count_not_found():
    """Ensures error is raised when file isn't found"""

    with pytest.raises(FileNotFoundError):
        open_file('not_a_file.txt')

def test_word_count_wrong_type():
    """Ensures error raised when wrong type passed for filename"""
    
    with pytest.raises(TypeError):
        open_file(10)

