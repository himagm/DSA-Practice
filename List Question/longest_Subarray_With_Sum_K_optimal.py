def longestSubarrayWithSumK(arr,k):
    sum =arr[0]
    left,right,size = 0 , 0, 0

    while right < len(arr):
        if sum < k:
            right += 1
            if right < len(arr):
                sum += arr[right]
        elif sum > k:
            sum -= arr[left]
            left += 1
        else:
            size = max(size, right-left+1)
            right += 1            
            if right < len(arr):
                sum += arr[right]
    
    return size


tst= [1, 2, 3, 1, 1, 1, 1]
print(longestSubarrayWithSumK(tst, 3))