# Intentionally flawed Python program

# importing modules
from itertools import product
from random import shuffle
# make a deck of cards
deck = list(product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
