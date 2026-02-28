class node():
    def __init__(self, left, data, right):
        self.data = data
        self.left = left
        self.right = right


BinaryTree = [
    node(1, 9, 2),
    node(3, 5, 4),
    node(5, 12, 6),
    node(7, 3, -1),
    node(-1, 6, -1),
    node(-1, 11, -1),
    node(-1, 14, -1),
    node(-1, 2, -1),
    node(-1, -1, -1)
    ]

RootNode = 0
Heap = 8

def Search(data):
    i = RootNode
    Found = False
    End = False
    while not Found and not End:
        
        if BinaryTree[i].left == -1 and BinaryTree[i].right == -1:
            End = True

        if BinaryTree[i].data == data:
            Found = True
        elif data < BinaryTree[i].data:
            i = BinaryTree[i].left
        elif data > BinaryTree[i].data:
            i = BinaryTree[i].right
            

    if Found == True:
        print("Found")
    elif Found == False:
        print("False")


Search(12)


def Add(data):

    global Heap, RootNode

    if Heap == -1:
        print("Full already")
        return

    if RootNode == -1:
        RootNode = 0

    i = RootNode
    End = False
    while not End:
        
        if BinaryTree[i].left == -1 and BinaryTree[i].right == -1:
            End = True

        if data < BinaryTree[i].data:
            i = BinaryTree[i].left
        elif data > BinaryTree[i].data:
            i = BinaryTree[i].right

    if data > BinaryTree[i].data:
        BinaryTree[i].right = Heap
        BinaryTree[Heap] = node(-1, data, -1)
    elif data > BinaryTree[i].data:
        BinaryTree[i].left = Heap
        BinaryTree[Heap] = node(-1, data, -1)
        Heap = BinaryTree[Heap].left

Add(1)

for i in BinaryTree:
    print(i.left, i.data, i.right)
