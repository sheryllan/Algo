from math import inf
from typing import List

# 恰好
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 递推
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        f[0][1][0] = 0  # 只需改这里
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                f[i + 1][j][0] = max(f[i][j][0], f[i][j][1] + p)
                f[i + 1][j][1] = max(f[i][j][1], f[i][j - 1][0] - p)
        return f[-1][-1][0]

        # 记忆化搜索
        # @cache
        # def dfs(i: int, j: int, hold: bool) -> int:
        #     if j < 0:
        #         return -inf
        #     if i < 0:
        #         return -inf if hold or j > 0 else 0
        #     if hold:
        #         return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
        #     return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])
        # return dfs(n - 1, k, False)

# 至少
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 递推
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        f[0][0][0] = 0
        for i, p in enumerate(prices):
            f[i + 1][0][0] = max(f[i][0][0], f[i][0][1] + p)
            f[i + 1][0][1] = max(f[i][0][1], f[i][0][0] - p)  # 无限次
            for j in range(1, k + 1):
                f[i + 1][j][0] = max(f[i][j][0], f[i][j][1] + p)
                f[i + 1][j][1] = max(f[i][j][1], f[i][j - 1][0] - p)
        return f[-1][-1][0]

        # 记忆化搜索
        # @cache
        # def dfs(i: int, j: int, hold: bool) -> int:
        #     if i < 0:
        #         return -inf if hold or j > 0 else 0
        #     if hold:
        #         return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
        #     return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])
        # return dfs(n - 1, k, False)
