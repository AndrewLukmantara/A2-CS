ArrayNodes = [[-1 for _ in range(3)] for _ in range(20)] # ARRAY[0:19, 0 : 2] OF INTEGER

RootPointer = -1 # INTEGER
FreeNode = 0 # INTEGER

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the data : ")) # INTEGER
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False # BOOLEAN
            CurrentNode = RootPointer # INTEGER
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                         ArrayNodes[CurrentNode][0] = FreeNode
                         Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]


        FreeNode = FreeNode + 1
        return FreeNode, RootPointer # PASSING BYREF

    else:
        print("Tree is full")


def PrintAll():

    i = 0 # INTEGER
    for i in ArrayNodes:
        if i[1] == -1:
            break
        else:
            print(i[0],  i[1],  i[2])
        

for i in range(10):
    FreeNode, RootPointer = AddNode(ArrayNodes, RootPointer, FreeNode)
PrintAll()


def InOrder(currentNode):

    global ArrayNodes

    if ArrayNodes[currentNode][1] != -1:
        InOrder(ArrayNodes[currentNode][0])
        print(ArrayNodes[currentNode][1])
    if ArrayNodes[currentNode][2] != -1:
        InOrder(ArrayNodes[currentNode][2])

InOrder(RootPointer)