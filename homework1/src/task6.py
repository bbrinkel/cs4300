# Importing string to use string.punctutation and Path from pathlib to get to the homework directory
import string
from pathlib import Path

def get_word_count(file_name):
    """
    A function that takes a file path as input and reads it to return the word count

    Args:
        file_name: string

    returns word count (int)
    
    """

    # Attempting to open the file
    try:
        # Finding the txt files directory using Path 
        txt_file_directory = str(Path(__file__).parent.parent.resolve()) + '/txt_files_task6/'
        txt_file = txt_file_directory + file_name

        with open(txt_file, 'r') as file:
            # If opens correctly in read mode, read the contents from the file and save it in a varaible
            file_content = file.read()

        # Creating a translator to remove all punctuation from the read content and applying it to the file contents
        translator = str.maketrans('', '', string.punctuation)
        words_only = file_content.translate(translator)

        # Put each word in a list
        words = words_only.split()

        return len(words)

    # Raises error when the file cannont be opened
    except FileNotFoundError:
        raise FileNotFoundError(f'{file_name} not found')
    
    # Raises error when an invalid type is applied to the open function.
    except TypeError:
        raise TypeError('Invalid type passed as file')

# Main, tests function with 'task6_read_me.txt' file.
if __name__ == "__main__":
    file_name = 'task6_read_me.txt'
    print(f"Word count of file {file_name}: {get_word_count(file_name)}\n")