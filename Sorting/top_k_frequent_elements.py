"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]



Constraints:

1 <= nums.length <= 10e5
-10e4 <= nums[i] <= 10e4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_sorted = list(sorted(counter.items(), key=lambda x: x[1]))

        n = len(counter_sorted)
        return [x for x, c in counter_sorted[n-k:]]



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums))]

        for num, cnt in counter.items():
            bucket[cnt - 1].append(num)

        print(bucket)

        ans = []
        for x in bucket[::-1]:
            if x:
                ans.extend(x)
            if len(ans) == k:
                return ans
