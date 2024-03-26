# TC - O(N) SC - O(1)

def check(nums):
    count = 0
    for i in range(len(nums)):
        #can also use 
        #if nums[i] > nums[(i+1) % len(nums)]
        if nums[i-1] > nums[i]:
            count += 1
    
    return count <= 1
    
    
    


print(check([3,4,5,1,2]))
print(check([3,4,5]))
print(check([3,4,5,1,2,6]))
print(check([7,9,10,6,9]))