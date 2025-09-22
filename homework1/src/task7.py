from bs4 import BeautifulSoup
from pathlib import Path

def get_first_five_paragraph_elements(html_name):
    """
    Uses BeautifulSoup4 to parse an html file and gets list of first 5 <p> elements

    Args:
        html_name: string

    returns list of first 5 paragrpah elements of html file
    
    """

    # Gets the file directory of the html file/s for this task and then applies the actual html file name to the path.
    html_file_directory = str(Path(__file__).parent.parent.resolve()) + '/html_files_task7/'
    html_file = html_file_directory + html_name

    # Tries to open the file for reading
    try:
        with open(html_file, 'r') as file:
            html_contents = file.read()

        # Creates a BeautifulSoup object for parsing the desired html file
        soup = BeautifulSoup(html_contents, 'html.parser')

        # If upon trying to find the first <p> element returns None, raise error. There are no <p> elements in the file.
        if soup.find('p') == None:
            raise ValueError('This HTML file has no <p> elements')

        # Get list of all paragraph elements, and then slices to be up to the first 5
        paragraphs = soup.find_all('p')
        paragraphs = [p.text for p in paragraphs][:5]

        return paragraphs
        
    # Raises error when the file cannont be opened
    except FileNotFoundError:
        raise FileNotFoundError(f'{html_name} not found')
    
    # Raises error when an invalid type is applied to the open function.
    except TypeError:
        raise TypeError('Invalid type passed as file')

# Main, tests the function above with a simple html file
if __name__ == "__main__":
    html_file = 'hello.html'
    paragraph_list = get_first_five_paragraph_elements(html_file)

    print(f'First five <p> elements of {html_file}:')
    for paragraph in paragraph_list:
        print(paragraph) 

    print()


