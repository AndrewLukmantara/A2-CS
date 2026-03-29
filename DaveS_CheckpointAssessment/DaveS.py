# #1A
# BeverageQueue = [""for _ in range(10)] # ARRAY OF STRINGS
# BeverageFrontPointer = 0 # INTEGER  
# BeverageRearPointer = 0 # INTEGER

# #1bi
# def DisplayMenu():
#     MyFile = open("c:\\Users\\62818\\OneDrive\\A Level CS\\DaveS_CheckpointAssessment\\BeverageData.txt", "r") # STRING
#     CurrentLine = MyFile.readline().strip() # STRING
#     while CurrentLine != "":
#         print(CurrentLine)
#         CurrentLine = MyFile.readline().strip()
#     MyFile.close()

# #1bii
# def TakeOrder(Orders):
#     Items = Orders.split(",") # ARRAY OF STRINGS
#     BeverageFile = open("c:\\Users\\62818\\OneDrive\\A Level CS\\DaveS_CheckpointAssessment\\BeverageData.txt", "r")
#     OrderFile = open("c:\\Users\\62818\\OneDrive\\A Level CS\\DaveS_CheckpointAssessment\\Order.txt", "w")
#     CurrentLine = BeverageFile.readline().strip()
#     while CurrentLine != "":
#         for i in range(len(Items)): 
#             if CurrentLine == Items[i]:
#                 print(f"{Items[i]} found!")
#                 OrderFile.write(f"{Items[i]}\n")
#         CurrentLine = BeverageFile.readline().strip()
#     BeverageFile.close()
#     OrderFile.close()

# #1biii
# def EnqueueBeverage(DataToEnqueue): #DataToEnqueue : STRING
#     global BeverageFrontPointer, BeverageQueue, BeverageRearPointer
#     if BeverageRearPointer == 10:
#         return False
#     else:
#         BeverageQueue[BeverageRearPointer] = DataToEnqueue
#         BeverageRearPointer = BeverageRearPointer + 1
#         return True

# #1biv
# def ReadOrderData():
#     MyFile = open("c:\\Users\\62818\\OneDrive\\A Level CS\\DaveS_CheckpointAssessment\\Order.txt", "r")
#     CurrentLine = MyFile.readline().strip()
#     while CurrentLine != "":
#         EnqueueBeverage(CurrentLine)
#         CurrentLine = MyFile.readline().strip()
#     MyFile.close()


# #1ci
# def DequeueBeverage():
#     global BeverageFrontPointer, BeverageQueue, BeverageRearPointer
#     if BeverageFrontPointer == BeverageRearPointer:
#         return ""
#     else:
#         ReturnData = BeverageQueue[BeverageFrontPointer] # STRING
#         BeverageFrontPointer = BeverageFrontPointer + 1
#         return ReturnData
    
# #1cii
# def ServeItem():
#     ServedItem = DequeueBeverage() # STRING
#     if ServedItem == "":
#         print("No more orders to serve")
#     else:
#         print(f"You ordered {ServedItem}")


# #1d
# DisplayMenu()
# Order = str(input("Wat di u want")) # STRING
# TakeOrder(Order)
# ReadOrderData()
# ServeItem()


#2a

#2b
def SetUp():
    global Data, Rows
    Rows = int(input("Enter number of rows (1-5): "))
    while Rows < 1 or Rows > 5:
            Rows = int(input("Only can number of rows (1-5): "))
    for i in range(Rows):
        for j in range(4):
            Data[i][j] = int(input(f"Enter data for row {i+1} column {j+1}: "))



def BubbleSort():
    global Data, Rows
    for i in range(Rows):
        Sorted = False
        while Sorted == False:
            Sorted = True
            for j in range(3):
                if Data[i][j] > Data[i][j+1]:
                    Temp = Data[i][j]
                    Data[i][j] = Data[i][j+1]
                    Data[i][j+1] = Temp
                    Sorted = False


def RecursiveBinarySearch(RowNumber, DataToFind, Low, High):
    global Data
    if Low > High:
        return -1
    else:
        Mid = (Low + High) // 2 # INTEGER
        if Data[RowNumber][Mid] == DataToFind:
            return Mid
        elif Data[RowNumber][Mid] < DataToFind:
            return RecursiveBinarySearch(RowNumber, DataToFind, Mid + 1, High)
        elif Data[RowNumber][Mid] > DataToFind:
            return RecursiveBinarySearch(RowNumber, DataToFind, Low, Mid - 1)

Data = [[0 for _ in range(4)] for _ in range(5)] # ARRAY OF INTEGERS
Rows = 5 # INTEGER
SetUp()
print(Data)
BubbleSort()
print(Data)
RowNum = int(input("input row number"))
Data = int(input("input data "))
IndexOfRow = RecursiveBinarySearch(RowNum-1,Data, 0, 3)
if IndexOfRow == -1:
    print("Number not found")
else:
    print(f"Number found at column {IndexOfRow} in row {RowNum}")