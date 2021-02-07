# Today consider the following version of Bubble Sort.

# The following method is to replace individual elements in the array. 
# By doing this technique multiple times with a loop statement we can sort the entire array.

# In this example, we would like to sort an array [ 1, 3, 2, 5 ] ascending.

# The replacement method that we will use is:


# Description of the process at [ 5, 2 ] point:

# temp = arry[x]            <- save the value of an element [ 5 ]
# arry[x] = arry[x + 1]     <- change value [ 5 ] => [ 2 ]
# arry[x + 1] = temp        <- define element [ 2 ] with the saved value [ 5 ]

# return [ 2, 5 ]

# ... repeat that process len(array) - 1 times descending => range(len(array) - 1, 0, -1)


def sort(array):
    
    arry = array.copy()
    
    for i in range(len(arry) - 1, 0, -1):
        
        for x in range(i):
            if arry[x] > arry[x + 1]:
                temp = arry[x]
                arry[x] = arry[x + 1]
                arry[x + 1] = temp
    
    return arry
    


print('Hi, Enter an array of values: ')

a = list(map(int, input().split(',')))

print(sort(a))
