def moveZeroes(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] != 0:
            res.append(nums[i])
    
    if len(res) < len(nums):
        diff = len(nums) - len(res)
        res = res + ([0] * diff)
    print(res)
    

lst =[0,1,0,3,12]
moveZeroes(lst)