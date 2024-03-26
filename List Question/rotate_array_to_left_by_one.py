
def rotateArray(arr, n):
    #got better than 100% for this
    # arr[:] = arr[1:] + [arr[0]]
    # return arr

    #anirudh's method
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    
    arr[-1] = temp
    return arr


print(rotateArray([1, 2, 3, 4, 5], 5))