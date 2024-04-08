def maxProduct(nums):
    prod = 1
    maxi = float('-inf')
    for i in nums:
        
        prod = prod * i
        if i > prod:
            maxi = max(maxi, i)
        else:
            maxi = max(maxi, prod)
    return maxi

print(maxProduct([0,2]))