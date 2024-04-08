def rearrangeArray(nums):
        left, right, res = 0, 1, ([0] * len(nums))

        for i in nums:
            if i >= 0:
                res[left] = i
                left += 2
            else:
                res[right] = i
                right += 2
                

        return res

print(rearrangeArray([3,1,-2,-5,2,-4]))
print(rearrangeArray([-1,1]))


"""
        pos, neg, res = [], [], []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        print(pos, neg)
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        print(res)
"""