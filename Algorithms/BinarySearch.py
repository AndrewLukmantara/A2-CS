# In a function

SearchElement = int(input("Please enter a search element : "))
myArr = [10, 8, 5, 1, 2, 6, 9, 3, 4, 7]
myArr.sort()
def BinarySearch(SearchElement):
    global myArr
    High = len(myArr) - 1
    Low = 0
    while Low >= High:
        Mid = int((Low + High) / 2)
        if myArr[Mid] == SearchElement:
            print(f"Search element {SearchElement} has been found!")
            return True
        elif myArr[Mid] < SearchElement:
            Low = Mid + 1
        elif myArr[Mid] > SearchElement:
            High = Mid - 1
    print(f"Search element {SearchElement} is not found!")


# Not in a function

SearchElement = int(input("Please enter a search element : "))
myArr = [10, 8, 5, 1, 2, 6, 9, 3, 4, 7]
myArr.sort()
Found = False
High = len(myArr) - 1
Low = 0
while Low >= High:
    Mid = int((Low + High) / 2)
    if myArr[Mid] == SearchElement:
        print(f"Search element {SearchElement} has been found!")
        Found = True
    elif myArr[Mid] < SearchElement:
        Low = Mid + 1
    elif myArr[Mid] > SearchElement:
        High = Mid - 1

if Found == False:  
    print(f"Search element {SearchElement} is not found!")