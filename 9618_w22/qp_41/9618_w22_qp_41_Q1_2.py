global DataArray
DataArray = [0 for _ in range(100)] # ARRAY[0 : 99] OF INTEGER


def ReadFile():
    try:
        file = open("9618_w22_qp_41 Q1 Only\\9618_w22_qp_41 Question Number-1\\IntegerData.txt","r")
        for i in range(100): # i : INTEGER
            line = file.readline().strip() # i : STRING
            DataArray[i] = int(line)

    except FileNotFoundError:
        print("File not found!")


def FindUpper(num):
    
    High = len(DataArray) - 1
    Low = 0
    Upper = -1
    while Low <= High:
        Mid = (Low + High) // 2
        if DataArray[Mid] > num:
            High = Mid - 1
        elif DataArray[Mid] < num:
            Low = Mid + 1
        else:
            Low = Mid + 1
            Upper = Mid

    return Upper
            


def FindLower(num):
    
    High = len(DataArray) - 1
    Low = 0
    Lower = -1
    while Low <= High:
        Mid = (Low + High) // 2
        if DataArray[Mid] > num:
            High = Mid - 1
        elif DataArray[Mid] < num:
            Low = Mid + 1
        else:
            High = Mid - 1
            Lower = Mid

    return Lower



def FindValues():
    Valid = False
    while not Valid:
        num = int(input("Please enter a number between 1 and 100 inclusive :"))
        if num >= 0 and num <= 100:
            Valid = True
    
    ans = FindUpper(num) - FindLower(num) + 1
    return ans
        
def InsertionSort():
    for i in range(len(DataArray)):
        j = i - 1
        key = DataArray[i]
        while j >= 0 and DataArray[j] > key:
            DataArray[j + 1] = DataArray[j]
            j -= 1
        DataArray[j + 1] = key
            

ReadFile()
InsertionSort()
print(f"The number you entered appears {FindValues()} times in the array")



for i in range(len(DataArray)):
    print(DataArray[i])

print(DataArray)