def check_sign(number):
    """
    Checks the sign of a number, returns 'Positive', 'Negative', or 'Zero'.
    
        Args:
            number: int or float

        returns string of sign case
    
    """

    # Ensures entered type is a numerical value
    if not isinstance(number, (int, float)):
        raise TypeError('Expected a numerical value')

    # Choses result based on passed number
    case = ''
    if number > 0:
        case = 'Positive'
    elif number < 0:
        case = 'Negative'
    else:
        case = 'Zero'

    return case

def find_sum(input):
    """
    This function finds the sum of all numbers from 1 to n.
    
        Args:
            input: int

        returns sum of all numbers from 1 to input
    
    """

    # Raises error if input isn't an int
    if not isinstance(input, int):
        raise TypeError('Expected integer input value')

    # Raises error if input is negative
    if input <= 0:
        raise ValueError('Expected positive input')

    # Has an iterator for each iteration, and a sum where each iteration value is added to
    iterator = 1
    sum = 0
    # While the iterator is less than or equal to 100, add the iterator to the sum
    while iterator <= input:
        sum += iterator
        iterator += 1

    return sum

def find_primes(num_primes):
    """
    Prints out the first num_primes prime numbers.
    
        Args:
            num_primes: int

    """

    # Raises error if input isn't an int
    if not isinstance(num_primes, int):
        raise TypeError('Expected integer input value')

    # Raises error if input is negative
    if num_primes < 0:
        raise ValueError('Expected positive input')

    # Keeps track of an iterator to go through as many numbers as it takes,
    # and number of primes found to keep track of how many more are needed.
    iterator = 0
    primes = 0
    # While there are less than 10 primes found, keep finding them
    while primes < num_primes:
        # If prime number found, print it and increase primes var by 1
        if is_prime(iterator):
            print(iterator, end=' ')
            primes += 1
        
        # Iterates after every iteration no matter what
        iterator += 1
    
    print()

def is_prime(number):
    """
    Determines if the entered number is prime or not.
    
        Args:
            number: int

        returns True or False
    
    """

    ret_value = True
    # Because we know 1 and 0 are not prime and unique cases, return False if number is less than 2
    if number < 2:
        ret_value = False
    else:
        # Check if any numbers in the range of 2 to (number - 1) divide number, if they do, number is not prime.
        for i in range(2, number):
            if (number % i) == 0:
                ret_value = False
                break
    
    return ret_value

# Main, prints the outcomes of each function
if __name__ == "__main__":
    print('The first 10 primes:')
    find_primes(10)
    print()
    print(f'Sum of numbers from 1 to 100: {find_sum(100)}\n')
    print(f'Resulting sign of -27: {check_sign(-27)}')
    print(f'Resulting sign of 145: {check_sign(145)}')
    print(f'Resulting sign of 0: {check_sign(0)}\n')
