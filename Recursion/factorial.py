# Functional way

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(6))


# Parameterized way

def facto(n, fac):
    if n < 1:
        print(fac)
        return
    
    facto(n -1, fac * n)

facto(6,1)