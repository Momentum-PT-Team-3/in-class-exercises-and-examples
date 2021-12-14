import random

SUITS = ["♥️", "♦️", "♠️", "♣️"]
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self, suits, ranks): 
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def __str__(self):
        return [str(card) for card in self.cards]
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self, player):
        player.hand.append(self.cards.pop())


class Player:
    def __init__(self, is_dealer=False):
        self.name = 'Dealer' if is_dealer else input("What is your name? ")
        self.is_dealer = is_dealer
        self.hand = []

    def __str__(self):
        return self.name

    def show_hand(self):
        print(f"{self.name}'s hand is: ")
        for card in self.hand:
            print(card)

    def sum_hand(self):
        face_cards = ["J", "Q", "K"]
        score = 0
        for card in self.hand:
            if card.rank in face_cards:
                score += 10
            elif card.rank != "A":
                score += card.rank
            elif card.rank == "A" and score < 10:
                card.rank += 11
            else:
                score.rank += 1
        return score

class Game:
    def __init__(self):
        self.dealer = Player(is_dealer=True)
        self.player = Player()
        self.deck = Deck(SUITS, RANKS)

    def __str__(self):
        return f"{self.dealer}'s hand is {self.dealer.show_hand()} and {self.player}'s hand is {self.player.show_hand()}"

    def deal(self):
        self.deck.shuffle()
        for i in range(2):
            self.deck.deal_card(self.player)
            self.deck.deal_card(self.dealer)


game = Game()
game.deal()
print(game)

