
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating a weighted mean. 

# Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, 
# calculate and print the weighted mean of X's elements. 
# Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

# mean = sum of X integers values / N length of X array

print("Enter length of time series.")
l = int(input())

print("Enter space-separated integers values of time series.")
arry = list(input().split())


print("Enter space-separated integers values of weights.")
weights = list(input().split())

value = 0
weight_sum = 0

for i in range(l):
    value += (int(arry[i]) * int(weights[i]))
    weight_sum += int(weights[i])

value /= weight_sum

print(round(value, 1))


# python [filename].py