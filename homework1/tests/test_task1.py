# Taking the print_hello() function from task1 source file.
from task1 import print_hello

def test_task1(capsys):
    """A simple test for taking what's printed out to the console due to task1.py, and ensuring it
    says 'Hello, World!'."""

    print_hello()
    # stores what was printed out to console
    captured = capsys.readouterr()
    assert captured.out == 'Hello, World!\n', "Expected print of 'Hello, World!'"