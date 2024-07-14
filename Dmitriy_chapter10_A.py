class Money:
    def __init__(self, amount: float, currency: str):
        # Initialize the Money object with a specific amount and currency.
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        # Add two Money objects if they have the same currency.
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            # Write error if the currencies do not match together.
            raise TypeError("Cannot add Money of different currencies")

    def __sub__(self, other):
        # Subtract two Money objects if they have the same currency otherwise print error.
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            # Raise an error if the currencies do not match
            raise TypeError("Cannot subtract Money of different currencies")

    def __mul__(self, multiplier: float):
        # Multiply the amount by a numeric value (int or float).
        if isinstance(multiplier, (int, float)):
            return Money(self.amount * multiplier, self.currency)
        else:
            # Raise an error if the multiplier is not a number.
            raise TypeError("Multiplier must be a number")

    def __repr__(self):
        # Provide a string representation of the Money object.
        return f"{self.amount} {self.currency}"

# Test function to verify the Money class operations.
def test_money_operations():
    # Create Money objects.
    m1 = Money(90, 'USD')
    m2 = Money(60, 'USD')
    m3 = Money(100, 'EUR')

    # Test addition
    try:
        result = m1 + m2
        print(f"Addition result: {result}")  # Expected Amount: 150 USD
    except TypeError as e:
        print(e)

    try:
        result = m1 + m3
        print(f"Addition result: {result}")
    except TypeError as e:
        print(e)  # Expected: Cannot add Money of different currencies

    # Test subtraction
    try:
        result = m1 - m2
        print(f"Subtraction result: {result}")  # Expected: 30 USD
    except TypeError as e:
        print(e)

    try:
        result = m1 - m3
        print(f"Subtraction result: {result}")
    except TypeError as e:
        print(e)  # Expected: Cannot subtract Money of different currencies

    # Test multiplication
    try:
        result = m1 * 2
        print(f"Multiplication result: {result}")  # Expected: 180 USD
    except TypeError as e:
        print(e)

    try:
        result = m1 * '2'
        print(f"Multiplication result: {result}")
    except TypeError as e:
        print(e)  # Expected: Multiplier must be a number

if __name__ == "__main__":
    # Run the test function to verify Money class.
    test_money_operations()
