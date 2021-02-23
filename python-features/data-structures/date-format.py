
# Objective
# In this challenge, we practice converting the datetype.

# We would like to normalise the int value to the specyfic format of a datetype.

# This produces a formatted string like:
# Thu_Nov_24:18:22:48_1986


from datetime import datetime

def normalise(input_time):

    str_time = datetime.fromtimestamp(int(input_time)/1000.0)

    str_time = str_time.strftime("%a_%b_%d:%H:%M:%S_%Y")

    return str_time
    
if __name__ == '__main__':
    x = 1614117133273
    print(normalised(x))


# python [filename].py