# WHILE Loop

i = 0
SearchElement = int(input("Please enter a search element : "))
Found = False
myArr = [10, 8, 5, 1, 2, 6, 9, 3, 4, 7]

while not Found:
    if myArr[i] == SearchElement:
        Found = True
        print(f"Search element {SearchElement} is found at index {i}!")
    i =+ 1

if not Found:
    print(f"Search element {SearchElement} is not found!")


# FOR Loop

for i in range(len(myArr)):
    Found = True
    print(f"Search element {SearchElement} is found at index {i}!")


if not Found:
    print(f"Search element {SearchElement} is not found!")