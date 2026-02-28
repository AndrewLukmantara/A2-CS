
def reverseString(string):

    if string == "":
        return ""
    else:
     
        return(reverseString(string[1:]) + string[0])

str = "cat"
print(reverseString(str))


# Winding
# function call        return statement

# reverseString(cat)   reverseString(at) + c
# reverseString(at)    reverseString(t) + a
# reverseString(t)     reverseString() + t
# reverseString(0)     

# Unwinding
# function call        return statement

# reverseString(0)    
# reverseString(t)     t
# reverseString(at)    ta
# reverseString(cat)   tac