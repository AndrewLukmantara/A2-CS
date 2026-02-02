# Linked List in Python

List = [[0 for _ in range(2)] for _ in range(10)] # ARRAY[0:9, 0:1] OF STRING
HeapPointer = 0 # INTEGER
StartPointer = -1 # INTEGER

for i in range(10): # i : INTEGER
    List[i][1] = i + 1

List[9][1] = -1

print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")

def addNode_End(data : str) -> bool:

    global StartPointer, HeapPointer, List

    if HeapPointer == -1:
        print("List is full")
        return False

    # creating node

    tempPointer = List[StartPointer][1]
    newNode = HeapPointer # newNode : INTEGER
    StartPointer = HeapPointer
    HeapPointer = List[HeapPointer][1]
    List[newNode][0] = data
    List[newNode][1] = -1 

    # adding node

    while List[tempPointer][1] != -1:
        tempPointer = List[tempPointer][1]
    List[tempPointer][1] = newNode

    return True


def deleteNode(position : int) -> bool:
    
    global StartPointer, HeapPointer, List

    if StartPointer == -1:
        print("List is empty!")
        return False
    
    before = 0
    while List[before][1] != position:
        before = before + 1

    after = List[position][1]
    List[position][1] = 0
    List[position][0] = 0
    List[before][1] = after

    return True
    


addNode_End("Cookie")
addNode_End("Orange")
addNode_End("Muffin")
addNode_End("watermelon")

print(f"\n \nHeap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")
print(List)

deleteNode(2)

print(f"\n \nHeap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")
print(List)