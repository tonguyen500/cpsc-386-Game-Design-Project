import random
import pygame
print("Hello World")

class Card:
    def __init__(self,suit,val,img):
        self.suit = suit
        self.value = val
        self.img = img
    def show(self):
        print("{} of {} {}".format(self.value, self.suit, self.img))
    def __eq__(self, other):
        return self.img == other.img
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        # for s in ["Potato Cat", "Watermelon Cat", "Taco Cat", "Beard Cat", "Rainbow Cat"]:
        # for s in ["Potato Cat"]:
        for s in ["Beard Cat", "Watermelon Cat"]:
            for v in range(7):
                self.cards.append(Card(s,2, s+'.jpg'))
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self,card):
        self.hand.remove(card)

# card = Card("Clubs", 6)
# card.show()
# deck = Deck()
# deck.shuffle()
# deck.show()
# card = deck.draw()
# card.show()

# bob = Player("Bob")
# hand = 3
# for x in range(hand):
#     bob.draw(deck)
# bob.showHand()
# print()
# jim = Player("Jim")
# for x in range(hand):
#     jim.draw(deck)
# jim.showHand()
# print()
# # deck.show()
# # bob.discard(bob.hand[0])
# # bob.showHand()
# print()
# try:
#     bob.discard(Card("","","bearjpg"))
# except:
#     pass
# for x in bob.hand[:]:
#     if x.img == "Beard Cat.jpg":
#         bob.discard(x)
# bob.showHand()