import random

def read_responses():
    with open('8ball_responses.txt', 'r') as file:
        responses = file.readlines()
    responses = [response.strip() for response in responses]
    return responses

def magic_8_ball():
    responses = read_responses()
    print("Welcome to the Magic 8 Ball game! Ask your yes/no question or type 'quit' to exit.")
    
    while True:
        question = input("What's your question? ")
        if question.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        else:
            answer = random.choice(responses)
            print(f"Magic 8 Ball says: {answer}")

magic_8_ball()
