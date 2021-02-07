import numpy as np


# The following method is a solution to search a value from a huge values collection. 
# The binary search technique requires an array of sorted values.

# In this example, we would like to search for a value from an array of random numbers.

position = 0

def search(arry, x):

    first = 0

    last = len(arry) - 1

    while first <= last:

        median = ( first + last ) // 2

        if arry[median] == x:
            globals()['position'] = median
            return True

        else:
            if arry[median] < x:
                first = median + 1
            else:
                last = median - 1
    
    return False

# get random sorted values with numpy

a = sorted(np.random.randint(100, size=60))

print(f'Given array: {a}')

if search(a, 99):
    print(f""" 
    Value found at {position} index
     """)

else:
    print(""" 
    Value not found. 
    """)

