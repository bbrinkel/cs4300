def print_favorite_books():
    """Function that slices the list of books gotten from get_book_list() to see the top three, and prints the top three."""

    book_list = get_book_list()
    
    # Slices original list and stores the first three in top_three_books
    top_three_books = book_list[0:3]

    # Prints each book in top_three_books.
    for book in top_three_books:
        print(book)


def get_book_list():
    """Simple function that returns a list of books to be used."""
    
    return ['Harry Potter and the Goblet of Fire by J.K. Rowling', 
    'Frankenstein by Mary Shelley', 'Of Mice and Men by John Steinbeck',
    'Lord of the Flies by William Golding', '1984 by George Orwell',
    'The Book Thief by Markus Zusak']

def create_student_dictionary():
    """
    Creates a studentDictionary and fills it with students and corresponding Student ID keys (hardcoded).
    
    returns student dictionary

    """

    studentDictionary = {}

    studentDictionary[1] = 'John Smith'
    studentDictionary[2] = 'Jane Smith'
    studentDictionary[3] = 'Walter White'
    studentDictionary[4] = 'James McGill'
    studentDictionary[5] = 'Michael Jordan'
    studentDictionary[6] = 'Nikola Jokic'

    return studentDictionary

# Main, Uses the functions listed above
if __name__ == "__main__":
    print('Three Favorite Books: ')
    print_favorite_books()
    print()

    print('Student Database: ')
    database = create_student_dictionary()

    # Prints each student along with their ID
    for item in database.items():
        print(f'Student: {item[1]} | ID: {item[0]}')

    print()