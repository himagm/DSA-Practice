
def sortedArray(a, b):
    # Write your code here
    i,j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] in res:
            i += 1
        elif b[j] in res:
            j += 1
        else:
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            elif b[j] < a[i]:
                res.append(b[j])
                j += 1
            elif b[j] == a[i]:
                res.append(a[i])
                i += 1
                j += 1
    
    while i < len(a) and a[i] not in res:
        res.append(a[i])
        i += 1
    while j < len(b) and b[j] not in res:
        res.append(b[j])
        j += 1
    
    return res

    # or
    # res = list(set(a+b))
    # res.sort()

    
    
    # return res

# a = [1, 2, 3, 4, 6]
# b = [2, 3, 5]

a= [1,2,3,3]
b = [2,2,4]
print(sortedArray(a,b))