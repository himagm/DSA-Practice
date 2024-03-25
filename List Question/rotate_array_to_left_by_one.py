
def rotateArray(arr, n):
    arr[:] = arr[1:] + [arr[0]]
    return arr


print(rotateArray([1, 2, 3, 4, 5], 5))