
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the geometric distributions.



# The probability that a machine produces a defective product is 1 /3. 
# What is the probability that the 1st defect is found during the first 5 inspections?



def distribution(n, p, q):
    return ( 1 - q ** n )

p = 1 / 3
n = 5
q = 1 - p

value = distribution(n, p, q)

print(round(value, 3))


# python [filename].py