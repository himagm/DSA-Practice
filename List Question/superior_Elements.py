# you are starting from the right, and you will keep finding the largest and compare it with the previously found largest, 
# if the current largest is greater than the previous largest, it is obviously greater than all the elements to it;s right
def superiorElements(a):
    res = [a[-1]]
    last_greatest = a[-1]
    for i in range(len(a)-2,-1,-1):
        greater = max(last_greatest,a[i])
        if greater > last_greatest:
            res.append(a[i])
            last_greatest = greater
    return res


print(superiorElements([5,4,3]))
print(superiorElements([187 ,64 ,133 ,62 ,49 ,163 ,50 ,115 ,42 ,65 ,60 ,49 ,32 ,87 ,141 ,142 ,146 ,159]))

"""    for i in range(len(a)-1):
        for j in range(i + 1, len(a)):
            if a[i] < a[j]:
                break
        print(j)
        if j == len(a):
            res.append(a[i])
    
    return res"""





"""    i, j = 0, 0
    n = len(a)
    res=[a[-1]]
    while i < len(a) -1:
        j = i + 1
        while j < len(a):
            # print(f"j value is {j}")
            if a[i] > a[j]:
                # print("entered if loop")
                j += 1
            else:
                break
            
            
        # print(j)
        if j == len(a):
            res.append(a[i])
        
        i += 1
    
    return res"""



# superiorElements()
# print(superiorElements([1, 2, 3, 2]))
# print(superiorElements([1, 2, 2, 1]))

"""n = len(a)
    end = n-2
    out = [a[-1]]
    while end >= 0:
        if a[end] > a[end+1]:
            out.append(a[end])
        
        end -= 1
        # else:
        #     return out
    
    return out"""

 

