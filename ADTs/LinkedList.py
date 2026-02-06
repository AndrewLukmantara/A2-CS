# Linked List in Python

List = [[0 for _ in range(2)] for _ in range(7)] # ARRAY[0:9, 0:1] OF INTEGER
HeapPointer = -1 # INTEGER
StartPointer = 3 # INTEGER

# Initializing a list

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


def addNode_End(data):

    global StartPointer, HeapPointer, List

    if HeapPointer == -1:
        print("List is full")

    # creating node

    tempPointer = StartPointer
    StartPointer = HeapPointer
    HeapPointer = List[HeapPointer][1]
    List[StartPointer][0] = data
    List[StartPointer][1] = tempPointer


    
def Search(SE):

    global StartPointer, HeapPointer, List, previous

    i = StartPointer
    while i != -1:
        if List[i][0] == SE:
            return i, previous
        else:
            previous = i
            i = List[i][1]
    
    return -1
        


def Delete(data):
    
    global StartPointer, HeapPointer

    if StartPointer == -1: # Check for empty list
        print("Can't delete from an empty list!")
        return

    store = Search(data)

    if store == -1:
        return
    
    else:
        current = store[0]
        previous = store[1]

        if previous == StartPointer:
            previous = -1        

        tempPointer = List[current][1]

        List[current][0] = 0
        List[current][1] = HeapPointer
        HeapPointer = current

        if previous == -1:
            StartPointer = current
        else:
            List[previous][1] = tempPointer

            
    
Delete(3)
print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")
Delete(8)
print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")
Delete(9)
print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")