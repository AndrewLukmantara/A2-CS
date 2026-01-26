myStack = [0 for _ in range(10)] # Stack of 10 elements
top = -1 # INTEGER
base = 0 # INTEGER

def push(num): # num : INTEGER
    global myStack, top, base
    if top != len(myStack)-1:
        top = top + 1
        myStack[top] = num
        print("Success")
    else:
        print("Unsuccessful")

def pop():  
    global myStack, top, base
    if top != -1:
        myStack[top ] = 0
        top = top - 1
        print("Success")
    
    else:
        print("Unsuccessful")

    
push(10)
push(2)
push(28)
push(23)
pop()
print(myStack)
