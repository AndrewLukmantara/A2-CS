def sumOfArray(arr):
    if arr == []:
        return 0
    else:
        newArr = arr[1:]
        return(arr[0] + sumOfArray(newArr))
    

myArr = [1,2,3,4]
print(sumOfArray(myArr))