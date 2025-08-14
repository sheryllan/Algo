"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 10e4
-1000 <= nums[i] <= 1000
-10e7 <= k <= 10e7
"""


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        s = 0
        cnt = 0
        for x in nums:
            s += x
            if s - k in prefix_sums:
                cnt += prefix_sums[s - k]

            prefix_sums[s] = prefix_sums.get(s, 0) + 1

        return cnt


s = Solution()
assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum([1,2,3], 3) == 2
assert s.subarraySum([1,2,3], 4) == 0
assert s.subarraySum([1,2,3,-1,1,-3], 3) == 4