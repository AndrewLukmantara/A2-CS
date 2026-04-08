from random import randint

arr = [0 for _ in range(10)]
for i in range(10):
    arr[i] = randint(0, 100)

print(arr)

upper = 9
lower = 0
count = 0
swap = True

while swap:

    swap = False

    for i in range(lower, upper - count):

        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
            swap = True

    count += 1

print(arr)