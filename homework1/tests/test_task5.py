# Imports print_favorite_books(), and create_student_dictionary() from task5 source file. Also imports pytest.
import pytest 
from task5 import print_favorite_books, create_student_dictionary

def test_book_list(capsys):
    """Runs tests corresponding to print_favorite_books() to ensure correct output."""

    # The expected list of books
    valid_list = ['Harry Potter and the Goblet of Fire by J.K. Rowling', 'Frankenstein by Mary Shelley',
    'Of Mice and Men by John Steinbeck']

    # Creating a list from the printed books of the print_favorite_books() function
    print_favorite_books()
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')

    # Ensure that the length of the list is 3 
    assert len(lines) == 3, 'Expected book list of 3'

    # Ensure every book in list is there (probably not necessary)
    for book in valid_list:
        assert book in lines, f'expected book {book} not found in list'

    # Ensure order matches
    assert lines == valid_list, 'Expected lists to match' 

def test_student_dictionary():
    """Runs tests corresponding to create_student_dictionary() to ensure correct output."""

    # The expected key-value pairs of the dictionary
    expected_dictionary = {1: 'John Smith', 2: 'Jane Smith', 3: 'Walter White', 4: 'James McGill', 
    5: 'Michael Jordan', 6: 'Nikola Jokic'}

    tested_dictionary = create_student_dictionary()

    # Ensuring that the returned data structure is a dictionary and that its length is 6
    assert isinstance(tested_dictionary, dict), 'Expected a dictionary data structure'
    assert len(tested_dictionary) == 6, 'Expected dictionary length of 6'

    # Ensure every item in the expected_dictionary is also in the tested dictionary (probably not necessary)
    testedItems = tested_dictionary.items()
    for item in expected_dictionary.items():
        assert item in testedItems, f'Expected {item} in dictionary'

    # Ensure order matches
    assert tested_dictionary == expected_dictionary, 'Expected Dictionaries to match'
