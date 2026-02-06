class node(): # RECORD of type node 
    def __init__(self, data : int, nextNode : int):
        self.__data = data
        self.__nextNode = nextNode
    
    def get_data(self):
        return self.__data
    
    def get_nextNode(self):
        return self.__nextNode
    
    def set_nextNode(self, new):
        self.__nextNode = new

    def set_data(self, new):
        self.__data = new


linkedList = [  # ARRAY[0 : 9] OF node
    node(1,1),
    node(5,4),
    node(6,7),
    node(7,-1),
    node(2,2),
    node(0,6),
    node(0,8),
    node(56,3),
    node(0,9),
    node(0,-1)
]
 
startPointer = 0 # int
emptyList = 5 # int

def outputNodes(ll : int, sP : int) -> bool:
    
    i = sP # i : int
    while i != -1:
        print(ll[i].get_data())
        i = ll[i].get_nextNode()

outputNodes(linkedList, startPointer)

def addNode(ll : int, sP : int, hP : int, data : int) -> bool:

    if hP == -1:
        print("List is already full!")
        return False


    # Setting the new Head
    tempPointer = hP
    hP = ll[hP].get_nextNode()
    ll[tempPointer] = node(data, -1)

    i = sP
    while i != -1:
        endPointer = i # endPointer : int
        i = ll[i].get_nextNode()

    ll[endPointer].set_nextNode(tempPointer)

    return hP, sP, True

outputNodes(linkedList, startPointer)
data = int(input("Please enter the data to be added : "))
temp = addNode(linkedList, startPointer, emptyList, data)

emptyList = temp[0]
startPointer = temp[1]
added = temp[2]


if added == True:
    print("added")
else:
    print("not added!")

outputNodes(linkedList, startPointer)
