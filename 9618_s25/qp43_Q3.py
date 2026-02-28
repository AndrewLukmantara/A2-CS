class Node():
    def __init__(self, TheData, NextNode):
        self._TheData = TheData
        self._NextNode = NextNode
    
    def GetData(self):
        return self._TheData
    
    def GetNextNode(self):
        return self._NextNode
    
    def SetNextNode(self, next):
        self._NextNode = next
    
class LinkedList():
    def __init__(self):
        self._HeadNode = None
        
    
    def InsertNode(self, data : int):
        newNode = Node(data, self._HeadNode)
        self._HeadNode = newNode

    def Traverse(self):
        i = self._HeadNode
        concstr = ""
        while i != None:
            concstr = concstr + " " + str(i.GetData())
            i = i.GetNextNode()

        return concstr

    def RemoveNode(self, data):
        
        if self._HeadNode == None:
            print("List is empty!")
            return False
    
        previous = None
        Found = False
        current = self._HeadNode
        while current.GetNextNode() != None:
            if current.GetData() == data:
                Found = True
                break
            else:
                previous = current
                current = current.GetNextNode()
        
        if Found == False:
            print("Data is not found!")
            return False
    
        temp = current.GetNextNode()
        current.TheData = -1
        
        if previous == None:
            self._HeadNode = temp
        else:
            previous.SetNextNode(temp)

        return True
    

myList = LinkedList()

myList.InsertNode(10)
myList.InsertNode(20)
myList.InsertNode(30)
myList.InsertNode(40)
myList.InsertNode(50)


print(myList.Traverse())
myList.RemoveNode(30)
print(myList.Traverse())