# Linked List in Python

List = [[0 for _ in range(2)] for _ in range(7)] # ARRAY[0:9, 0:1] OF INTEGER
HeapPointer = -1 # INTEGER
StartPointer = 3 # INTEGER

# for i in range(10): # i : INTEGER
#     List[i][1] = i + 1

List[0][0] = 3
List[0][1] = -1
List[1][0] = 6
List[1][1] = 0
List[2][0] = 4
List[2][1] = 6
List[3][0] = 9
List[3][1] = 4
List[4][0] = 2
List[4][1] = 2
List[5][0] = 1
List[5][1] = 1
List[6][0] = 8
List[6][1] = 5



print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")

def addNode_End(data):

    global StartPointer, HeapPointer, List

    if HeapPointer == -1:
        print("List is full")
        return -1

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

    return 0


# def deleteNode(position : int) -> bool:
    
#     global StartPointer, HeapPointer, List

#     if StartPointer == -1:
#         print("List is empty!")
#         return False
    
#     before = 0
#     while List[before][1] != position:
#         before = before + 1

#     after = List[position][1]
#     List[position][1] = 0
#     List[position][0] = 0
#     List[before][1] = after

#     return True
    

def Search(data):

    global StartPointer, HeapPointer, List

    Found = False
    ItemPointer = StartPointer
    while not Found and List[ItemPointer][0] != 0:
        if List[ItemPointer][0] == data:
            Found = True
        else:
            TempPointer = ItemPointer
            ItemPointer = List[ItemPointer][1]
            Position = ItemPointer

    if Found:
        print("Found!")
        print(f"Position : {Position}")
        print(f"Previous : {TempPointer}")
        return Position, TempPointer
    else:
        print("Not Found!")
        return -1

def Delete(data):
    
    global StartPointer, HeapPointer, List

    if StartPointer == -1:
        print("Can't delete from an empty list!")
    else:
        if Search(data) == -1:
            print("Not found!")
        else:
            temp = Search(data)
            Position = temp[0]
            Previous = temp[1]
            if List[Position][1] == -1:
                List[Position][1] = 0
                List[Position][0] = 0
                StartPointer = -1
                HeapPointer = Position
            else:
                List[Previous][1] = List[Position][1]
                List[Position][0] = 0 
                List[Position][1] = 0
                HeapPointer = Position


print(f"\nHeap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")
print(f"{List}\n")
Delete(4)
print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")