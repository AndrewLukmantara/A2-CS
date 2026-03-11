class Node():
    def __init__(self, Data):
        self.LeftPointer = -1
        self.Data = Data
        self.RightPointer = -1
        
    def GetLeft(self):
        return self.LeftPointer
    
    def GetRight(self):
        return self.RightPointer

    def GetData(self):
        return self.Data    

    def SetLeft(self, Left):
        self.LeftPointer = Left

    def SetRight(self, Right):
        self.RightPointer = Right

    def SetData(self, Data):
        self.Data = Data
    

class TreeClass():
    
    def __init__(self):
        self.Tree = [Node(-1) for _ in range(20)]
        self.FirstNode = -1
        self.NumberNodes = 0

    def InsertNode(self, NewNode):

        if self.FirstNode == -1:
            self.Tree[0] = NewNode
            self.FirstNode = 0
            self.NumberNodes += 1
            return

        i = self.FirstNode
        while True:

            if NewNode.GetData() < self.Tree[i].GetData():

                if self.Tree[i].GetLeft() == -1:
                    self.Tree[i].SetLeft(self.NumberNodes)
                    self.Tree[self.NumberNodes] = NewNode
                    self.NumberNodes += 1
                    return
                else:
                    i = self.Tree[i].GetLeft()

            else:

                if self.Tree[i].GetRight() == -1:
                    self.Tree[i].SetRight(self.NumberNodes)
                    self.Tree[self.NumberNodes] = NewNode
                    self.NumberNodes += 1
                    return
                else:
                    i = self.Tree[i].GetRight()
        

    def OutputTree(self):

        if self.FirstNode != -1:
            i = 0
            for i in range(len(self.Tree)):
                if self.Tree[i].GetData() != -1:
                    print(f"Left : {self.Tree[i].GetLeft()}, Data : {self.Tree[i].GetData()}, Right : {self.Tree[i].GetRight()}")
                else:
                    break
            
        else:
            print("No nodes")


TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()
