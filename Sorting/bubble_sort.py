# arr = [6,5,4,3,2,1]
# arr = [4,3,2,1]
# arr = [1,2,3,4]
# arr = [1,2,3,4]
arr = [6,3,9,8,4,6,5,2]
arr = [2, 3, 4, 5, 6, 6, 8, 9]

n = len(arr)
count = 0
sorted = True

for i in range(n-1):
    for j in range(n-1-i):

        # count += 1
        if arr[j] > arr[j+1]:
            # count += 1
            sorted = False
            arr[j], arr[j+1] = arr[j+1], arr[j]
            # print(count)


print(arr, sorted, count)