
#Defining selling tickets function.

def selling_tickets():

#Total tickets to keep track of the remaing tickets and total buyers to keep track of the buyers starting at 0.
    total_tickets = 20
    total_buyers = 0

#Creating a while loop
    while total_tickets > 0:
        try:
            tickets_requested = int(input(f'There are {total_tickets} tickets remaining. How many tickets would you like to buy? (1-4): '))

            if 1 <= tickets_requested <=4:

                if tickets_requested <=total_tickets:
                    total_tickets -= tickets_requested
                    total_buyers += 1
                    print(f'You have successfully purchased {tickets_requested} tickets.')
                    print(f'{total_tickets} tickets remaining./n')
                else:
                    print(f'Sorry, only {total_tickets} tickets are remaining. Please try again. ')
            else:
                print(f'Invalid number of tickets requested. Please keep a minimum of 1-4 tickets. ')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 4.\n')


    print("All tickets have been sold.")
    print(f"Total number of buyers: {total_buyers}")

if __name__ == "__main__":
    selling_tickets()


