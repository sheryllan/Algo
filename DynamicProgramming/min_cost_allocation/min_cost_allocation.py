from typing import List
from math import inf
from functools import cache


def min_cost_dfs(M: int, cost: List[List[int]]) -> int:
    m = M / 2

    @cache
    def dfs(i, a):
        if i < 0 and a == 0:
            return 0
        if i < 0:
            return inf

        if a < max(i - m + 1, 0):
            return inf

        cost_a, cost_b = cost[i]
        return min(dfs(i - 1, a - 1) + cost_a, dfs(i - 1, a) + cost_b)

    return dfs(M-1, m)


# assert min_cost_dfs(2, [[10, 30], [30, 200]]) == 60
# assert min_cost_dfs(4, [[10, 30], [10, 50], [30, 200], [20, 30]]) == 100


def min_cost_iterative(M: int, cost: List[List[int]]) -> int:
    m = M // 2

    dp = [inf] * (m + 1)
    dp[0] = 0

    for i, (cost_a, cost_b) in enumerate(cost):
        for j in range(min(m - 1, i), max(i - m, 0) - 1, -1):
            dp[j + 1] = min(dp[j] + cost_a, dp[j + 1] + cost_b)

        if i - m <= 0:
            dp[0] += cost_b

    return dp[m]

assert min_cost_iterative(2, [[10, 30], [30, 200]]) == 60
assert min_cost_iterative(4, [[10, 30], [10, 50], [30, 200], [20, 30]]) == 100

