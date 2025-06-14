"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-10e4 <= nums[i] <= 10e4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10e4 <= target <= 10e4
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_on_target_right(i):
            end = nums[-1]
            if target > end:
                return nums[i] >= target or nums[i] <= end
            else:
                return target <= nums[i] <= end

        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if is_on_target_right(mid):
                right = mid
            else:
                left = mid + 1

        return -1 if left == len(nums) or nums[left] != target else left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool:
            x = nums[i]
            if x > nums[-1]:
                return target > nums[-1] and x >= target
            return target > nums[-1] or x >= target

        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1


# 链接：https://leetcode.cn/problems/search-in-rotated-sorted-array/solutions/1987503/by-endlesscheng-auuh/

s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(s.search([1], 0))  # -1
