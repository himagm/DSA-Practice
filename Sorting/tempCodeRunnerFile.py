smallerLeftSubarray = j - 1 - left < right - (j + 1)
    if smallerLeftSubarray:
        helper(arr, left, j - 1)
        helper(arr, j + 1, right)
    else:
        helper(arr, j + 1, right)
        helper(arr, left, j - 1)