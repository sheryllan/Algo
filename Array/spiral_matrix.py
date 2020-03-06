"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix) -> [int]:

        def loop(i_min, i_max, j_min, j_max):
            i, j = 0, 0
            while i_min < i_max and j_min < j_max:
                if i == i_min and j == j_min:
                    yield from matrix[i][j: j_max]
                    j = j_max - 1
                    i_min += 1
                    i = i_min
                elif i == i_min and j < j_max:
                    yield from (matrix[x][j] for x in range(i, i_max))
                    i = i_max - 1
                    j_max -= 1
                    j = j_max
                elif i < i_max and j == j_max:
                    yield from reversed(matrix[i][j_min: j])
                    j = j_min
                    i_max -= 1
                elif i == i_max and j == j_min:
                    yield from (x[j] for x in reversed(matrix[i_min: i]))
                    j_min += 1
                    j = j_min
                    i = i_min

        return list(loop(0, len(matrix), 0, (len(matrix[0]) if matrix else 0)))



solution = Solution()
sm = solution.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
])

print(sm)

sm = solution.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
print(sm)

sm = solution.spiralOrder([[], [], []])
print(sm)




