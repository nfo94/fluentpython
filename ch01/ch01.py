import collections
from random import choice

# namedtuple(): factory function for creating tuple subclasses with named fields
# tuple: collection which is ordered and unchangeable, written with round brackets,
# and allow duplicate values
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # why split like this instead of just creating a list with the strings? is this about
    # performance stuff?
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        # are we adding a variable to self, which is the own object? can i say this is a
        # new property?
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # i've read somewhere that ovewriting special methods is not a good idea. is this it?
    # or it got nothing to do with it and we're actually creating special methods for this
    # new object called FreanchDeck?
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card("7", "diamonds")
print(beer_card)
deck = FrenchDeck()
print(choice(deck))
print(choice(deck))

# "Because our __getitem__ delegates to [] operator of self._cards, our deck automatically
# supports slicing". ???

print(deck[:3])

# "Because our __getitem__ delegates to [] operator of self._cards, our deck automatically
# supports slicing". ???
