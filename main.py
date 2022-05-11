import random
print "hello world"

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print "{} of {}".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["spades", "clubs", "diamonds", "hearts"]:
            for v in range(1,9):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r], = self.cards[r], self.cards[i]


    def drawCard(self):
        return self.cards.pop()


class player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showhand(self):
        for card in self.hand:
            card.show()

#card = Card("Clubs", 6)
#card.show()
deck = Deck()
deck.shuffle()
deck.show()
deck.build()
deck.show()





#card = deck.draw()
#card.show()