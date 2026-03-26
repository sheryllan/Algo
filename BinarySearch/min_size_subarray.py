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

from bisect import bisect_right


# solution with O(nlog(n)) complexity
def min_sub_array_len2(target, nums):
    prefix_sums = [0] * len(nums)
    cum_sum = 0
    min_len = len(nums) + 1
    left = 0

    for i in range(len(nums)):
        cum_sum += nums[i]
        prefix_sums[i] = cum_sum

        if cum_sum > target:
            right = i
            target_sum = cum_sum - target

            # Compare against target_sum + 1;
            # one index left of first >= value corresponds to <= target_sum
            while left < right:
                mid = (left + right) // 2
                if prefix_sums[mid] < target_sum + 1:
                    left = mid + 1
                elif prefix_sums[mid] > target_sum + 1:
                    right = mid
                else:
                    left = mid
                    break

            min_len = min(min_len, i - left + 1)

        elif cum_sum == target:
            min_len = min(min_len, i + 1)

    return min_len % (len(nums) + 1)


def min_sub_array_len2_bisect(target, nums):
    n = len(nums)
    prefix = [0] * n
    running = 0
    left = 0
    ans = n + 1
    for i, x in enumerate(nums):
        running += x
        prefix[i] = running

        if running > target:
            # Need largest j < i with prefix[j] <= curr - target
            # bisect_right gives insertion point before which all a[lo:ip] <= (curr-target), i.e. higher bound
            j = bisect_right(prefix, running - target, left, i)
            ans = min(ans, i - j + 1)
        elif running == target:
            ans = min(ans, i + 1)

    return ans % (n + 1)


nums = [10,2,3]
target = 6
assert min_sub_array_len2_bisect(target, nums) == 1


nums = [1,2,3,4,5]
target = 11
assert min_sub_array_len2_bisect(target, nums) == 3


nums = [2, 3, 1, 2, 4, 3]
target = 7
assert min_sub_array_len2_bisect(target, nums) == 2


nums = [1, 4, 4]
target = 4
assert min_sub_array_len2_bisect(target, nums) == 1


nums = [1] * 8
target = 11
assert min_sub_array_len2_bisect(target, nums) == 0