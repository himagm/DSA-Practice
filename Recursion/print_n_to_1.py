"""
Print N to 1 without BACKTRACKING
"""

def funct(i,n):
    if i < 1:
        return
    print(i)
    funct(i-1, n)

# funct(5,5)
"""
Print N to 1 with BACKTRACKING
"""

def funct2(i,n):
    if i > n:
        return
    funct2(i+1, n)
    print(i)

funct2(1,5)
