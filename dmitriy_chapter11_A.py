import random

# Define the Card class
class Card:
    # Class variables for suits and ranks
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define the Deck class
class Deck:
    def __init__(self):
        # Create a deck of 52 cards
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)  # Shuffle the deck

    def deal(self, num):
        # Deal 'num' cards from the deck
        dealt_cards = []
        for _ in range(num):
            dealt_cards.append(self.cards.pop())
        return dealt_cards

# Define the PokerHand class
class PokerHand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def replace(self, indices, new_cards):
        # Replace cards at given indices with new cards
        for i, new_card in zip(indices, new_cards):
            self.cards[i] = new_card

def main():
    # Create a deck and deal a hand of five cards
    deck = Deck()
    hand = PokerHand(deck.deal(5))

    print("Your hand:")
    print(hand)

    # Prompt user for cards to replace
    indices = input("Enter the positions (1-5) of the cards you want to replace, separated by spaces: ").split()
    indices = [int(index) - 1 for index in indices]  # Convert to zero-based index

    # Deal new cards and replace selected cards
    new_cards = deck.deal(len(indices))
    hand.replace(indices, new_cards)

    print("\nYour new hand:")
    print(hand)

# Entry point of the program
if __name__ == "__main__":
    main()
