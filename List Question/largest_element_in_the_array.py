
# def largestElement(arr, n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i] > max:
#             max = arr[i]
    
#     return max
def largestElement(arr, n):
    arr.sort()
    print(arr)

print(largestElement([1,2,3,4,5,1,4],5))