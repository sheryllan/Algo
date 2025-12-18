"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 10e5
-10e4 <= nums[i] <= 10e4
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_seen = k
        nums_part = nums

        while k_seen > 0 and nums_part:
            smaller, larger = [], []
            pivot = len(nums_part) - 1
            k_pivot = 1
            for x in nums_part[:-1]:
                if x < nums_part[pivot]:
                    smaller.append(x)
                elif x == nums_part[pivot]:
                    k_pivot += 1
                else:
                    larger.append(x)

            if len(larger) > k_seen:
                nums_part = larger
            elif len(larger) == k_seen:
                return min(larger)
            elif len(larger) >= k_seen - k_pivot:
                return nums_part[pivot]
            else:
                k_seen -= (len(larger) + k_pivot)
                nums_part = smaller


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counter = {}
        for x in nums:
            counter[x] = counter.get(x, 0) + 1

        nums_unique = list(counter)

        i_klargest = len(nums) - k
        low, high = 0, len(nums_unique) - 1
        i_unique = 0
        i_pivot = -1
        while i_pivot < i_klargest:
            pivot = nums_unique[high]
            i = low
            for j in range(low, high):
                if nums_unique[j] < pivot:
                    nums_unique[i], nums_unique[j] = nums_unique[j], nums_unique[i]
                    i_pivot += counter[nums_unique[i]]
                    if i_pivot >= i_klargest:
                        return nums_unique[i]

                    i += 1

            nums_unique[i], nums_unique[high] = pivot, nums_unique[i]
            i_pivot += counter[nums_unique[i]]

            if i_pivot < i_klargest:
                low = i + 1
            i_unique = i

        return nums_unique[i_unique]


s = Solution()
# assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert s.findKthLargest([3,2,3,1,2,4,5,5,6], 9) == 1