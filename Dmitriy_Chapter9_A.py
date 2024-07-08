class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        # Initializes a new bank account.
        # :param name: Account holder's name
        # :param account_number: Account number
        # :param amount: Initial amount in the account
        # :param interest_rate: Interest rate in percentage
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        # Adjusts the interest rate of the account.
        # :param new_rate: New interest rate in percentage
        self.interest_rate = new_rate

    def withdraw(self, amount):
        # Withdraws an amount from the account.
        # :param amount: Amount to withdraw
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount

    def deposit(self, amount):
        # Deposits an amount into the account.
        # :param amount: Amount to deposit
        self.amount += amount

    def get_balance(self):
        # Returns the current balance of the account.
        # :return: Current balance
        return self.amount

    def calculate_interest(self, days):
        # Calculates the interest earned over a given number of days.
        # :param days: Number of days
        # :return: Interest earned
        return self.amount * (self.interest_rate / 100) * (days / 365)

    def __str__(self):
        # Returns a string representation of the account details.
        # :return: Account details as a string
        return f"Account Holder: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}\nInterest Rate: {self.interest_rate:.2f}%"

def test_bank_acct():
    # Tests the BankAcct class methods.
    
    # Create a new bank account
    account = BankAcct("Sarah Jones", "123456789", 1000.0, 1.5)
    print(account)

    # Adjust interest rate
    account.adjust_interest_rate(2.0)
    print("\nAdjusted Interest Rate:")
    print(account)

    # Deposit money
    account.deposit(500.0)
    print("\nAfter Deposit:")
    print(account)

    # Withdraw money
    account.withdraw(300.0)
    print("\nAfter Withdrawal:")
    print(account)

    # Check balance
    balance = account.get_balance()
    print(f"\nBalance: ${balance:.2f}")

    # Calculate interest for 30 days
    interest = account.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

# Run the test function
if __name__ == "__main__":
    test_bank_acct()
