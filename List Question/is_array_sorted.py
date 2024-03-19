def isSorted(n,  a):
    # Write your code here.
    for i in range(n-1):
        if a[i] > a[i+1]:
            return 0
    
    return 1

print(isSorted(5, [5,1,2,3,4,5]))