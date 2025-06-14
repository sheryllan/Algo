
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 1e5
-1e9 <= nums[i] <= 1e9
nums is a non-decreasing array.
-1e9 <= target <= 1e9
"""
from typing import List


class Solution:
    def lower_bound(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the index that is target <= nums[i] and nums[j] <= target (equivalent to nums[j] > target - 1)
        lower = self.lower_bound(nums, target)
        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]
        upper = self.lower_bound(nums, target + 1) - 1
        return [lower, upper]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([2, 2], 3))
print(s.searchRange([], 0))


"""
问：如何理解 end = lowerBound(nums, target + 1) - 1 这段代码？

答：要想找到 ≤target 的最后一个数，无需单独再写一个二分。我们可以先找到这个数的右边相邻数字，也就是 >target 的第一个数。
在所有数都是整数的前提下，>target 等价于 ≥target+1，这样就可以复用我们已经写好的二分函数了，即 lowerBound(nums, target + 1)，
算出这个数的下标后，将其减一，就得到 ≤target 的最后一个数的下标。


问：如果 ≥target+1 的第一个数不存在怎么办？

答：在数组中有 target 的前提下，这意味着数组的最后一个数（下标 n−1）就是 target。同时，lowerBound(nums, target + 1) 在这种情况下会返回 n，
减一得到 n−1，这正是我们要计算的下标。


链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/1980196/er-fen-cha-zhao-zong-shi-xie-bu-dui-yi-g-t9l9/

"""