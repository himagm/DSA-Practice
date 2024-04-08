from collections import Counter
def findMissingRepeatingNumbers(a):
    missing, repeat = a[0], a[0]
    n = len(a)
    # my_dict = {x:0 for x in range(1, n+1)}
    # print(my_dict)
    b = Counter(a)
    print(b)
    for i in range(1,n+1):
        if i not in b:
            missing = i
        if b[i] == 2:
            repeat = i
    print(missing)
    print(repeat)
findMissingRepeatingNumbers([1,2,2])