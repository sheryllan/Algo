"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100
"""


from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def dfs(i, j):
            if i == 0 and j == 0:
                return 1

            paths = 0
            if i > 0:
                paths += dfs(i - 1, j)
            if j > 0:
                paths += dfs(i, j - 1)

            return paths

        return dfs(m - 1, n - 1)


class Solution2:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     f = [[1] * n for _ in range(m)]
    #
    #     for i in range(m - 1):
    #         for j in range(n - 1):
    #             f[i + 1][j + 1] = (f[i][j + 1] + f[i + 1][j])
    #
    #     return f[m-1][n-1]

    def uniquePaths(self, m, n):
        dp = [[1]*n for _ in range(2)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-1]
        return dp[(m-1)&1][-1]


assert Solution2().uniquePaths(3, 7) == 28
assert Solution2().uniquePaths(3, 2) == 3
assert Solution2().uniquePaths(1, 1) == 1