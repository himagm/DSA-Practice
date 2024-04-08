def missingNumber(nums):

    n = len(nums)
    v = [-1] * (n+1)

    for num in nums:
        v[num] = num
    
    for i in range(len(v)):
        if v[i] == -1:
            return i
    # return sum(list(range(len(nums) + 1 ))) - sum(nums)
    # or    
    # n = len(nums)
    # for i in range(n+1):
    #     if i not in nums:
    #         return i


nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))