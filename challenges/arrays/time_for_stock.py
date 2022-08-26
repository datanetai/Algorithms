# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# dynamic programming O(n) time complexity
def maxProfit(prices: list[int]) -> int:
    max_pr = 0
    max_sofar = 0
    for i in range(1,len(prices)):
        max_sofar += prices[i] - prices[i-1]
        if max_sofar < 0:
            max_sofar = 0
        if max_sofar > max_pr:
            max_pr = max_sofar
        

    return max_pr

# solution2 O(n) time complexity
def maxProfit2(prices: list[int]) -> int:
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit > max_profit:
            max_profit = profit
        if profit < 0:
            left = right
        right += 1
    return max_profit
l= [7,1,5,3,6,4]
print(maxProfit(l))