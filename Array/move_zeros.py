"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 10e4
-2e31 <= nums[i] <= 2e31 - 1
"""


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero_idx = None
        n = len(nums)
        for i in range(n):
            if nums[i] == 0 and first_zero_idx is None:
                first_zero_idx = i

            elif nums[i] != 0 and first_zero_idx is not None:
                nums[first_zero_idx] = nums[i]
                nums[i] = 0
                first_zero_idx += 1


s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
print(nums)

nums = [0]
s.moveZeroes(nums)
print(nums)

nums = [1,1,2,3,12]
s.moveZeroes(nums)
print(nums)

nums = [1,0,0,3,12]
s.moveZeroes(nums)
print(nums)
