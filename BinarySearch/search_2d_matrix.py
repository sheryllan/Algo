"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-1e4 <= matrix[i][j], target <= 1e4
"""

from typing import List


class Solution:
    def binary_search(self, nums, target):
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                return mid, mid

        return left, right


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, n - 1
        if target == matrix[i][j]:
            return True

        if target < matrix[i][j]:
            col, _ = self.binary_search(matrix[0], target)
            if col < 0:
                return False
            nums = [matrix[x][col] for x in range(m)]
            row_start, row_end = self.binary_search(nums, target)
            return matrix[row_start][col] == target
        else:
            nums = [matrix[x][n - 1] for x in range(m)]
            _, row = self.binary_search(nums, target)
            if row > m - 1:
                return False
            col_start, col_end = self.binary_search(matrix[row], target)
            return matrix[row][col_start] == target


s = Solution()
assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
assert not s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)