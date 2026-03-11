from random import randint

myArr = [-1 for _ in range(20)] # ARRAY[0:19] OF INTEGER
for i in range(20): # i : INTEGER
    myArr[i] = randint(0, 100)

def PrintArray(arr): # arr : ARRAY OF INTEGER

    line = "" # line : STRING

    for i in range(20):
        line = line + " " + str(arr[i])

    print(line)


def BubbleSort(arr): # arr : ARRAY OF INTEGER
    
    Swap = True
    Upper = len(arr) - 1
    Pass = 0
    Lower = 0
    Temp = 0

    while Swap:
        Swap = False
        for i in range(Lower, Upper - Pass):
            if arr[i] > arr[i + 1]:
                Temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = Temp
                Swap = True

        Pass = Pass + 1

    return arr


PrintArray(myArr)
BubbleSort(myArr)
print("Sorted")
PrintArray(myArr)


def RecursiveBinarySearch(arr, lower : int, upper : int, value : int) -> int:
    
    if lower > upper:
        return -1

    mid = (lower + upper) // 2

    if arr[mid] < value:
        return RecursiveBinarySearch(arr, mid + 1, upper, value)
    elif arr[mid] > value:
        return RecursiveBinarySearch(arr, lower, mid - 1, value)
    else:
        return mid


searchNum = int(input("Please enter an integer number : "))

if RecursiveBinarySearch(myArr, 0, 19, searchNum) == -1:
    print("Not found")
else:
    print(f"Found at position {RecursiveBinarySearch(myArr, 0, 19, searchNum)}")

