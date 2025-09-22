# Imports pytest and various functions from task3 source file to test
import pytest
from task3 import check_sign, find_primes, find_sum

class TestSignClass:
    """Class for testing all outcomes of check_sign() function"""

    @pytest.mark.parametrize("value, expected", [(1, 'Positive'), (-1, 'Negative'), (0, 'Zero'), (100000000, 'Positive'),
    (-10000000, 'Negative'), (-3.14, 'Negative')])
    def test_sign(self, value, expected):
        """
        Uses parameterized values to test that the expected value of check_sign() are returned (checks various edge cases)
        
        Args:
            value: int or float
            expected: int or float
        
        """
        assert check_sign(value) == expected, f"Expected {expected} for {value}"

    @pytest.mark.parametrize("input", ['', 'hello',])
    def test_sign_type(self, input):
        """
        Ensures that a TypeError is correctly raised when it needs to be
        
        Args:
            input: non float or int

        """

        with pytest.raises(TypeError):
            check_sign(input)

class TestPrimesClass:
    """Class for testing cases for find_primes() function"""

    @pytest.mark.parametrize("numPrimes, expected", [(10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), 
    (1, [2]), (0, [])])
    def test_primes(self, capsys, numPrimes, expected):
        """
        Tests to ensure that the find_primes() function genertes the correct output. Although only have to test 10, added
        a second test for increased learning. 
        
        Args:
            numPrimes: int
            expected: list of primes (ints)
        
        """

        find_primes(numPrimes)
        # Stores what was printed out to the console and splits it into list of strings (lines)
        captured = capsys.readouterr()
        lines = captured.out.split()

        # Ensuring that the length of lines is 10
        assert len(lines) == numPrimes, f'Expected amount of primes to be {numPrimes}'

        # For every prime value in the list, cast it as an int and compare it to its corresponding correct
        # value in the hardcoded list.
        for i in range(numPrimes):
            assert expected[i] == int(lines[i]), f'Mismatch in list at index {i}'

    def test_primes_type(self):
        """Simple test for ensuring error is raised when wrong type is used for input"""

        with pytest.raises(TypeError):
            find_primes('Hello')

    def test_primes_negative(self):
        """Simple test for ensuring error is raised when input is negative"""

        with pytest.raises(ValueError):
            find_primes(-1)


class TestSumClass:
    """Class for testing all aspects of the test_sum() function"""

    @pytest.mark.parametrize("number, expected", [(100, 5050), (47, 1128), (1,1)])
    def test_sum(self, number, expected):
        """
        Simple test, just asserting that the correct output of the find_sum() function gives the correct sum.
        Testing different cases for increased learning.
        
        Args:
            number: int
            expected: int
        
        """

        assert find_sum(number) == expected, f'Expected {expected} for sum of all numbers 1-{number}' 

    def test_sum_type(self):
        """Ensures error raised when invalid type is input into find_sum()."""

        with pytest.raises(TypeError):
            find_sum('Test')

    def test_sum_negative(self):
        """Ensures error raised when input value is less than or equal to 0."""
        
        with pytest.raises(ValueError):
            find_sum(0)
