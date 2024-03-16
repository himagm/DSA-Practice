def revAr(arr, ind):
    n = len(arr)
    if ind == n //2:
        print(arr)
        return
    arr[ind], arr[n-1-ind] = arr[n-1-ind], arr[ind]
    revAr(arr, ind+1)


revAr([1,2,3,4,5,6,8,7,8,8,8], 0)

    