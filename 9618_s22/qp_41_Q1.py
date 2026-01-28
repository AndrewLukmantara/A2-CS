StackData = [0 for _ in range(10)] # StackData : ARRAY[0:9] OF INTEGER [GLOBAL]
StackPointer = 0 # StackPointer : INTEGER [GLOBAL]

def stack_Output():
    global StackData, StackPointer
    print(f"Stack Pointer : {StackPointer}")

    print("Stack Contents :")
    for i in range(10): # i : INTEGER
        print(StackData[i])



def Push(num : int) -> bool:
    global StackData, StackPointer
    if StackPointer < 10:
        StackData[StackPointer] = num
        StackPointer += 1
        return True
    else:
        return False
    

for i in range(11):
    num = int(input("Please enter a number : "))
    if Push(num) == True:
        print("Added successfully!")
    else:
        print("Stack is full!")

stack_Output()

def Pop() -> int:
    global StackData, StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackData[StackPointer - 1] = 0
        StackPointer -= 1
        return StackData[StackPointer - 1]
    
Pop()
Pop()

stack_Output()