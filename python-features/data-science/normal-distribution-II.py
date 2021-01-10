
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the normal distributions of Cumulative Probability.

# The final grades for a Physics exam taken by a large group of students have a mean of 70 
# and a standard deviation of 10. 
# If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:

# Scored higher than 80 (i.e., have a grade > 80)?
# Passed the test (i.e., have a grade >= 60)?
# Failed the test (i.e., have a grade < 60)?
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

# Gauss error function => math.erf(x)
# https://docs.python.org/3/library/math.html#math.erf


import math

def distribution(x, std, mean):
    return ( 0.5 * ( 1 + math.erf( ( x - mean) / ( 10 * (2 ** 0.5) ) )) )

value_A = distribution(80, 10, 70)

value_B = distribution(60, 10, 70)

print(round( (1 - value_A) * 100 , 2))
print(round( (1 - value_B) * 100 , 2))
print(round(value_B * 100, 2))


# python [filename].py