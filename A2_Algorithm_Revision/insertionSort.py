from random import randint

arr = [0 for _ in range(10)]
for i in range(10):
    arr[i] = randint(0, 100)

print(arr)

for i in range(1, 10):

    j = i - 1
    Key = arr[i]

    while j >= 0 and arr[j] > Key:
        arr[j + 1] = arr[j]
        j -= 1
        
    arr[j + 1] = Key

print(arr)
