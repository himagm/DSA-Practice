# Method 1
"""total = 0
def sumOf(i,n):
    global total
    if i>n:
        return
    total += i

    sumOf(i+1, n)

sumOf(1,5)

print(total)"""

# Method 2 - parameterized
"""
def sumOf(i, sum):
    if i < 1:
        print(sum)
        return
    sumOf(i-1,sum+i)

sumOf(5,0)
"""
#method 3 - functionaly way

def addi(n):
    if n == 1:
        return 1
    
    return n + addi(n-1)

    
print(addi(5))

"""def addition(n):
    if n == 1:
        return 1
    return n + addition(n - 1)

print(addition(5))"""