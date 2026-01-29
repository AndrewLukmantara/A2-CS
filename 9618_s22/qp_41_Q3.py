QueueArray = ["None" for _ in range(10)] # ARRAY[0:9] OF STRING
HeadPointer = 0 # int
TailPointer = 0 # int
NumberItems = 0 # int

def Enqueue(DataToAdd : str) -> bool:
    global QueueArray, HeadPointer, TailPointer, NumberItems
    if NumberItems == 10:
         return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    NumberItems = NumberItems + 1
    return True
    
def Dequeue() -> bool:
    global QueueArray, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return "FALSE"
    QueueArray[HeadPointer] = 0
    if HeadPointer >= 9:
        HeadPointer = 0
    else:
        HeadPointer = HeadPointer + 1
    return QueueArray[HeadPointer]

for i in range(11):
    DataToAdd = str(input("Enter a string : "))
    if Enqueue(DataToAdd) == True:
        print("Success!")
    else:
        print("Queue is full!")


print(f"Next data item : {Dequeue()}")

print(f"Next data item : {Dequeue()}")




