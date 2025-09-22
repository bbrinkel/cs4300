# Importing pytest and taking various functions from task2 source file to test.
import pytest
from task2 import integer_operations, floating_point_operations, string_operations, bool_operations

class TestIntClass:
    """Class for testing integer operations"""

    @pytest.mark.parametrize("first, second, expected", [(8,1,9), (5,3,8)])
    def test_int(self, first, second, expected):
        """
        Uses parameterized values to test and ensure correct output of integer_operations()

        Args:
            first: int
            second: int
            expected: int
        
        """

        test = integer_operations(first, second)

        assert test == expected, f'Expected return value to be {expected}'

    @pytest.mark.parametrize("first, second", [(8.1,1), ('Hello',3)])
    def test_int_type(self, first, second):
        """
        Tests to see if TypeError is correctly raised
        
        Args:
            first: non int
            second: non int

        """
        with pytest.raises(TypeError):
            integer_operations(first, second)


class TestFloatClass:
    """Class for testing floating point operations"""

    @pytest.mark.parametrize("value, expected", [(9.5, 9.0), (5.5, 5.0)])
    def test_float(self, value, expected):
        """
        Uses parameterized values to test and ensure correct output of floating_point_operations()
        
        Args:
            value: float
            expected: float
        
        """

        test = floating_point_operations(value)

        assert test == expected, f'Expected return value to be {expected}'

    @pytest.mark.parametrize("input", [8, 'Hi'])
    def test_float_type(self, input):
        """
        Tests to see if TypeError is correctly raised
        
        Args:
            input: non float
        
        """

        with pytest.raises(TypeError):
            floating_point_operations(input)

class TestStringClass:
    """Class for testing string operations"""

    @pytest.mark.parametrize("first, second, expected", [('Hello ', 'Bye ', 'Hello Bye Hello Bye Hello Bye '), 
    ('Good ', 'Bye ', 'Good Bye Good Bye Good Bye ')])
    def test_string(self, first, second, expected):
        """
        Uses parameterized values to test and ensure correct output of string_operations()

        Args:
            first: string
            second: string
            expected: string

        """
        test = string_operations(first, second)

        assert test == expected, f'Expected return value to be {expected}'
    
    @pytest.mark.parametrize("first, second", [('Hello', 9.5), ('Hi', True)])
    def test_string_type(self, first, second):
        """
        Tests to see if TypeError is correctly raised
        
        Args:
            first: non string
            second: non string
        
        """
        with pytest.raises(TypeError):
            string_operations(first, second)

    @pytest.mark.parametrize("first, second", [('Hello', ''), ('Hi', '')])
    def test_string_empty(self, first, second):
        """
        Tests to see if ValueError is correctly raised (No empty strings allowed)

        Args:
            first: string
            second: string
        
        """

        with pytest.raises(ValueError):
            string_operations(first, second)

class TestBoolClass:
    """Class for testing boolean operations"""

    @pytest.mark.parametrize("first, second, expected", [(True, True, False), (False, False, True), (False, True, False),
    (True, False, False)])
    def test_bool(self, first, second, expected):
        """
        Uses parameterized values to test and ensure correct output of bool_operations()

        Args:
            first: bool
            second: bool
            expected: bool

        """
        test = bool_operations(first, second)

        assert test == expected, f'Expected return value to be {expected}'

    @pytest.mark.parametrize("first, second", [(5, False), ('Hi', True)])
    def test_bool_type(self, first, second):
        """
        Tests to see if TypeError is correctly raised
        
        Args:
            first: non bool
            second: non bool

        """
        with pytest.raises(TypeError):
            bool_operations(first, second)