"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""

class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
            else:
                first, last = low, min(high, len(nums) - 1)
                while nums[first] != target:
                    first += 1
                while nums[last] != target:
                    last -= 1
                return [first, last]

        return [-1, -1]


s = Solution()
assert s.searchRange([5,7,7,8,8,10], 8) == [3, 4]
assert s.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
