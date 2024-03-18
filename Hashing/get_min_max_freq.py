from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    my_dict = {}
    for i in v:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    
    # print(my_dict)

    min_num, min_freq = float('inf'), float('inf')
    max_num, max_freq = float('-inf'), float('-inf')
    for num, freq in my_dict.items():
        if freq < min_freq:
            min_num = num
            min_freq = freq
        elif freq == min_freq:
            if num < min_num:
                min_num = num
                min_freq = freq
        
        if freq > max_freq:
            max_num = num
            max_freq = freq
        elif freq == max_freq:
            if num < max_num:
                max_num = num
                max_freq = freq
    
    return [max_num, min_num]

    # print(min_num, min_freq)
    # print(max_num, max_freq)
"""
    max_num, max_freq = float('-inf'), float('-inf')
    for num, freq in my_dict.items():
        if freq > max_freq:
            max_num = num
            max_freq = freq
        elif freq == max_freq:
            if num < max_num:
                max_num = num
                max_freq = freq
"""


print(getFrequencies([1 ,2,2,2, 3 ,1 ,1 ,4]))