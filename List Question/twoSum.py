"""
def twoSum(nums, target):
        left = 0
        right = len(nums) -1

        for i in range(len(nums)-1):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i,j]
                    
"""

def twoSum(nums, target):
    # to store value and Index
    numToIndex = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in numToIndex:
            return [i,numToIndex[diff]]
        numToIndex[nums[i]] = i


print(twoSum([2,7,11,15], 9))