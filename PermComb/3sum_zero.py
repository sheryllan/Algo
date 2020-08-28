"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
Runtime: 676 ms, faster than 95.78% of Python3 online submissions for 3Sum.
Memory Usage: 17.5 MB, less than 27.86% of Python3 online submissions for 3Sum.
"""
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        num_indexes = {}
        pos, neg = [], []
        for i, x in enumerate(nums):
            if x not in num_indexes:
                num_indexes[x] = []
                if x >= 0:
                    pos.append(x)
                if x <=0:
                    neg.append(x)
            if len(num_indexes[x]) < 3:
                num_indexes[x].append(i)

        seen = set()
        for a in pos:
            for b in neg:
                if len(num_indexes[a]) - 1 < int(a == b):
                    continue
                c = - (a + b)
                if c in num_indexes:
                    if len(num_indexes[c]) - 1 < int(c == a) + int(c == b):
                        continue
                    triplet = tuple(sorted((a, b, c)))
                    if triplet not in seen:
                        seen.add(triplet)

        return seen


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([-1,0, 0, 0, 1, 2, -3, 2, -1]))
print(s.threeSum([0, 0, 2]))
