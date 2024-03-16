arr = [64,11,6,20,34]

min = arr[0]
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]

print(min)
