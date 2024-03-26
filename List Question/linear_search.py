
def linearSearch(n, num, arr) -> int:
    for i in range(n):
        if arr[i] == num:
            return i
    
    return -1


print(linearSearch( 5, 4, [6,7,8,4,1] ))