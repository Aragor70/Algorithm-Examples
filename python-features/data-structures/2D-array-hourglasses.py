
# Part of Data Structures algorithms at https://www.hackerrank.com/

# Objective
# In this challenge, we practice calculating the hourglasses sum from a 2D array.

# [
#   [1, 1, 1, 0, 0, 0], 
#   [0, 1, 0, 0, 0, 0], 
#   [1, 1, 1, 0, 0, 0], 
#   [0, 0, 2, 4, 4, 0], 
#   [0, 0, 0, 2, 0, 0], 
#   [0, 0, 1, 2, 4, 0]
# ]

# In this case, we would like to get the sum of every hourglass from this 2D array.

# 1, 1, 1
#    1
# 1, 1, 1

# We would like to get them all and search for the maximum sum.

# For that, we can use for loop two times to get the rows and columns.

# Next would be searching for the single hourglass and sum every record.

# And then we will return the highest sum to the console.


def hourglassSum(arr):
    
    arry = arr
    
    values = []
    
    for i in range(4):
        for j in range(4):
            
            value = arry[i][j] + arry[i][j+1] + arry[i][j+2] + arry[i+1][j+1] + arry[i+2][j] + arry[i+2][j+1] + arry[i+2][j+2]
        
            values.append(value)
            
    return max(values)
    

arr = [
    [1, 1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0], 
    [0, 0, 2, 4, 4, 0], 
    [0, 0, 0, 2, 0, 0], 
    [0, 0, 1, 2, 4, 0]
]

print(hourglassSum(arr))


# python [filename].py