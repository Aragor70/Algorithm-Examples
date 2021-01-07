
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the mean, median, and mode.

# Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
# If your array contains more than one modal value, choose the numerically smallest one.

# mean = sum of X integers values / N length of X array
# median = sum of two middle values of sorted array half = (list[N // 2])
# mode = the most popular duplication value of the list

import statistics as st
from scipy import stats

print("Enter length of time series.")
l = int(input())

print("Enter space-separated integers values of time series.")
arry = input()

the_mean = st.mean(list(map(int, arry.split())))
the_median = st.median(list(map(int, arry.split())))
the_mode = int(stats.mode(list(map(int, arry.split())))[0])

print(the_mean)
print(the_median)
print(the_mode)


# python [filename].py