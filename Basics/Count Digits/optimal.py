"""
Time complexity : O(1)
Space Complexity: O(1)

"""

import math

def count_digits(num):
    return math.floor(math.log10(num) + 1)


print(count_digits(1234))

