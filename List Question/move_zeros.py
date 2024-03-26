arr = [7,8,0,3,2,0,0,1,0,7,6,2]
# Optimal - TC - O(N) SC- O(1)
def moveZeros(arr):
    n = len(arr)
    i = 0
    if n <= 1:
        return
    while True:
        if arr[i] == 0:        
            break
        i += 1
    else:
        return

    # or
    #j = i + 1
    #while j < n:
        # if nums[j] != 0:
        #     arr[i], arr[j] = arr[j], arr[i]
        #     i += 1
        # j += 1

    for x in range(n):
        if arr[i] == 0 and arr[x] !=0 and x > i:
            arr[i], arr[x] = arr[x], arr[i]
            i += 1
    
    return arr

print(moveZeros(arr))



# def moveZeroes(nums):
#     res = []
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             res.append(nums[i])
    
#     if len(res) < len(nums):
#         diff = len(nums) - len(res)
#         res = res + ([0] * diff)
#     print(res)
    

# lst =[0,1,0,3,12]
# moveZeroes(lst)