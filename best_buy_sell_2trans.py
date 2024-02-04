"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
import sys


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0

        N = len(prices)
        max_profits = [0] * N
        min_price_till = prices[0]
        max_price_asof = prices[-1]
        max_profit_till, max_profit_asof = 0, 0
        max_profit = 0
        for i in range(1, N):
            max_profit_till = max(prices[i] - min_price_till, max_profit_till)
            max_profits[i] += max_profit_till
            min_price_till = min(prices[i], min_price_till)

            j = N - i
            max_profit_asof = max(max_price_asof - prices[j], max_profit_asof)
            max_profits[j - 1] += max_profit_asof
            max_price_asof = max(prices[j], max_price_asof)

            max_profit = max(max_profits[i], max_profits[j - 1], max_profit)

        return max_profit

    def max_profit2(self, prices: [int]) -> int:
        first_buy = -sys.maxsize
        first_sell = 0
        second_buy = -sys.maxsize
        second_sell = 0

        for i in range(len(prices)):
            first_buy = max(first_buy, -prices[i])
            first_sell = max(first_sell, first_buy + prices[i])
            second_buy = max(second_buy, first_sell - prices[i])
            second_sell = max(second_sell, second_buy + prices[i])

        return second_sell


s = Solution()
assert s.max_profit2([8, 3, 2, 6, 1, 1, 1, 3, 2, 4, 9, 8, 7, 10]) == 13
assert s.max_profit2([5, 1, 3, 2, 6,4, 6, 7, 5, 5, 3, 0, 8, 3]) == 14
assert s.max_profit2([3,3,5,0,0,3,1,4]) == 6
assert s.max_profit2([1,2,3,4,5]) == 4
assert s.max_profit2([7,6,4,3,1]) == 0
assert s.max_profit2([1]) == 0

assert s.maxProfit([2, 30, 15, 10, 8, 25, 80]) == 100
assert s.maxProfit([8, 3, 2, 6, 1, 1, 1, 3, 2, 4, 9, 8, 7, 10]) == 13
assert s.maxProfit([5, 1, 3, 2, 6, 4, 6, 7, 5, 5, 3, 0, 8, 3]) == 14
assert s.maxProfit([3,3,5,0,0,3,1,4]) == 6
assert s.maxProfit([1,2,3,4,5]) == 4
assert s.maxProfit([7,6,4,3,1]) == 0
assert s.maxProfit([1]) == 0
