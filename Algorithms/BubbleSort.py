myArr = [10, 8, 5, 1, 2, 6, 9, 3, 4, 7]
lower = 0
upper = 9
Swap = True

while Swap == True and upper != 0:
    Swap = False
    for i in range(lower, upper):
        if myArr[i] < myArr[i + 1]:
            Temp = myArr[i]
            myArr[i] = myArr[i + 1]
            myArr[i + 1] = Temp
            Swap = True
    upper -= 1

for i in range(len(myArr)):
    print(myArr[i])
