# Also known as Dutch National Flag Algorithm
def sortColors(nums):
    left = 0
    right = len(nums) -1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[left],nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1

    print(nums)

sortColors([2,0,2,1,1,0])
sortColors([2,0,2,1,0,1])
