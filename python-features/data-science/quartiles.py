
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating a weighted mean. 

# Given an array, S, of n integers, 
# calculate the respective first quartile (Q1), 
# second quartile (Q2 or M), 
# and third quartile (Q3). 
# It is guaranteed that Q1, Q2 or M, and Q3 are integers.

# median, q2 = sum of two middle values of sorted array half = (list[N // 2])
# q1 = median of the first part of sorted array
# q3 = median of the second part of sorted array


import statistics as st
import math

print("Enter length of time series.")
l = int(input())

print("Enter space-separated integers values of time series.")
arry = sorted(list(map(int, input().split())))
the_median = st.median(arry)


q1 = print(math.floor(st.median(arry[:l // 2])))

q2 = print(math.floor(the_median))
q3 = 0
if l % 2 == 0:
    q3 = print(math.floor(st.median(arry[l // 2:])))
else:
    q3 = print(math.floor(st.median(arry[(l // 2) + 1:])))


    
# python [filename].py