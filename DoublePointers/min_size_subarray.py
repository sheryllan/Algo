"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 10e9
1 <= nums.length <= 10e5
1 <= nums[i] <= 10e4

"""


def get_subarray_size(nums: list, target):
    if not nums:
        return 0

    i = 0
    n = len(nums)
    j = i
    min_size = float('inf')
    sub_sum = 0
    while i < n:
        while j < n and sub_sum < target:
            sub_sum += nums[j]
            j += 1

        if sub_sum >= target:
            min_size = min(min_size, j - i)

        if min_size == 1:
            return 1

        sub_sum -= nums[i]
        i += 1

    return 0 if min_size == float('inf') else min_size


nums = [10,2,3]
target = 6
print(get_subarray_size(nums, target))


nums = [1,2,3,4,5]
target = 11
print(get_subarray_size(nums, target))


nums = [2, 3, 1, 2, 4, 3]
target = 7
print(get_subarray_size(nums, target))


nums = [1, 4, 4]
target = 4
print(get_subarray_size(nums, target))


nums = [1] * 8
target = 11
print(get_subarray_size(nums, target))




