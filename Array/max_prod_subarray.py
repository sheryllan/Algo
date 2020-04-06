"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: [int]) -> int:
        if not nums:
            return 0

        max_prod = nums[0]
        cum_prod = 1
        prod_from_neg = 1

        for n in nums:
            if n > 0:
                prod_from_neg *= n
                cum_prod *= n
                max_prod = max(max_prod, cum_prod, prod_from_neg)
            elif n < 0:
                prod_from_neg = n if cum_prod <= 0 else (prod_from_neg * n)
                cum_prod *= n
                max_prod = max(max_prod, cum_prod, prod_from_neg)
            else:
                max_prod = max(max_prod, n)
                cum_prod = 1
                prod_from_neg = 1

        return max_prod


solution = Solution()
p1 = solution.maxProduct([2,3,-2,4])
assert p1 == 6

p2 = solution.maxProduct([-2,0,-1])
assert p2 == 0

p3 = solution.maxProduct([2,3,-2,4, 0, 9, -2, -5, 3])
assert p3 == 270

p4 = solution.maxProduct([0, -2, -4, -1])
assert p4 == 8

p5 = solution.maxProduct([4, -2, 6, -5, 3, 0, -1, -2, -5, 0, -2, -9])
assert p5 == 720

p6 = solution.maxProduct([2,-5,-2,-4,3])
assert p6 == 24
