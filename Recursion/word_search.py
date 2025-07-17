"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

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


s = Solution()
assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
assert s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")