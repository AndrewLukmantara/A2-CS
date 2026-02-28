def Factorial(num):
    if num == 0:
        return 1
    else:
        return (num * Factorial(num-1))

print(Factorial(5))

# Winding
# function call   return statement

# Factorial(4)    4 * Factorial(3)
# Factorial(3)    3 * Factorial(2)
# Factorial(2)    2 * Factorial(1)
# Factorial(1)    1 * Factorial(0)
# Factorial(0)    1

# Unwinding
# function call   return statement

# Factorial(0)    1
# Factorial(1)    1 * 1
# Factorial(2)    2 * 1 = 2
# Factorial(3)    3 * 2 = 6
# Factorial(4)    4 * 6 = 24