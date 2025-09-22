def calculate_discount(price, discount):
    """
        Calculates a discounted price given two values. One for the price and one for the discount.
    
        Args:
            price: int or float
            discount: int or float

        returns discounted price
    
    """

    # Raises a TypeError if price or discount are not numerical values
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError('Expected numerical values')

    # Raises a ValueError if discount is negative or over 100%
    if discount > 100 or discount < 0:
        raise ValueError('Invalid Discount, must be between 0 and 100')

    # Raises a valueError if price is less than or equal to 0
    if price <= 0:
        raise ValueError('Invalid Price, must be greater than 0')

    # Gets amount of money off and subtracts by the original price
    applied_discount = price * (discount / 100)
    final_price = price - applied_discount

    return round(final_price, 2)

# Main, tests different calculations with floats and ints
if __name__ == "__main__":
    print(f'Applying discount of 25% to $46 purchase: ${calculate_discount(46, 25)}')
    print(f'Applying discount of 33% to $101.55 purchase: ${calculate_discount(101.55, 33)}')
    print(f'Applying discount of 33.67% to $94 purchase: ${calculate_discount(94, 33.67)}')
    print(f'Applying discount of 45.5% to $200.10 purchase: ${calculate_discount(200.10, 45.5)}')
    print()