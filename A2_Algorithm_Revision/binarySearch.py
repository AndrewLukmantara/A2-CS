from random import randint

myArr = [0 for _ in range(10)]
for i in range(len(myArr)):
    myArr[i] = randint(0, 100)


# def BinarySearch(SE):
    
#     upper = 9
#     lower = 0
    
#     Mid = (upper + lower) // 2
    
#     while lower <= upper:

#         Mid = (upper + lower) // 2
#         if myArr[Mid] == SE:
#             print(F"Found at {Mid}")
#             return
#         elif myArr[Mid] > SE:
#             upper = Mid - 1
#         elif myArr[Mid] < SE:
#             lower = Mid + 1
    

#     print("Not Found!")


def BinarySearch(SE, Lower, Upper):

    if Lower > Upper:
        return -1
    else:
        Mid = (Upper + Lower) // 2
        if myArr[Mid] == SE:
            return Mid
        elif myArr[Mid] > SE:
            return BinarySearch(SE, Lower, Mid - 1)
        elif myArr[Mid] < SE:
            return BinarySearch(SE, Mid + 1, Upper)
        

myArr.sort()
print(myArr)
SE = int(input("Please enter the search element : "))
print(f"Element found : {BinarySearch(SE, 0, 9)}")

