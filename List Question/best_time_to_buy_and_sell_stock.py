def maxProfit(prices):
    buy = prices[0]
    profit = 0
    for i in prices:
        if i < buy:
            buy = i
        elif i - buy > profit:          
            profit = i - buy
    return profit
    
# arr = [7,1,5,3,6,4]
# arr = [2,4,1]
# arr = [7,6,4,3,1]
arr = [3,2,6,5,0,3]
print(maxProfit(arr))

"""
def maxProfit(prices):
        max_profit = 0
        min_price = float("inf")
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit"""
"""
    i, buy_ind = 0, 0
    buy = prices[0]
    # print(type(buy), buy_ind)
    while i < len(prices)-1:
        # print(type(prices[i]))
        if prices[i] < buy:
            buy_ind = i
            buy = prices[i]
        i += 1
    
    print(buy, buy_ind)
    # if buy_ind == len(prices) -1:
    #     return 0
    
    j = buy_ind + 1
    profit = 0
    while j < len(prices):
        profit = max(profit, (prices[j] - buy))
        j += 1

    return profit
    """
"""
def maxProfit(prices):
    profit = 0
    for i in range(len(prices)-1, 0, -1):
        small = min(prices[0:i])
        profit = max(profit, (prices[i]-small))
    return profit 
  """  