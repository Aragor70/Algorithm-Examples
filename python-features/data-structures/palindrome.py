
# Objective
# In this challenge, we produce palindrome function to print if given value is an palindrome value.

# In this task we will create two different examples.

# One function would convert string value
# The second function would convert int number

# The output will be True or False


def palindrome_STR(value):

    return value[::-1] == value

def palindrome_NUM(value):

    x = int(value)

    temp = x

    reverse = 0

    while (x > 0):
        dig = x % 10
        
        reverse = reverse * 10 + dig

        x = x // 10

    return temp == reverse


if __name__ == '__main__':

    print(palindrome_STR('bambino'))
    print(palindrome_NUM(1234567890))


# python [filename].py