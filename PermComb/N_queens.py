"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queens = [0] * n  # 皇后放在 (r,queens[r])
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)
        def dfs(r: int) -> None:
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return
            # 在 (r,c) 放皇后
            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:  # 判断能否放皇后
                    queens[r] = c  # 直接覆盖，无需恢复现场
                    col[c] = diag1[r + c] = diag2[r - c] = True  # 皇后占用了 c 列和两条斜线
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans

"""
答疑

问：本题和 46. 全排列 的关系是什么？

答：由于每行恰好放一个皇后，记录每行的皇后放在哪一列，可以得到一个 [0,n−1] 的排列 queens。示例 1 的两个图，分别对应排列 [1,3,0,2] 和 [2,0,3,1]。所以我们本质上是在枚举列号的全排列。

问：如何 O(1) 判断两个皇后互相攻击？

答：由于我们保证了每行每列恰好放一个皇后，所以只需检查斜方向。对于 ↗ 方向的格子，行号加列号是不变的。对于 ↖ 方向的格子，行号减列号是不变的。如果两个皇后，行号加列号相同，或者行号减列号相同，那么这两个皇后互相攻击。

问：如何 O(1) 判断当前位置被之前放置的某个皇后攻击到？

答：额外用两个数组 diag1和 diag2分别标记之前放置的皇后的行号加列号，以及行号减列号。如果当前位置的行号加列号在 diag1中（标记为 true），
或者当前位置的行号减列号在 diag2中（标记为 true），那么当前位置被之前放置的皇后攻击到，不能放皇后。

复杂度分析

时间复杂度：O(n^2⋅n!)。搜索树中至多有 O(n!) 个叶子，每个叶子生成答案每次需要 O(n^2) 的时间，所以时间复杂度为 O(n^2⋅n!)。
实际上搜索树中远没有这么多叶子，n=9 时只有 352 种放置方案，远远小于 9!=362880。更加准确的方案数可以参考 OEIS A000170，为 O(n!/2.54^n)。
空间复杂度：O(n)。返回值的空间不计入。


链接：https://leetcode.cn/problems/n-queens/solutions/2079586/hui-su-tao-lu-miao-sha-nhuang-hou-shi-pi-mljv/
"""