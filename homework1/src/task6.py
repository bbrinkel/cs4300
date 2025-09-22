# Importing string to use string.punctutation and Path from pathlib to get to the homework directory
import string
from pathlib import Path

def get_word_count_decorator(func):
    """A decorator that adds the functionality of counting the words of a file, needs decorated function to open file
    (Using to add a form of metaprogramming)"""

    def wrapper(*args, **kwargs):
        """
        Wrapper for get_word_count_decorator
        
        Does not check for exceptions, it assumes that the function being decorated already does so. If it did,
        tests would het jumbled up.
        
        """

        # Tries to get file object from function being decorated, and reads its contents
        file_object = func(*args, **kwargs)
        try:
            file_content = file_object.read()
        finally:
            file_object.close()

        # Creating a translator to remove all punctuation from the read content and applying it to the file contents
        translator = str.maketrans('', '', string.punctuation)
        words_only = file_content.translate(translator)

        # Put each word in a list
        words = words_only.split()

        return len(words)

    return wrapper

# decorated with get_word_count_decorator so word count will be gotten
@get_word_count_decorator
def open_file(file_name):
    """
    Function that simply opens up a file and returns that file object if opened to read successfully.

    Args:
        file_name: string

    returns file object of opened file
    
    """

    # Attempting to open the file
    try:
        # Finding the txt files directory using Path 
        txt_file = Path(__file__).parent.parent.resolve() / 'txt_files_task6' / file_name

        file = open(txt_file, 'r')
        return file

    # Raises error when the file cannont be opened
    except FileNotFoundError:
        raise FileNotFoundError(f'{file_name} not found')
    
    # Raises error when an invalid type is applied to the open function.
    except TypeError:
        raise TypeError('Invalid type passed as file')
    

# Main, Uses functions with 'task6_read_me.txt' file.
if __name__ == "__main__":
    file_name = 'task6_read_me.txt'
    print(f"Word count of file {file_name}: {open_file(file_name)}\n")