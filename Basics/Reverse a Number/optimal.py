# Optimal Way

"""
Time Complexity: O(log10 N)
Space Complexity: O(1)
"""
def reverseNum(num):
    reversed_num = 0
    n = num
    while n:
        rem = n % 10
        reversed_num = reversed_num * 10 + rem
        n = n // 10

    return reversed_num


print(reverseNum(3102))
