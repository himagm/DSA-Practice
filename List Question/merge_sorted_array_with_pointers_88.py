def merge(nums1, m, nums2, n):
    if m == 0 and n > 0:
        nums1[:] = nums2[:]
    
    elif m > 0 and n > 0:
        k = m
        i = 0
        j = 0
        while i <= m and j < n:
            print(i, j)
            if nums1[i] < nums2[j]:
                i += 1
            else:
                z = k
                while z > i:
                    nums1[z] = nums1[z-1]
                    z -= 1
                nums1[i] = nums2[j]
                i += 1
                k += 1
                j += 1
        print(f"i = {i}, j = {j}, k={k}")
        
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1



tst1 = [1,2,3,0,0,0]
tst2 = [4,5,6]
merge(tst1, 3, tst2, 3)
print(tst1)

# tst1 = [1,2,3,0,0,0]
# tst2 = [2,5,6]
# merge(tst1, 3, tst2, 3)
# print(tst1)

# tst1 = [1]
# tst2 = []
# merge(tst1, 1, tst2, 0)
# print(tst1)