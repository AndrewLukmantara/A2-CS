TreeArray = [[-1 for _ in range(3)] for _ in range(50)] # ARRAY[0 : 49, 0 : 2] OF INTEGER
RootPointer = -1 # INTEGER
FreeNode = 0 # INTEGER

def AddNode(toStore : int):

    global RootPointer, FreeNode, TreeArray
    
    if FreeNode >= 50:
        print("The tree is full")
        return

    if RootPointer == -1:
        RootPointer = FreeNode
        TreeArray[RootPointer][0] = -1
        TreeArray[RootPointer][1] = toStore 
        TreeArray[RootPointer][2] = -1
        FreeNode += 1

    else:

        tempPointer = RootPointer # INTEGER
        Placed = False # BOOLEAN
        while not Placed:

            if toStore > TreeArray[tempPointer][1]:
                if TreeArray[tempPointer][2] == -1:
                    TreeArray[tempPointer][2] = FreeNode
                    Placed = True
                else:
                    tempPointer = TreeArray[tempPointer][2]
            else:
                if TreeArray[tempPointer][0] == -1:
                    TreeArray[tempPointer][0] = FreeNode
                    Placed = True
                else:
                    tempPointer = TreeArray[tempPointer][0]
        

        TreeArray[FreeNode][1] = toStore
        FreeNode += 1




file = open("C:/Users/AndrewCL JC2Hope/OneDrive/A Level CS/9618_w25/qp_42/TreeData.txt", "r")
line = file.readline().strip()
while line != "":
    AddNode(int(line))
    line = file.readline().strip()
    print(line)
file.close()


def WriteAllToFile():
    try:
        file = open("C:/Users/AndrewCL JC2Hope/OneDrive/A Level CS/9618_w25/qp_42/Tree.txt", "w")
        for i in range(len(TreeArray)):
            line = str(TreeArray[i][0]) + "," + str(TreeArray[i][1]) + "," + str(TreeArray[i][2]) + "\n"
            file.write(line)

        file.close()
    except:
        FileNotFoundError



WriteAllToFile()