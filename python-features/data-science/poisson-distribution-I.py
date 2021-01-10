
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the Poisson distributions.

# A random variable, X, follows Poisson distribution with mean of 2.5. 
# Find the probability with which the random variable X is equal to 5.

# math.factorial => !5 => 1 * 2 * 3 * 4 * 5

import math

def distribution(k, l):
    return ( (l ** k) * (math.e ** ( 0 - l )) ) / math.factorial(k)

l = 2.5
k = 5

value = distribution(k, l)

print(round(value, 3))


# python [filename].py