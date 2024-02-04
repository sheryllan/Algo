"""
A robot is located in the top-left corner of a m×n grid (marked ‘Start’ in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).
How many possible unique paths are there?
"""


def bottom_up_search(m, n):
    paths = [[0] * (n + 1)] * (m + 1)
    paths[m][n - 1] = 1
    paths[m - 1][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            paths[i][j] = paths[i + 1][j] + paths[i][j + 1]

    return paths[0][0]
