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


def FindValues():

    count = 0 # count : INTEGER
    num = 0 # num : INTEGER
    Valid = False # Valid : BOOLEAN
    while Valid == False:
        num = int(input("Please enter a number between 1 and 100 inclusive :"))
        if num >= 0 and num <= 100:
            Valid = True
    
    for i in range(100):
        if DataArray[i] == num:
            count = count + 1
    return count


ReadFile()
print(f"The number you entered appears {FindValues()} times in the array")

def BubbleSort():
    lower = 0 # lower : INTEGER
    upper = 99 # upper : INTEGER
    Swap = True # Swap : BOOLEAN

    while Swap == True and upper != 0:
        Swap = False
        for i in range(lower, upper):
            if DataArray[i] > DataArray[i + 1]:
                Temp = DataArray[i]
                DataArray[i] = DataArray[i + 1]
                DataArray[i + 1] = Temp
                Swap = True
        upper -= 1

BubbleSort()
print(DataArray)