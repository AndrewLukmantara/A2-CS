def countDigits(n):
    if n < 10:
        return 1
    else:
        return (1 + countDigits(int(n/10)))
    
print(countDigits(54321))