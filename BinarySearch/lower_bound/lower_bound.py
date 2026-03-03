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

def lower_bound(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid

        else:
            return mid

    return left


print(lower_bound([5,7,7,8,8,10], 6))
print(lower_bound([5,5,6,6,7,7,8,8,10], 5))
print(lower_bound([5,5,6,6,7,7,8,8,10], 7) - 1)
print(lower_bound([5,5,6,6,7,7,8,8,10], 6))