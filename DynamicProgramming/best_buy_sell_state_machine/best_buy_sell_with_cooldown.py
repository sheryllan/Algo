"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0_0 = 0  # the day before yesterday no position
        f1_0 = 0  # yesterday no position
        f1_1 = -inf  # yesterday with position

        for p in prices:
            # f0 denotes today
            new_f0_0 = max(f1_0, f1_1 + p)
            f0_1 = max(f1_1, f0_0 - p)
            f0_0 = new_f0_0

            # swap the value, f1 -> f0 so that f0 becomes the day before yesterday, and
            # new_f0 -> f1 so that f1 becomes yesterday again, ready for the next iteration
            f0_0, f1_0 = f1_0, f0_0
            f0_1, f1_1 = f1_1, f0_1

        # f1 is transferred from the new f0
        return f1_0


s = Solution()
assert s.maxProfit([1,2,3,0,2]) == 3
assert s.maxProfit([1]) == 0
assert s.maxProfit([6,5,4]) == 0
assert s.maxProfit([3, 7, 2, 5, 8]) == 7
assert s.maxProfit([]) == 0