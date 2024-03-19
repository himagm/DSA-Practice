def getSecondOrderElements(n,  a):
    # Write your code here.
    max,second_max = int(-1e9), int(-1e9)
    min,second_min = int(1e9), int(1e9)

    # for i in a:
    #     if i > max:
    #         second_max = max
    #         max = i
    #     elif i > second_max and i != max:
    #         second_max = i            

    #     if i < min:
    #         second_min = min
    #         min = i
    #     elif i < second_min and i != min:
    #         second_min = i            

    for i in a:
        if i > max:
            max = i
                    

        if i < min:
            min = i

    for i in a:
        if i > second_max and i != max:
                second_max = i
        if i < second_min and i != min:
                second_min = i

    return [second_max, second_min]

print(getSecondOrderElements(5,[1, 2, 3, 4, 5]))