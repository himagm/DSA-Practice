# from collections import Counter
# Using Moore's Voting Algorithm
def majorityElement(nums):
    candidate = nums[0]
    count = 0
    for i in range(len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            candidate = nums[i]
            count = 1
    
    return candidate



nums = [3,2,3,3,4,5,5,4,4,4,4,4,4]
print(majorityElement(nums))
"""nums.sort()
    return nums[(len(nums)-1)//2]"""

"""    print(Counter(nums))
    for [x, cnt] in Counter(nums).items():
        if cnt >= len(nums)//2:
            return x

    return -1"""
"""
    for i in set(nums):
        if nums.count(i) > len(nums)/2:
            return i
"""
"""
counter = 0
        c = {}
        half = len(nums) // 2
        for i in range(len(nums)):
            if nums[i] in c:
                c[nums[i]] += 1
            else:
                c[nums[i]] = 1
        
        for key,value in c.items():
            if value > half:
                return key

"""