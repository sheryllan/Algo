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


# PASS, non DP solution
class Solution:
    def maxProduct(self, nums: [int]) -> int:
        max_prod = float('-inf')
        cum_prod = 0
        first_neg_prod = 1
        last_neg_prod = 1
        prod_cnt = 0

        for i, num in enumerate(nums):
            if num:
                cum_prod = (cum_prod * num) if cum_prod else num
                prod_cnt += 1

                if first_neg_prod > 0:
                    first_neg_prod *= num

                last_neg_prod = num if num < 0 else (last_neg_prod * num)
            else:
                if cum_prod < 0 and prod_cnt > 1:
                    cum_prod = max(cum_prod / first_neg_prod, cum_prod / last_neg_prod)

                max_prod = max(cum_prod, max_prod, 0)
                first_neg_prod, last_neg_prod = 1, 1
                cum_prod, prod_cnt = 0, 0

        if cum_prod < 0 and prod_cnt > 1:
            cum_prod = max(cum_prod / first_neg_prod, cum_prod / last_neg_prod)

        return int(max(cum_prod, max_prod))



# solution = Solution()
# p1 = solution.maxProduct([2, -3, 0, -2, 4])
# assert p1 == 4
# p1 = solution.maxProduct([-3, -1, -1])
# assert p1 == 3
#
# p2 = solution.maxProduct([-2,0,-1])
# assert p2 == 0
#
# p3 = solution.maxProduct([2,3,-2,4, 0, 9, -2, -5, 3])
# assert p3 == 270
#
# p4 = solution.maxProduct([0, -2, -4, -1])
# assert p4 == 8
#
# p5 = solution.maxProduct([4, -2, 6, -5, 3, 0, -1, -2, -5, 0, -2, -9])
# assert p5 == 720
#
# p6 = solution.maxProduct([2,-5,-2,-4,3])
# assert p6 == 24
#
# p7 = solution.maxProduct([2, 5, 2, 1, 3])
# assert p7 == 60
#
# p8 = solution.maxProduct([-15])
# assert p8 == -15


# DP solution
class Solution:
    def maxProduct(self, nums: [int]) -> int:


        if not nums: return 0

        f = [0] * len(nums) # max prod of subarray joinable with the next
        g = [0] * len(nums) # min prod of subarray joinable with the next
        res = float('-inf') # historical max prod is saved here

        for i in range(len(nums)):
            if i == 0:
                f[i] = nums[i]
                g[i] = nums[i]
                res = max(res, f[i])
                continue

            if nums[i] > 0:
                f[i] = max(nums[i] * f[i-1], nums[i]) # nums[i] > 0, then times the largest, or sets to itself
            else:
                f[i] = max(nums[i] * g[i-1], nums[i]) # nums[i] <= 0, times the smallest, or sets to itself

            res = max(res, f[i])

            if nums[i] > 0:
                g[i] = min(nums[i] * g[i-1], nums[i]) # opposite to f[i]
            else:
                g[i] = min(nums[i] * f[i-1], nums[i])

        return res


solution = Solution()
p1 = solution.maxProduct([2, -3, 0, -2, 4])
assert p1 == 4
p1 = solution.maxProduct([-3, -1, -1])
assert p1 == 3

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

p7 = solution.maxProduct([2, 5, 2, 1, 3])
assert p7 == 60

p8 = solution.maxProduct([-15])
assert p8 == -15
