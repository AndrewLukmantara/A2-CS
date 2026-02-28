def countdown(num):
    if num == 0:
        print("Done")
    else:
        countdown(num-1)
        print(num)
    
countdown(3)


# function call         print statement     # function call 2


# countdown(3)          3                   # countdown(2)
# countdown(2)          2                   # countdown(1)
# countdown(1)          1                   # countdown(0)
# countdown(0)          Done                None

