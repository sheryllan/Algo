"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# recursion -> top-down
class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 1

        def rcsv_build(start: int, stop: int):
            count = memo[stop - start]
            if count:
                return count

            for i in range(start, stop):
                n_left = rcsv_build(start, i)
                n_right = rcsv_build(i + 1, stop)
                count += (n_left * n_right)

            memo[stop - start] = count
            return count

        return rcsv_build(0, n)


solution = Solution()
assert solution.numTrees(7) == 429
assert solution.numTrees(3) == 5



# memoization - bottom-up
"""
memo[i] = sum(2 * memo[j] * memo[i - 1 - j]), j ranging from 0 to (i - 1)/2
if int((i - 1) % 2) == int(i / 2), then memo[i] = memo[i] + memo[(i - 1)/2]^2
"""

class Solution2:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = 1

        for i in range(1, n + 1):
            k = int((i - 1) / 2)
            memo[i] = sum(2 * memo[j] * memo[i - 1 - j] for j in range(k + 1) if j != i - 1 - j)
            if k == int(i / 2):
                memo[i] += (memo[k] * memo[k])

        return memo[n]


solution2 = Solution2()
assert solution2.numTrees(7) == 429
assert solution2.numTrees(3) == 5
assert solution2.numTrees(10) == 16796



