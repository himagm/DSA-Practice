def check(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i-1] > nums[i]:
            count += 1
    
    return count <= 1
    
    
    


print(check([3,4,5,1,2]))
print(check([3,4,5]))
print(check([3,4,5,1,2,6]))