
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the binomial distributions.

# The ratio of boys to girls for babies born in Russia is . 
# If there is 1.09 : 1 child born per birth, 
# what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. 
# Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

# math.factorial => !5 => 1 * 2 * 3 * 4 * 5

import math

def distribution(x, n, p):
    return ( (math.factorial(n) / (math.factorial(x) * (math.factorial(n - x)))) * (p ** x) * ((1 - p) ** (n - x)) )

b = 0
    
for i in range(3, 7):
    b += distribution(i, 6, 1.09 / 2.09)
    
print(round(b, 3))


# python [filename].py