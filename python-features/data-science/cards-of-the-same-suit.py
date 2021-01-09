
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the combinations and permutations. 

# You draw 2 cards from a standard 52-card deck without replacing them. 
# What is the probability that both cards are of the same suit?

a = 1 / 156
b = 1 / 39
c = 12 / 39
d = 12 / 51

# Player draw one card from 52 at first. Before the next take the length of card list reduced by one.

# 13 cards are the cards with the same type. 13 / 52
# When we take again we need the same color and figure.
# c = 12 / 51