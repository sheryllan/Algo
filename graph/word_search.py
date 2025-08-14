"""

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, k):
            if k == l:
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if visited[i][j] or board[i][j] != word[k]:
                return False

            visited[i][j] = True
            found = dfs(i, j - 1, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1)
            visited[i][j] = False
            return found

        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True

        return False



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        visited = [[0] * n for _ in range(m)]
        neighbours = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def dfs(i, j, word_i):
            if board[i][j] != word[word_i]:
                return False

            if word_i == l - 1:
                return True

            visited[i][j] = 1
            for dx, dy in neighbours:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if dfs(x, y, word_i + 1):
                        return True

            visited[i][j] = 0
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False




s = Solution()
assert not s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
assert s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")