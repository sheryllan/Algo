"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.


Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        sub_sum = total_sum // 2
        dp = [False] * (sub_sum + 1)
        dp[0] = True

        for x in nums:
            for i in range(sub_sum, x - 1, -1):
                dp[i] = dp[i] or dp[i - x]

        return dp[sub_sum]


assert Solution().canPartition([1, 5, 11, 5]) == True
assert Solution().canPartition([1, 2, 3, 5]) == False



from functools import cache


class Solution2:

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        @cache
        def dfs(i, sub_sum):
            if i < 0 or sub_sum < 0:
                return False

            if sub_sum == 0:
                return True

            return dfs(i - 1, sub_sum) or dfs(i - 1, sub_sum - nums[i])

        n = len(nums)
        return dfs(n - 1, total_sum / 2)

