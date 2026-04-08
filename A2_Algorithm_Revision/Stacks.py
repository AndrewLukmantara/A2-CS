topPointer = -1
basePointer = 0

stack = [0 for _ in range(10)]

def Push(data : int):

    global topPointer, basePointer
    
    if topPointer == 9:
        return -1
    
    else:
        topPointer += 1
        stack[topPointer] = data
    
def Pop():

    global topPointer, basePointer
    
    if topPointer == - 1:
        return -1
    
    else:
        stack[topPointer] = 0
        topPointer -= 1


Push(1)
Push(2)
Push(3)
Push(4)
Push(5)
Push(6)
Pop()
print(stack)