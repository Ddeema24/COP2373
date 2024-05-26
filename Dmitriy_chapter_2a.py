#List of common spam words/phrases found.
spam_keywords = [
    "free", "winner", "congratulations", "claim", "prize", "urgent", "100% free",
    "click here", "act now", "limited time", "offer expires", "guaranteed", 
    "risk-free", "money back", "investment", "special promotion", "cash bonus",
    "earn money", "extra income", "cheap", "discount", "order now", "best price",
    "no cost", "free gift", "incredible deal", "promotion", "unsubscribe",
    "this is not spam", "remove me"
]
#Function to keep the score.
def get_spam_score(message):
    score = 0
    found_keywords = []
#Make sure to put .lower to convert message to lowercase for case-insensitive comparison.
    message_lower = message.lower()

    for  keyword in spam_keywords:
        if keyword in message_lower:
            score += 1
            found_keywords.append(keyword)
    return score, found_keywords

#Function to calculate the likelihood that the message is a scam.
def rate_spam_likelihood(score):
    if score == 0:
        return 'Not Spam'
    elif score <= 3:
        return "Low likelihood of being Spam"
    elif score <= 6:
        return "Medium likelihood of being Spam"
    elif score <= 10:
        return "High likelihood of being Spam"
    else:
        return "Very High likelihood of being Spam"
    
def main():
    # Get user input
    message = input("Enter the email message: ")
    
    # Calculate spam score and get found keywords
    spam_score, found_keywords = get_spam_score(message)
    
    # Rate the likelihood of spam
    spam_likelihood = rate_spam_likelihood(spam_score)
    
    # Display results
    print(f"\nSpam Score: {spam_score}")
    print(f"Spam Likelihood: {spam_likelihood}")
    if found_keywords:
        print(f"Keywords found: {', '.join(found_keywords)}")
    else:
        print("No spam keywords found.")
#Call main function to run the program
if __name__ == "__main__":
    main()