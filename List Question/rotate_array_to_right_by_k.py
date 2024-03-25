def rotate(nums, k):
    print(nums)
    if len(nums) < k:
        while k > 0:
            nums.insert(0, nums[-1])
            nums.pop()
            k -= 1
    else:
        nums[:] = nums[-k:] + nums[:-k]

    print(nums)

rotate([1,2,3,4], 4)
