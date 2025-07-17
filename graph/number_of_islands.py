from typing import List


def num_islands(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    islands = 0

    def dfs(i, j):
        grid[i][j] = 0
        for k in range(4):
            neighbour_x = i + dx[k]
            neighbour_y = j + dy[k]
            if 0 <= neighbour_x < m and 0 <= neighbour_y < n and grid[neighbour_x][neighbour_y] == 1:
                dfs(neighbour_x, neighbour_y)

    for x in range(m):
        for y in range(n):
            if grid[x][y] == 0:
                continue

            dfs(x, y)
            islands += 1

    return islands


assert num_islands([
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]) == 1


