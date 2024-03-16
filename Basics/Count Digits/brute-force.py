"""
Time Complexity: O(log10 n) where n is the number
Space Complexity: O(1)

"""

def countDigit(n): 
    count = 0
    num = n
    while n:
        count += 1
        n = n // 10
    
    return count

print(countDigit(1234))
