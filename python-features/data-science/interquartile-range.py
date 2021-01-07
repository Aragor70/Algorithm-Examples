
# Part of 10 Days of Statistics at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the interquartile range.

# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

# Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, construct a data set, S, where each xi occurs at frequency fi. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

# median, q2 = sum of two middle values of sorted array half = (list[N // 2])
# q1 = median of the first part of sorted array
# q3 = median of the second part of sorted array


import statistics as st
import math

print("Enter length of time series.")
n = int(input())

print("Enter space-separated integers values of time series.")
values = list(input().split())

print("Enter space-separated integers values of frequences.")
freq = list(map(int, input().split()))

dataset = []

for i in range(n):
    dataset.append((values[i] + ' ' ) * freq[i])
    
cleaning = []
for i in range(n):
    cleaning.append(dataset[i].split())

data = []
for i in range(n):
    data += cleaning[i]
    
data = sorted(list(map(int, data)))

q1 = st.median(data[:int(len(data) // 2)])

q3 = 0

if len(data) % 2 == 0:
    q3 = st.median(data[len(data) // 2:])
else:
    q3 = st.median(data[len(data) // 2 + 1:])

print(round(float(q3 - q1), 1))

    
# python [filename].py