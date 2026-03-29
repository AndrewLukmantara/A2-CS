
# SOME ERRORS HERE (DO NOT USE FOR REFERENCE YET)

BeverageQueue = ["None" for _ in range(10)] # array[0 : 9] of string
BeverageFrontPointer = 0 # integer
BeverageRearPointer = 0 # integer

def DisplayMenu():
    file = open("C:/Users/62818/OneDrive/A Level CS/AndrewCL_CheckpointAssessment/BeverageData.txt", "r") # STRING
    line = file.readline().strip() # STRING
    while line != "":
        print(line)
        line = file.readline().strip()

    file.close()

def TakeOrder(selection):

    Items = selection.split(",") # ARRAY OF STRING

    Beveragefile = open("C:/Users/62818/OneDrive/A Level CS/AndrewCL_CheckpointAssessment/BeverageData.txt", "r")
    OrderFile = open("C:/Users/62818/OneDrive/A Level CS/AndrewCL_CheckpointAssessment/Order.txt", "w")

    line = Beveragefile.readline().strip()

    while line != "":

        for i in range(len(Items)): # i : INTEGER

            if line == Items[i]:
                print(f"{Items[i]} found!")
                OrderFile.write(f"{Items[i]}")

        line = Beveragefile.readline().strip()

    Beveragefile.close()
    OrderFile.close()



    

def EnqueueBeverage(DataToEnqueue):

    global BeverageFrontPointer, BeverageQueue, BeverageRearPointer
    
    if BeverageRearPointer == 10:
        return False
    else:
        BeverageQueue[BeverageRearPointer] = DataToEnqueue
        BeverageRearPointer = BeverageRearPointer + 1
        return True

def ReadOrderData():
    
    file = open("C:/Users/62818/OneDrive/A Level CS/AndrewCL_CheckpointAssessment/Order.txt", "r")
    line = file.readline().strip()
    while line != "":
        EnqueueBeverage(line)
        line = file.readline().strip()
        
def DequeueBeverage():

    global BeverageFrontPointer, BeverageQueue, BeverageRearPointer

    if BeverageFrontPointer == BeverageRearPointer:
        return ""
    else:
        ReturnData = BeverageQueue[BeverageFrontPointer]
        BeverageFrontPointer = BeverageFrontPointer + 1
        return ReturnData

def ServeItem():

    return_result = DequeueBeverage()
    if return_result == "":
        print("No more orders to serve")
    else:
        print(f"You ordered {return_result}.")


DisplayMenu()
TakeOrder("Tea,Coffee,Apple Juice,Cold Tea,Smoothie")
ReadOrderData()
ServeItem()