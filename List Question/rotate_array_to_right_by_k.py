# Brute Force

# def rotate(nums, k):
#     print(nums)
#     if len(nums) < k:
#         while k > 0:
#             nums.insert(0, nums[-1])
#             nums.pop()
#             k -= 1
#     else:
#         nums[:] = nums[-k:] + nums[:-k]

#     print(nums)

# rotate([1,2,3,4], 4)
#Above can be written as
# def rotate(nums, k):
#     k = k % len(nums)
#     nums[:] = nums[-k:] + nums[:-k]

#     print(nums)

# rotate([1,2,3,4], 7)
# rotate([1,2,3,4], 3)

# Optimal - Using pointers

# divide the array into 2 parts [:k] and [k:]
# then reverse [:k] 
# next reverse [k:]
# finally reverse the entire array
def reverse(arr, start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate(nums, k):
    if len(nums) == k:
        return nums
    k = k % len(nums)
    reverse(nums, 0,len(nums)-k-1)
    reverse(nums, len(nums)-k, len(nums)-1)
    reverse(nums,0,len(nums)-1)

    # Below won't work because you have to pass positive indices to reverse. Otherwise start < end won't be satisfied
    # reverse(nums, 0,-k-1)
    # reverse(nums, -k, len(nums)-1)
    # reverse(nums,0,len(nums)-1)

    return nums

print(rotate([1,2,3,4], 2))