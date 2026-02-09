FirstNode = -1 # INTEGER
FirstEmpty = 0 # INTEGER
LinkedList = [[-1 for _ in range(2)] for _ in range(20)] # ARRAY[0 : 19, 0 : 1] OF INTEGER
for i in range(19):
    LinkedList[i][1] = i + 1
LinkedList[19][1] = -1


def InsertData(n1, n2, n3, n4, n5 : int):

    global FirstNode, FirstEmpty
    if FirstEmpty == -1:
        print("False!")
        pass
    
    temp = FirstNode # temp : INTEGER
    FirstNode = FirstEmpty
    FirstEmpty = LinkedList[FirstNode][1]
    LinkedList[FirstNode][0] = n1
    LinkedList[FirstNode][1] = temp

        
    temp = FirstNode
    FirstNode = FirstEmpty
    FirstEmpty = LinkedList[FirstNode][1]
    LinkedList[FirstNode][0] = n2
    LinkedList[FirstNode][1] = temp

    temp = FirstNode
    FirstNode = FirstEmpty
    FirstEmpty = LinkedList[FirstNode][1]
    LinkedList[FirstNode][0] = n3
    LinkedList[FirstNode][1] = temp

    temp = FirstNode
    FirstNode = FirstEmpty
    FirstEmpty = LinkedList[FirstNode][1]
    LinkedList[FirstNode][0] = n4
    LinkedList[FirstNode][1] = temp


    temp = FirstNode
    FirstNode = FirstEmpty
    FirstEmpty = LinkedList[FirstNode][1]
    LinkedList[FirstNode][0] = n5
    LinkedList[FirstNode][1] = temp


def OutputLinkedList():
    i = FirstNode # i : INTEGER
    while i != -1:
        print(LinkedList[i][0])
        i = LinkedList[i][1]



InsertData(10, 7, 8, 5, 6)
OutputLinkedList()

def RemoveData(data : int):

    global FirstNode, FirstEmpty

    current = FirstNode # current : INTEGER
    Found = False
    previous = -1

    while current != -1 :

        if LinkedList[current][0] == data:
            Found = True
            break
        else:
            previous = current
            current = LinkedList[current][1]
    
    if FirstNode == -1:
        print("Empty list!")

    if Found:

        temp = LinkedList[current][1]
        LinkedList[current][0] = -1
        LinkedList[current][1] = FirstEmpty
        FirstEmpty = current

        if previous == -1:
            FirstNode = temp
        else:
            LinkedList[previous][1] = temp
            

RemoveData(5)
print("After")
OutputLinkedList()