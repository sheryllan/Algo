"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    # def generateMatrix(self, n: int):
    #     matrix = [[0] * n for _ in range(n)]
    #     i, j = 0, 0
    #     top, bottom, left, right = 0, n - 1, 0, n - 1
    #
    #     for x in range(1, n * n + 1):
    #         matrix[i][j] = x
    #
    #         if i == top and j < right:
    #             j += 1
    #         elif j == right and i < bottom:
    #             i += 1
    #         elif i == bottom and j > left:
    #             j -= 1
    #         elif j == left and i > top:
    #             i -= 1
    #
    #         if i == top and j == left:
    #             top += 1
    #             bottom -= 1
    #             left += 1
    #             right -= 1
    #
    #             i, j = top, left
    #
    #     return matrix


    def generateMatrix(self, n: int):
        n_dim = n - 1
        matrix = [[0] * n for _ in range(n)]
        start = 1
        while n_dim > 0:
            i = int((n - n_dim - 1) / 2)
            numbers = range(start, start + 4 * n_dim)
            matrix[i][i:i + n_dim] = numbers[: n_dim]
            matrix[i + n_dim][i + 1:i + n_dim + 1] = numbers[3 * n_dim - 1: 2 * n_dim - 1:  -1]
            for i_row, x, y in zip(range(i, i + n_dim),
                                   numbers[1 * n_dim: 2 * n_dim],
                                   numbers[4 * n_dim - 1: 3 * n_dim - 1: -1]):
                matrix[i_row][i + n_dim] = x
                matrix[i_row + 1][i] = y

            start = numbers[-1] + 1
            n_dim -= 2

        if n_dim == 0:
            i = int((n - 1) / 2)
            matrix[i][i] = n * n

        return matrix





solution = Solution()
for y in solution.generateMatrix(0):
    print(y)


"""
Solution 1: Build it inside-out - 44 ms, 5 lines

Start with the empty matrix, add the numbers in reverse order until we added the number 1. Always rotate the matrix clockwise and add a top row:

    ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                     |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                         |8 7|      |7 6 5|
The code:

def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
While this isn't O(n^2), it's actually quite fast, presumably due to me not doing much in Python but relying on zip and range and + being fast. I got it accepted in 44 ms, matching the fastest time for recent Python submissions (according to the submission detail page).




Solution 2: Ugly inside-out - 48 ms, 4 lines

Same as solution 1, but without helper variables. Saves a line, but makes it ugly. Also, because I access A[0][0], I had to handle the n=0 case differently.

def generateMatrix(self, n):
    A = [[n*n]]
    while A[0][0] > 1:
        A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
    return A * (n>0)
    
    
    
    
Solution 3: Walk the spiral - 52 ms, 9 lines

Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. Make a right turn when the cell ahead is already non-zero.

def generateMatrix(self, n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A
"""
