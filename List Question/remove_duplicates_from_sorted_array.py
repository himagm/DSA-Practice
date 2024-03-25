def removeDuplicates(nums):

    # or
    i = 1
    j = 1
    while j < len(nums)-1:
        if nums[j] != nums[j+1]:
            nums[i] = nums[j+1]
            i += 1
            j += 1
        else:
            j += 1

    print(i,j,nums)

    # k = 0
    # unique = []
    # dup = []
    # for i in nums:
    #     if i not in unique:
    #         unique.append(i)
    #     else:
    #         dup.append(i)
    # nums[:] = unique + dup
    # print(unique,dup, nums)

    # or
    # nums[:] = sorted(set(nums))
    # print(nums)
    # return len(nums)

    

removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])

