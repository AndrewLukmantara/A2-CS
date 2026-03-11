# DECLARE NumberArray : ARRAY[0 : 6] OF INTEGER

NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray, NumberElements): #IntegerArray : ARRAY OF INTEGER, NumberElements : INTEGER

    # DECLARE LastItem : INTEGER
    # DECLARE CheckItem : INTEGER
    # DECLARE LoopAgain : BOOLEAN

    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements -1)
        LastItem = IntegerArray[NumberElements -1]
        CheckItem = NumberElements -2
    
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem -1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray


RecursiveInsertion(NumberArray, 7)
print("Recursive")
print(NumberArray)


def IterativeInsertion(IntegerArray):

    # DECLARE i, j, key : INTEGER

    for i in range(len(IntegerArray)):
        j = i -1
        key = IntegerArray[i]
        while j >= 0 and IntegerArray[j] > key:
            IntegerArray[j + 1] = IntegerArray[j]
            j -= 1
        IntegerArray[j + 1] = key


IterativeInsertion(NumberArray)
print("iterative")
print(NumberArray)

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    Mid = (First + Last) // 2
    if ToFind > IntegerArray[Mid]:
        First = Mid + 1
        return BinarySearch(IntegerArray, First, Last, ToFind)
    elif ToFind < IntegerArray[Mid]:
        Last = Mid - 1
        return BinarySearch(IntegerArray, First, Last, ToFind)
    elif ToFind == IntegerArray[Mid]:
        return Mid

retval = BinarySearch(NumberArray, 0, 6, 644)
if retval == -1:
    print("Not found")
else:
    print(f"Index : {retval}")