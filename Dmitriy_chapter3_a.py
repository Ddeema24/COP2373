from functools import reduce


#Function to collect expenses from the user.
def get_expenses():
    #List to store the expenses.
    expenses = []
    while True:
        #Ask user for the type of expense.
        expense_type = input('Enter the type of expense (or "done" to finish):' )
        if expense_type.lower() == 'done': #Break the loop since the user wants to finish.
            break
        try:
            #Ask the user to enter the amount of the expense.
            amount = float(input(f'Enter the amount for {expense_type}:'))
            # Append the expense as a tuple.
            expenses.append((expense_type, amount))
        except ValueError:
            #Adding this ensures there are no invalid inputs.
            print('Please enter a valid amount. ')
    return expenses 

def calculate_total(expenses):
    #Use reduce to sum up all the amounts of expenses.
    return reduce(lambda acc, expense: acc + expense[1], expenses, 0)

def find_highest(expenses):
    # Use reduce to find the expense with the highest amount,
    return reduce(lambda highest, expense: expense if expense[1] > highest[1] else highest, expenses)

def find_lowest(expenses):
    # Use reduce to find the expense with the lowest amount.
    return reduce(lambda lowest, expense: expense if expense[1] < lowest[1] else lowest, expenses)

def main():
    #Get expense list from user.
    expenses = get_expenses()
    #Check to see if the user enetered any expenses.
    if not expenses:
        print('No expenses entered. ')
        return
    
# Calculate the total expense using the calculate_total function.
    total_expense = calculate_total(expenses)

# Find the highest expense using the find_highest function.
    highest_expense = find_highest(expenses)

# Find the lowest expense using the find_lowest function
    lowest_expense = find_lowest(expenses)

    #Print the total expenses.
    print(f"\nTotal expense: ${total_expense:.2f}")

    #Print the highest expense amount with its type.
    print(f'Highest expense: {highest_expense[0]} - ${highest_expense[1]:.2f}')

    # Print the lowest expense with its type.
    print(f"Lowest expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

#Call main function.
if __name__ == "__main__":
     main()