
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the Poisson distributions.

# The manager of a industrial plant is planning to buy a machine of either type A or type B. 
# For each day’s operation:

# The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
# The daily cost of operating A is Ca = 160 + 40 * (X ** 2).
# The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
# The daily cost of operating B is Cb = 128 + 40 * (X ** 2).

# Assume that the repairs take a negligible amount of time and the machines are maintained nightly
# to ensure that they operate like new at the start of each day. 
# Find and print the expected daily cost for each machine.

average_x = 0.88
average_y = 1.55

value_X = ( 160 + 40 * ( average_x + (average_x ** 2)) )
value_Y = ( 128 + 40 * ( average_y + (average_y ** 2)) )

print(round(value_X, 3))
print(round(value_Y, 3))

# python [filename].py