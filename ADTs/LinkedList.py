List = [[0 for _ in range(2)] for _ in range(10)]
HeapPointer = 0
StartPointer = -1

for i in range(10):
    List[i][1] = i + 1

List[9][1] = StartPointer

print(List)

def addNode_End(data):

    global StartPointer, HeapPointer, List

    if StartPointer == -1:
        List[HeapPointer][0] = data
        StartPointer = HeapPointer
        HeapPointer += 1
        print("Success")

    elif HeapPointer == 9:
        print("Unsuccessful")

    else:
        List[HeapPointer][0] = data
        HeapPointer += 1
        print("Success")

def addNode_Middle(data, position):

    global StartPointer, HeapPointer, List

    if position > 0 and position < HeapPointer - 1:
        List[HeapPointer][0] = data
        List[position][1] = HeapPointer
        List[HeapPointer][1] = position + 1
        HeapPointer += 1
        print("Success")
    else:
        print("Unsuccessful")


addNode_End("Cookie")
addNode_End("Orange")
addNode_End("Muffin")
addNode_End("Tick")
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")
print(List)
addNode_Middle("Goggles", 2)
print(List)
print(f"Heap Pointer Value : {HeapPointer}\nStart Pointer Value : {StartPointer}")