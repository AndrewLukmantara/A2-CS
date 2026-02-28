def sumOfNaturalNumbers(num):
    if num == 1:
        return 1
    else:
        return(num + sumOfNaturalNumbers(num-1))
    
print(sumOfNaturalNumbers(3))


# Winding
# function call             return statement

# sumOfNaturalNumbers(3)    3 + sumOfNaturalNumbers(2)
# sumOfNaturalNumbers(2)    2 + sumOfNaturalNumbers(1)
# sumOfNaturalNumbers(1)    1 + sumOfNaturalNumbers(0)

# Unwinding
# function call             return statement

# sumOfNaturalNumbers(1)    1
# sumOfNaturalNumbers(2)    2 + 1 = 3
# sumOfNaturalNumbers(3)    3 + 3 = 6