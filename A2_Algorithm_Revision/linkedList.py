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


def Add(data : int) -> int:

    global StartPointer, HeapPointer
    
    if HeapPointer == -1:
        return -1
    
    currentPointer = StartPointer
    StartPointer = HeapPointer

    List[StartPointer][0] = data

    HeapPointer = List[StartPointer][1]

    List[StartPointer][1] = currentPointer

    return 0
    

def Delete(data : int) -> int:
    
    global StartPointer, HeapPointer

    if StartPointer == -1:
        return -1

    current = StartPointer
    previous = -1
    while current != -1:
        if List[current][0] == data:
            break
        else:
            previous = current
            current = List[current][1]
        
    tempPointer = List[current][1]
    List[current][0] = 0
    List[current][1] = HeapPointer
    HeapPointer = current
    
    if previous == -1:
        StartPointer == current
    else:
        List[previous][1] = tempPointer

    return 0


def Search(data : int) -> int:
    
    global StartPointer, HeapPointer


    if StartPointer == -1:
        return -1
    
    current = StartPointer
    while current != -1:
        if List[current][0] == data:
            print("found!")
            break
        else:
            current = List[current][1]

print(List)
Delete(2)
print(List)
Delete(3)
print(List)
Delete(6)
print(List)

Search(4)