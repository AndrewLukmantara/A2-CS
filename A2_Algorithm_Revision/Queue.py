frontPointer = 0
rearPointer = -1
queueLen = 0

queue = [0 for _ in range(10)]

def Enqueue(data : int) -> int:

    global rearPointer, queueLen
    
    if queueLen == 10:
        return -1
    
    if rearPointer == 9: 
        rearPointer = 0
        queue[rearPointer] = data
    
    else:
        rearPointer += 1
        queue[rearPointer] = data
    
    queueLen += 1

    return 0


def Dequeue() -> int:

    global frontPointer, queueLen
    
    if queueLen == 0: 
        return -1

    queue[frontPointer] = 0

    if frontPointer == 9:
        frontPointer = 0
    else:
        frontPointer += 1
    
    queueLen -= 1
    return 0

Enqueue(1) 
Enqueue(2)
Enqueue(3)
Enqueue(4)
Enqueue(5)
Enqueue(6)
Enqueue(7)
print(queue)
Dequeue()
print(queue)
Enqueue(8)
Enqueue(9)
Enqueue(10)
Enqueue(11)
print(queue)
Enqueue(12)
print(queue)
Dequeue()
print(queue)
Dequeue()
print(queue)





