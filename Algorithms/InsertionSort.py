myArr = [10, 8, 5, 1, 2, 6, 9, 3, 4, 7]

for i in range(len(myArr)):
    j = i - 1
    key = myArr[i]
    while j >= 0 and myArr[j] > key:
        myArr[j + 1] = myArr[j]
        j -= 1
    myArr[j + 1] = key

for i in range(len(myArr)):
    print(myArr[i])
