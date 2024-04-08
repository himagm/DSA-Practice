def longestSubarrayWithSumK(arr,k):
    index = 0
    total = 0
    size = 0
    sumToIndex = {}
    while index < len(arr):
        total += arr[index]
        # sumToIndex[total] = index
        if total == k:
            size = max(size, index + 1)
        
        diff = total - k
        if diff in sumToIndex:
            size = max(size, (index - sumToIndex[diff]))
        
        if total not in sumToIndex:
            sumToIndex[total] = index

        index += 1

    print(size)

# longestSubarrayWithSumK([1, 2, 3, 1, 1, 1, 1], 3)
# longestSubarrayWithSumK([2, 2 ,4 ,1 ,2 ], 3)
longestSubarrayWithSumK([0 ,2 ,5 ,3 ,3 ,4 ,4 ,3 ,0 ,5 ,5 ,4 ,4 ,4 ,3 ,2 ,0 ,2 ,3 ,1 ,3 ,0 ,4 ,3 ,1 ,4 ,5 ,2 ,4 ,3 ,1 ,4 ,5 ,0 ,3 ,4 ,0 ], 52)
print(len([0 ,2 ,5 ,3 ,3 ,4 ,4 ,3 ,0 ,5 ,5 ,4 ,4 ,4 ,3 ,2 ,0 ,2 ,3 ,1 ,3 ,0 ,4 ,3 ,1 ,4 ,5 ,2 ,4 ,3 ,1 ,4 ,5 ,0 ,3 ,4 ,0 ]))
print(sum([0 ,2 ,5 ,3 ,3 ,4 ,4 ,3 ,0 ,5 ,5 ,4 ,4 ,4 ,3 ,2 ,0 ,2 ,3 ,1 ,3 ,0 ,4 ,3 ,1 ,4 ,5 ,2 ,4 ,3 ,1 ,4 ,5 ,0 ,3 ,4 ,0 ]))
# 37 52
# [0 ,2 ,5 ,3 ,3 ,4 ,4 ,3 ,0 ,5 ,5 ,4 ,4 ,4 ,3 ,2 ,0 ,2 ,3 ,1 ,3 ,0 ,4 ,3 ,1 ,4 ,5 ,2 ,4 ,3 ,1 ,4 ,5 ,0 ,3 ,4 ,0 ]