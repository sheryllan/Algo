"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


"""
Consider coins = [7, 6, 4, 1], and amount = 16
    16 = 7 * 2 + 1 * 2 = 6 * 2 + 4 * 1
the resulting number of coins is 4 and 3.
If the biggest number is considered as priority, then it isn't the minimum.
"""

class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        counts = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                n = counts[i - coin] + 1
                counts[i] = min(counts[i], n)

        return counts[amount]



solution = Solution()

assert solution.coinChange([1, 2, 5], 11) == 3

assert solution.coinChange([1, 4, 7, 6], 16) == 3

assert solution.coinChange([3, 4, 5], 21) == 5

assert solution.coinChange([405, 3, 436, 7], 25)

