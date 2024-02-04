"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""

from decode_ways import s
print(s.numDecodings('10'))

class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        combinations = [0] * (amount + 1)
        combinations[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                combinations[i] += combinations[i - coin]

        return combinations[amount]


solution = Solution()

print(solution.change(100, [1, 2, 5, 20, 50, 100]))

assert solution.change(100, [20, 2, 1, 5, 50]) == 1441

assert solution.change(5, [1, 2, 5]) == 4

assert solution.change(3, [2]) == 0

assert solution.change(16, [1, 4, 7, 6]) == 15




"""
The above algo is distinct from the following which calculates the number in the composition, 
where A is the given set of numbers, and N is the target sum 
"""

def count(A, N):
    sums = [1] + [0] * N
    for i in range(1, N + 1):
        for a in A:
            if i < a:
                continue

            sums[i] += sums[i - a]

    return sums[N]

assert count([1, 2, 8], 13) == 415
