#This function creates the 8 ball file.
def create_8ball_responses_file():
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]
    with open('8ball_responses.txt', 'w') as file:
        for response in responses:
            file.write(response + '\n')

# Run this function to create the file
create_8ball_responses_file()




