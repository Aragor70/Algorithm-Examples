
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the probability of a compound event. 

# There are  urns labeled , , and .
# Urn X contains 4 red balls and 3 black balls.
# Urn Y contains 5 red balls and 4 black balls.
# Urn Z contains 4 red balls and 4 black balls.

# One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

a = 10 / 63
b = 2 / 7
c = 17 / 42
d = 31 / 126


# For this example we need draw some table.

# urns | Red | Black    | sum

#   x     4     3       =   7
#   y     5     4       =   9
#   z     4     4       =   8

# probability for red in 4 / 7, for black is 3 / 7
# probability for red in 5 / 9, for black is 4 / 9
# probability for red in 4 / 8, for black is 4 / 8


# probability to get 2 red and 1 black is:
# (4 / 7) * (5 / 9) * (4 / 8) + (4 /7) * (5 / 9) * (4 / 8) + (3 / 7) * (4 / 9) * (4 / 8) = 17 / 42

# c = 17 / 42
