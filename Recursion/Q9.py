def binarySearch(arr, SE, lower, upper):
    mid = (upper + lower) // 2

    if arr[mid] == SE:
        return mid
    elif upper < lower:
        return -1
    else:
        if arr[mid] > SE:
            upper = mid - 1
        elif arr[mid] < SE:
            lower = mid + 1
        return binarySearch(arr, SE, lower, upper)


myArr = [0,1,2,3,4,5,6,7,8,9]
print(binarySearch(myArr, 11, 0, 9))