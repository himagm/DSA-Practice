def removeDuplicates(nums):
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
    nums[:] = sorted(set(nums))
    print(nums)
    return len(nums)

removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])

