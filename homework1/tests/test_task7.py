# Import pytest and get_first_five_paragraph_elements from task7 source file.
import pytest
from task7 import get_first_five_paragraph_elements

def test_first_five_paragraph_elements():
    """Tests to ensure that the get_first_five_paragraph_elements() function returns the correct list"""

    # Hardcoded list for expected strings from function.
    expected_list = [ ' Paragraph 1 ', ' Paragraph 2 ', ' Paragraph 3 (Inside div) ', 
    ' Paragraph 4 (Inside div) ', ' Paragraph 5 ']

    # Set the tested_list to the return value of the function.
    tested_list = get_first_five_paragraph_elements('hello.html')

    # Ensures list size is the same for tested and expected
    assert len(tested_list) == len(expected_list), f'Expected list of {len(expected_list)} entries'

    # Ensures every entry in expected_list is in tested_list (not necessary but good for pointing out what's missing)
    for paragraph in expected_list:
        assert paragraph in tested_list, f'Expected {paragraph} in list but not found' 

    # Ensures that order of lists match
    assert expected_list == tested_list, 'Lists do not match'

def test_first_five_not_found():
    """Ensures error is raised when file isn't found"""

    with pytest.raises(FileNotFoundError):
        get_first_five_paragraph_elements('not_a_file.txt')

def test_first_five_wrong_type():
    """Ensures error raised when wrong type passed for filename"""

    with pytest.raises(TypeError):
        get_first_five_paragraph_elements(10)

def test_first_five_no_paragraphs():
    """Ensures error is raised when there are no <p> elements in the html file given"""

    with pytest.raises(ValueError):
        get_first_five_paragraph_elements('no_paragraphs.html')
