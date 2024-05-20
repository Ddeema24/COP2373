import random
#Function to read responses from the 8ball file.
def read_responses():
    # Open the file '8ball_responses.txt' in read mode
    with open('8ball_responses.txt', 'r') as file:
        responses = file.readlines()
        #strip any trailing whitespace characters from each response.
    responses = [response.strip() for response in responses]
    return responses
# Function to simulate the Magic 8 Ball game.
def magic_8_ball():
    responses = read_responses()
#Print a welcome message. Which also says how to quit the program if the user wishes to exit.
    print("Welcome to the Magic 8 Ball game! Ask your yes/no question or type 'quit' to exit.")

    while True:
        question = input("What's your question? Or type 'quit' to end the game.")
    #This if statement checks if the user said quit or if he choses to continue playing.
        if question.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        else:
            answer = random.choice(responses)
            print(f"Magic 8 Ball says: {answer}")
#Calling the main function to run the game.
magic_8_ball()
