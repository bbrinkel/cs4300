def integer_operations(first_int, second_int):
    """
        Showcases integer operations with two entered ints (first - second + (2 * second)).

        Args:
            FirstInt: int
            SecondInt: int

        returns integer
    
    """

    # Ensuring entered types are integers only
    if not isinstance(first_int, int) or not isinstance(second_int, int):
        raise TypeError('Expected two integers')

    # Performing random operations with integers to be tested
    third_int = first_int - second_int
    third_int += (second_int * 2)

    return third_int

# Showcases floating point operations with two entered floats
def floating_point_operations(input_float):
    """
        Showcases floating point operations with entered float (floor(input * 2 + 0.75)).

        Args:
            input_float: float

        returns floating point
    
    """

    # Ensuring entered type is float only
    if not isinstance(input_float, float):
        raise TypeError('Expected floating point value')

    # Performing random operations with floating point value to be tested
    ret_value = input_float * 2
    ret_value += 0.75
    ret_value = ret_value // 2

    return ret_value

def string_operations(string_one, string_two):
    """
        Showcases string operations with two entered strs (concatenates first and second then multiplies by 3)

        Args:
            string_one: str
            string_two: str

        returns string
    
    """

    # Ensuring entered types are strings only
    if not isinstance(string_one, str) or not isinstance(string_two, str):
        raise TypeError('Expected two strings')

    # Ensuring strings entered are not empty
    if len(string_one) == 0 or len(string_two) == 0:
        raise ValueError('Cannot have empty strings')

    # Performing random operations with strings to be tested
    string_three = string_one + string_two
    string_three *= 3

    return string_three

def bool_operations(bool_one, bool_two):
    """
        Showcases boolean operations with two entered bools (nots both inputs and ands them together to get the returned value)

        Args:
            bool_one: bool
            bool_two: bool

        returns boolean
    
    """

    # Ensuring entered types are bools only
    if not isinstance(bool_one, bool) or not isinstance(bool_two, bool):
        raise TypeError('Expected two bools')

    # Performing random operations with bools to be tested
    bool_three = not bool_one
    bool_four = not bool_two
    bool_five = (bool_three and bool_four)

    return bool_five

# Main, prints the outcomes of each function
if __name__ == "__main__":
    print(f"After integer operations with 8 and 1: {integer_operations(8, 1)}")
    print(f"After floating point operations with 9.5: {floating_point_operations(5.5)}")
    print(f"After string operations with 'Hello ' and 'Bye ': {string_operations('Hello ', 'Bye ')}")
    print(f"After bool operations with True and False: {bool_operations(True, False)}")
    print()
