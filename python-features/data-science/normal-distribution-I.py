
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the normal distributions.

# In a certain plant, the time taken to assemble a car is a random variable, X, 
# having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
# What is the probability that a car can be assembled at this plant in:

# Less than 19.5 hours?
# Between 20 and 22 hours?

# Gauss error function => math.erf(x)
# https://docs.python.org/3/library/math.html#math.erf

import math

def distribution(mean, std, x):
    return ( 0.5 * (1 + math.erf((x - mean)/( std * 2 ** 0.5))) )
           
average = 20

deviation = 2

value_A = distribution(average, deviation, 19.5)

value_B = distribution(average, deviation, 20)
value_C = distribution(average, deviation, 22)

print(round(value_A, 3))
print(round(value_C - value_B, 3))


# python [filename].py