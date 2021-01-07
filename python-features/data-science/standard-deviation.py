
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the standard deviation.

# Given an array, X, of N integers, calculate and print the standard deviation. 
# Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). 
# An error margin of +0.1 will be tolerated for the standard deviation.




import statistics as st
import math

print("Enter length of time series.")
n = int(input())


print("Enter space-separated integers values of time series.")
arry = list(map(int, input().split()))

value = 0

for i in range(n):
    calc = arry[i] - st.mean(arry)
    value += calc ** 2
    
value /= n
value = round(math.sqrt(value), 1)

print(value)


# python [filename].py