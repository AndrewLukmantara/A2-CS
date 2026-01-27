# Linked List in Python

List = [[0 for _ in range(2)] for _ in range(10)] # ARRAY[0:9, 0:1] OF INTEGER
HeapPointer = 0 # INTEGER
StartPointer = -1 # INTEGER

for i in range(10): # i : INTEGER
    List[i][1] = i + 1

List[9][1] = -1

print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")

def addNode_End(data):

    global StartPointer, HeapPointer, List

    if HeapPointer == -1:
        print("List is full")
        return False

    # creating node

    newNode = HeapPointer # newNode : INTEGER
    HeapPointer = List[HeapPointer][1]
    List[newNode][0] = data
    List[newNode][1] = -1 

    # adding node

    if StartPointer == -1:  # list is empty
        StartPointer = newNode
    else:  # list is not empty
        current = StartPointer # current : INTEGER
        while List[current][1] != -1:
            current = List[current][1]
        List[current][1] = newNode


addNode_End("Cookie")
addNode_End("Orange")
addNode_End("Muffin")

print(f"\n \nHeap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")
print(List)