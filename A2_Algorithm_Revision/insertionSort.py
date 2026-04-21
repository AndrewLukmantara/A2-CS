from random import randint

arr = [0 for _ in range(10)]
for i in range(10):
    arr[i] = randint(0, 100)

print(arr)

for i in range(1, 10):
<<<<<<< HEAD

    j = i - 1
    Key = arr[i]

    while j >= 0 and arr[j] > Key:
        arr[j + 1] = arr[j]
        j -= 1
        
    arr[j + 1] = Key

print(arr)
=======
    
    j = i - 1 
    Key = arr[i]

    while j >= 0 and Key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = Key


print(arr)
>>>>>>> d0dd6b973d45db410e6d092738970a124533ad03
