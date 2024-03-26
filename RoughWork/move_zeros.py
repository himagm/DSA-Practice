# arr = [0,1,0,3,12]
arr = [7,8,0,3,2,0,0,1,0,7,6,2]
def moveZeros(arr):
    n = len(arr)
    i = 0
    if n <= 1:
        return
    while True:
        if arr[i] == 0:        
            break
        i += 1
    else:
        return


    for x in range(n):
        if arr[i] == 0 and arr[x] !=0 and x > i:
            arr[i], arr[x] = arr[x], arr[i]
            i += 1
    
    return arr

print(moveZeros(arr))
