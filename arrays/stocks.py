# you are given an array prices where prices[i] is the price of a give stock
# on the ith day. yu want to maximize the profit by choosing a single day to buy
# one stock and choosing a different day in future to sell that stock.
# return the maximum profit you can achieve from this transaction.
# if you cannot achieve any profit, return 0.

class Solution:

    def max_Profit (self, prices):

        if len(prices) < 2: return 0  # stocks can be bought and sold at the same price without making a profit
        if len(prices) == 2:
            if prices[1] - prices[0] >= 0:
                return prices[1] - prices[0]
            else:
                return 0

        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]

        return profit