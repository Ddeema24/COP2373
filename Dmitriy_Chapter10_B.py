class Money:
    def __init__(self, amount: float, currency: str):
        # Initialize the Money object with a specific amount and currency
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        # Add two Money objects if they have the same currency
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            # Raise an error if the currencies do not match
            raise TypeError("Cannot add Money of different currencies")

    def __sub__(self, other):
        # Subtract two Money objects if they have the same currency
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            # Raise an error if the currencies do not match
            raise TypeError("Cannot subtract Money of different currencies")

    def __mul__(self, multiplier: float):
        # Multiply the amount by a numeric value (int or float)
        if isinstance(multiplier, (int, float)):
            return Money(self.amount * multiplier, self.currency)
        else:
            # Raise an error if the multiplier is not a number
            raise TypeError("Multiplier must be a number")

    def __repr__(self):
        # Provide a string representation of the Money object
        return f"{self.amount} {self.currency}"

class BankAcct:
    def __init__(self, initial_balance: float, currency: str):
        # Initialize the BankAcct object with an initial balance and currency
        self.balance = Money(initial_balance, currency)

    def deposit(self, amount: float):
        # Deposit a specified amount to the account balance using the Money class's add method
        self.balance = self.balance + Money(amount, self.balance.currency)

    def withdraw(self, amount: float):
        # Withdraw a specified amount from the account balance using the Money class's subtract method
        self.balance = self.balance - Money(amount, self.balance.currency)

    def __repr__(self):
        # Provide a string representation of the BankAcct object
        return f"BankAcct(balance={self.balance})"

# Test function to verify the BankAcct class operations
def test_bank_acct_operations():
    # Create a BankAcct object with an initial balance
    acct = BankAcct(100, 'USD')

    # Test deposit
    try:
        acct.deposit(50)
        print(f"Deposit result: {acct}")  # Expected: 150 USD
    except TypeError as e:
        print(e)

    # Test withdraw
    try:
        acct.withdraw(30)
        print(f"Withdraw result: {acct}")  # Expected: 120 USD
    except TypeError as e:
        print(e)

    # Test over-withdraw
    try:
        acct.withdraw(200)
        print(f"Withdraw result: {acct}")
    except TypeError as e:
        print(e)  # Expected: Cannot subtract Money of different currencies (if not enough balance)

if __name__ == "__main__":
    # Run the test function to verify BankAcct class operations
    test_bank_acct_operations()

