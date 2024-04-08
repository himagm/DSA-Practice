def longestSuccessiveElements(a):
    my_set = set(a)
    print(a,my_set)
    longest = 0
    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            while x + 1 in my_set:
                count += 1
                x += 1
            longest = max(longest, count)
    return longest

print(longestSuccessiveElements([5, 8, 3, 2, 1, 4]))


# print(longestSuccessiveElements([5,4,3]))
# print(longestSuccessiveElements([1,2,2,1]))
print(longestSuccessiveElements([15 ,6 ,2 ,1 ,16 ,4 ,2 ,29 ,9 ,12 ,8 ,5 ,14 ,21 ,8 ,12, 17 ,16 ,6 ,26 ,3]) )

"""    a[:] = list(set(a))
    print(a)
    counter,temp = 1,1
    for i in range(len(a)-1):
        if a[i] + 1 == a[i+1]:
            temp += 1
        else:
            counter = max(counter,temp)
            temp = 1
        

    return max(counter,temp)"""