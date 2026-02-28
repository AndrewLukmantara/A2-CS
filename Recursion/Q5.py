def baseRaisedToExponent(base, exp):
    if exp == 1:
        return base * exp
    else:
        return (base * baseRaisedToExponent(base, exp - 1))
    

print(baseRaisedToExponent(2, 3))

# Winding
# function call        return statement

# baseRaisedToExponent(2, 3)    2 * baseRaisedToExponent(2, 2)
# baseRaisedToExponent(2, 2)    2 * baseRaisedToExponent(2, 1)
# baseRaisedToExponent(2, 1)    2 * 1

# Unwinding
# function call        return statement

# baseRaisedToExponent(2, 1)    2 * 1 = 2
# baseRaisedToExponent(2, 2)    2 * 2 = 4
# baseRaisedToExponent(2, 3)    2 * 4 = 8