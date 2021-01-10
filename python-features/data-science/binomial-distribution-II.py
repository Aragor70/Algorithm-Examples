
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the binomial distributions.

# A manufacturer of metal pistons finds that, on average, 12% of the pistons 
# they manufacture are rejected because they are incorrectly sized. 
# What is the probability that a batch of 10 pistons will contain:

# No more than 2 rejects?
# At least 2 rejects?

# math.factorial => !5 => 1 * 2 * 3 * 4 * 5

import math


def distribution(x, n, p):
    return ( math.factorial(n) / ( math.factorial(x) * math.factorial(n - x) ) ) * (p ** x) * ((1 - p) ** (n - x))

b = 0
p = 0.12
n = 10

for i in range(0, 3):
    b += distribution(i, n, p)

print(round(b, 3))

b = 0
for i in range(2, 11):
    b += distribution(i, n, p)

print(round(b, 3))



# python [filename].py