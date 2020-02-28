"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

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
        # coins_desc = sorted(coins, reverse=True)
        #
        # def change_rcsv(idx: int, rem: int):
        #     if idx >= len(coins_desc):
        #         return -1 if rem != 0 else 0
        #
        #     coin = coins_desc[idx]
        #     if rem % coin == 0:
        #         return rem // coin
        #     min_count = -1
        #     for k in range(rem // coin, -1, -1):
        #         rem_k = rem - coin * k
        #         with_k_coin = change_rcsv(idx + 1, rem_k)
        #         if with_k_coin == -1:
        #             continue
        #         min_count = (k + with_k_coin) if min_count == -1 else min(k + with_k_coin, min_count)
        #
        #     return min_count
        #
        # return change_rcsv(0, amount)

        counts = [0] + [-1] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                if counts[i - coin] == -1:
                    continue
                n = counts[i - coin] + 1
                counts[i] = n if counts[i] == -1 else min(counts[i], n)

        return counts[amount]




solution = Solution()

assert solution.coinChange([1, 2, 5], 11) == 3

assert solution.coinChange([1, 4, 7, 6], 16) == 3

assert solution.coinChange([3, 4, 5], 21) == 5

assert solution.coinChange([405, 3, 436, 7], 25)

