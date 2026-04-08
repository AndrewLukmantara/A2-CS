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

def Search(SE):

    global StartPointer

    currentNode = StartPointer

    while currentNode != -1:
        if List[currentNode][0] == SE:
            print(f"Element found at position : {currentNode}")
            break
        else:
            currentNode = List[currentNode][1]

print(List)
Search(1)


def Add(E):

    global HeapPointer, StartPointer

    if HeapPointer == -1:
        print("Full!")
        return -1
    
    # Find the location for the new node to be added
    new_node = HeapPointer

    # Adjust value of heap pointer
    HeapPointer = List[HeapPointer][1]

    # Insert the data, along with the pointer
    List[new_node][0] = E
    List[new_node][1] = StartPointer

    # Adjust value of start pointer
    StartPointer = new_node


Add(10)
print(List)


def Delete(E):

    global HeapPointer, StartPointer

    if StartPointer == -1:
        print("Empty!")
        return -1
    
    previous = -1
    current = StartPointer
    while current != -1:
        if List[current][0] == E:
            break
        else:
            previous = current
            current = List[current][1]

    # Save the node that the node to be deleted is pointing to
    tempPointer = List[current][1]

    # Delete the contents of the node
    List[current][0] = -1

    # Adjust the heap
    List[current][1] = HeapPointer

    HeapPointer = current

    # Set value of the previous pointer, if there is a previous pointer
    if previous != -1:
        List[previous][1] = tempPointer
    else:
        StartPointer = -1


Delete(8)
print(List)

Add(10)
print(List)

Delete(6)
print(List)

Delete(2)
print(List)

Add(100)
print(List)