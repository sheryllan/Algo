"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.


Constraints:

1 <= nums.length <= 10e5
1 <= nums[i], k <= 10e9
"""



from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0

        counter = defaultdict(int)
        n = len(nums)
        cnt = 0
        ans = 0

        while i <= j <= n:
            while cnt < k and j < n:
                cnt += counter[nums[j]]
                counter[nums[j]] += 1
                j += 1

            if cnt < k and (i == 0 or j == n):
                break

            ans += n - j + 1
            cnt -= (counter[nums[i]] - 1)
            counter[nums[i]] -= 1
            i += 1

        return ans


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0

        counter = defaultdict(int)
        n = len(nums)
        cnt = 0
        ans = 0

        for j in range(n):
            cnt += counter[nums[j]]
            counter[nums[j]] += 1

            while cnt >= k:
                ans += n - j
                cnt -= (counter[nums[i]] - 1)
                counter[nums[i]] -= 1
                i += 1

        return ans


s = Solution()
assert s.countGood([3,1,4,3,2,2,4], 2) == 4
assert s.countGood([1,1,1,1,1], 10) == 1