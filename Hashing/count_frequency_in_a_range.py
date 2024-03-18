# https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446

def countFrequency(n,x,arrr):
    res = [0] * n
    for i in arrr:
        if i <= n:
            res[i-1] += 1
    
    return res

print(countFrequency(10,28,[18 ,21 ,20 ,5 ,12 ,15 ,18 ,26 ,6 ,3]))

