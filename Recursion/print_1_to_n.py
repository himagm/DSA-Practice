
# without backtracking
def onetoN(i, n):
    if i > n:
        return
    print(i)
    onetoN(i+1, n)

# With Backtracking
def printtoN(n):
    if n == 1:
        print(1)
        return
    printtoN(n-1)
    print(n)

# With Backtracking
def printOneToN(i,n):
    if i < 1:
        return
    printOneToN(i - 1, n)
    print(i)

if __name__ == "__main__":

    onetoN(1,5)
    printtoN(5)
    printOneToN(5,5)