arr = [10,64,25,12,22,11]

# Using min

# for i in range(len(arr)):
#     small = min(arr[i:])
#     ind = arr.index(small)
#     arr[i], arr[ind] = arr[ind], arr[i]

# without min
n = len(arr)

for i in range(n):
    min_ind = i
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            min_ind = j
    
    arr[i], arr[min_ind] = arr[min_ind], arr[i]


print(arr)

