class node():
    def __init__(self, left, data, right):
        self.data = data
        self.left = left
        self.right = right

RootNode = 0
Heap = 8

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


def Search(SE):
    current = RootNode
    while current != -1:
        
        if BinaryTree[current].data == SE:
            print(f"Found at node : {current}")
            break

        if SE > BinaryTree[current].data:
            current = BinaryTree[current].right

        elif SE < BinaryTree[current].data:
            current = BinaryTree[current].left


Search(14)


def Add(E):

    global RootNode, Heap

    if Heap == -1:
        print("Full!")
        return

    node_position = Heap
    Heap = BinaryTree[Heap].left
    Right = False
    current = RootNode

    while current != -1:
        
        previous = current

        if E > BinaryTree[current].data:
            current = BinaryTree[current].right
            Right = True
        elif E < BinaryTree[current].data:
            current = BinaryTree[current].left
            Right = False


    if previous == -1:
        RootNode = node_position
    elif Right:
        BinaryTree[previous].right = node_position
    else:
        BinaryTree[previous].left = node_position

    BinaryTree[node_position].data = E
    

for i in range(len(BinaryTree)):
    print(BinaryTree[i].data)

Add(100)

print("Add result")
for i in range(len(BinaryTree)):
    print(BinaryTree[i].data)


def inOrder(current): # left -> root -> right
    
    if BinaryTree[current].left != -1:
        inOrder(BinaryTree[current].left)

    print(BinaryTree[current].data)

    if BinaryTree[current].right != -1:
        inOrder(BinaryTree[current].right)


inOrder(RootNode)


def postOrder(current): # right -> root-> left
    
    if BinaryTree[current].right != -1:
        inOrder(BinaryTree[current].right)

    print(BinaryTree[current].data)

    if BinaryTree[current].left != -1:
        inOrder(BinaryTree[current].left)


print("\n")
postOrder(RootNode)


def postOrder(current): # root -> left -> right

    print(BinaryTree[current].data)
    
    if BinaryTree[current].left != -1:
        inOrder(BinaryTree[current].left)

    if BinaryTree[current].right != -1:
        inOrder(BinaryTree[current].right)


print("\n")
postOrder(RootNode)