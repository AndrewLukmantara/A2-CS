def Unknown(X, Y : int):
    if X < Y:
        print(X + Y)
        return(Unknown(X + 1, Y) * 2)
    elif X == Y:
        return 1
    else:   
        print(X + Y)
        return(Unknown(X - 1, Y) // 2)

print("X : 10, Y : 15")
print(f"Return : {Unknown(10,15)}")

print("X : 10, Y : 10")
print(f"Return : {Unknown(10,10)}")

print("X : 15, Y : 10")
print(f"Return : {Unknown(15,10)}")

print("\n")

def IterativeUnknown(X, Y : int):

    n = 0 # INTEGER

    while X != Y:

        if X < Y:
            print(X + Y)
            X = X + 1
            n = n + 1

        else:
            print(X + Y)
            X = X - 1
            n = n - 1

    return(int(2 ** n))
    

print("X : 10, Y : 15")
print(f"Iterative Return : {IterativeUnknown(10,15)}")
    
    
print("X : 10, Y : 10")
print(f"Iterative Return : {IterativeUnknown(10,10)}")


print("X : 15, Y : 10")
print(f"Iterative Return : {IterativeUnknown(15,10)}")




