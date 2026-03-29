Data = [[-1 for _ in range(4)] for _ in range(5)] # 2D ARRAY OF INTEGER
Row = 0 # INTEGER


def SetUp():

    global Data, Row

    Row = int(input("Please enter the number of rows you would like to enter : "))
    if Row >= 1 and Row <= 5:
        print("Valid input!")
        pass
    else:
        print("Invalid input!")
        return

    for row in range(Row):
        for col in range(4):
            number = int(input("Enter the number for the column : "))
            Data[row][col] = number
    
SetUp()
print(Data)


def BubbleSort():

    global Row, Data

    for row in range(Row):
        for col in range(3):
            if Data[row][col] > Data[row][col + 1]:
                temp = Data[row][col + 1]
                Data[row][col + 1] = Data[row][col]
                Data[row][col] = temp
    
BubbleSort()
print(Data)

def RecursiveBinarySearch(RowNum, DataToFind, Low, High):

    global Data

    if Low > High:
        return -1
    else:
        Mid = (Low + High) // 2
        if Data[RowNum][Mid] < DataToFind:
            return RecursiveBinarySearch(RowNum, DataToFind, Mid + 1, High)
        elif Data[RowNum][Mid] > DataToFind:
            return RecursiveBinarySearch(RowNum, DataToFind, Low, Mid - 1)
        else:
            return Mid

RowNum = int(input("Please enter a row number : "))
DataToFind = int(input("Please enter a data to find"))
return_result = RecursiveBinarySearch(RowNum - 1, DataToFind, 0, 3)
if return_result == -1:
    print("Number not found")
else:
    print(f"Number found at column {return_result} in row {RowNum}")

