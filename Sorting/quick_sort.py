# https://mariam-jaludi.medium.com/sorting-algorithms-quick-sort-3e8f7bce8fc

def quickSort(arr):
    helper(arr, 0, len(arr) - 1)
    return arr

def helper(arr, left,right):
    if left >= right:
        return
    
    pivot = left
    i  = left + 1
    j = right

    while i < j:
        print(i)
        if arr[i] > arr[pivot] and arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] <= arr[pivot]:
            i += 1
        
        if arr[j] >= arr[pivot]:
            j -= 1
    arr[j], arr[pivot] = arr[pivot], arr[j]
    helper(arr, left, j - 1)
    helper(arr, j + 1, right)
    # smallerLeftSubarray = j - 1 - left < right - (j + 1)
    # if smallerLeftSubarray:
    #     helper(arr, left, j - 1)
    #     helper(arr, j + 1, right)
    # else:
    #     helper(arr, j + 1, right)
    #     helper(arr, left, j - 1)
    # if j - 1 - left > 1:
    #     helper(arr, left, j - 1)
    #     helper(arr, j + 1, right)
    # else:
    #     helper(arr, j + 1, right)



    

test = [5,4,3,2,1]
print(test)
# quickSort(test, 0 , len(test) -1)
quickSort(test)
print(test)