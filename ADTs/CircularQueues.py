myQueue = [0 for _ in range(10)] # ARRAY [0 : 9] OF INTEGER
front = 0 # INTEGER
rear = -1 # INTEGER
queueFull = len(myQueue) # INTEGER
queueLen = 0 # INTEGER

def enqueue(num): # num : INTEGER
    global front, rear, myQueue, queueLen, queueFull
    if queueLen != queueFull:  
        if rear != 9:
            rear = rear + 1
            myQueue[rear] = num
            queueLen = queueLen + 1
        else:
            rear = 0
            myQueue[rear] = num
            queueLen = queueLen + 1
        print("Success")
    else:
        print("Unsuccessful")

def dequeue():
    global front, rear, myQueue, queueLen, queueFull
    if queueLen != 0:
        if front != 9:
            myQueue[front] = 0
            front = front + 1
            queueLen = queueLen - 1

        else:
            myQueue[front] = 0
            front = 0
            queueLen = queueLen - 1
        print("Success")
    
    else:
        print("Unsuccessful")

    

enqueue(9)
enqueue(10)
enqueue(11)

print(myQueue)
dequeue()
print(myQueue)

enqueue(77)
enqueue(88)
enqueue(67)

print(myQueue)
dequeue()
print(myQueue)

enqueue(99)
enqueue(54)
enqueue(17)
enqueue(12)
enqueue(33)

print(myQueue)

enqueue(12)
enqueue(67)
