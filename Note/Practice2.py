arr = [8 , 9 , 10, 5 , 4 , 2 , 1, 3]
# swap = True
# Pass = 0
# while swap == True and Pass < len(arr) - 1: 
#     swap = False
#     for i in range(len(arr) - 1 - Pass):
#         if arr[i] > arr[i+1]:
#             tempObj = arr[i + 1]
#             arr[i + 1] = arr[i]
#             arr[i] = tempObj
#             swap = True
#     Pass = Pass + 1

# print(arr)

arr.sort(reverse=True)
print(arr)

            

if 1 in arr:
    print("true")