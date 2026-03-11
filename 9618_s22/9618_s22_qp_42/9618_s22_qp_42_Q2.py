from random import randint

ArrayData = [[-1 for _ in range(10)] for _ in range (10)] # ARRAY[0 : 9, 0 : 9] OF INTEGER
for i in range(10): # i : INTEGER
    for j in range(10): # i : INTEGER
        ArrayData[i][j] = randint(2, 99)

def OutputValue():
    for i in range(10):
        tempStr = "" # tempStr : STRING
        for j in range(10):
            tempStr = tempStr + " " + str(ArrayData[i][j])
        print(tempStr)

print("Before")
OutputValue()
print("\n")

ArrayLength = 10 # ArrayLength : STRING
for X in range(0, ArrayLength): # X : INTEGER
    for Y in range(0, ArrayLength - 1): # Y : INTEGER
        for Z in range(0, ArrayLength - Y - 1): # Z : INTEGER
            if ArrayData[X][Z] > ArrayData[X][Z + 1]: 
                TempValue = ArrayData[X][Z]  # TempValue : INTEGER
                ArrayData[X][Z] = ArrayData[X][Z + 1] 
                ArrayData[X][Z + 1] = TempValue


print("After")
OutputValue()


def BinarySearch(SearchArray, Lower : int, Upper : int, SearchValue : int) -> int: # SearchArray : ARRAY OF INT

    if Upper >= Lower:
        Mid = (Lower + Upper - 1) // 2 # MID : INTEGER
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        elif SearchArray[0][Mid] < SearchValue:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
        
    return -1


print(f"Test 1 : {BinarySearch(ArrayData, 0, 10, 68)}")
print(f"Test 2 : {BinarySearch(ArrayData, 0, 10, 93)}")