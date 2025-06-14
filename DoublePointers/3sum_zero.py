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
                if x <= 0:
                    neg.append(x)
            if len(num_indexes[x]) < 3:
                num_indexes[x].append(i)

        seen = set()
        for a in pos:
            for b in neg:
                if len(num_indexes[a]) - 1 < int(a == b):  # if a == b == 0 and len(num_indexes[a]) == 1
                    continue
                c = - (a + b)
                if c in num_indexes:
                    if len(num_indexes[c]) - 1 < int(c == a) + int(c == b):  # if a == b == c and len(num_indexes[c]) == 2
                        continue
                    triplet = tuple(sorted((a, b, c)))
                    if triplet not in seen:
                        seen.add(triplet)

        return seen


s = Solution()
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# print(s.threeSum([-1, 0, 0, 0, 1, 2, -3, 2, -1]))
# print(s.threeSum([0, 0, 2]))


def three_sums(nums: [int], target: int) -> [[int]]:
    nums.sort()
    n = len(nums)
    ans = []
    for a in range(n - 2):
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        if sum(nums[a: a + 3]) > target:
            break

        if nums[a] + sum(nums[-2:]) < target:
            continue

        b = a + 1
        c = n - 1
        while b < c < n:
            sm = nums[a] + nums[b] + nums[c]
            if sm < target:
                b += 1
            elif sm > target:
                c -= 1
            else:
                ans.append([nums[a], nums[b], nums[c]])
                b += 1
                c -= 1

                while b < c and nums[b] == nums[b - 1]:
                    b += 1
                while b < c and nums[c] == nums[c + 1]:
                    c -= 1

    return ans


print(three_sums([1, 2, -2, -1], 0))
print(three_sums([-1, 0, 1, 2, -1, -4], 0))
print(three_sums([-1, 0, 0, 0, 1, 2, -3, 2, -1], 0))
print(three_sums([0, 0, 2], 0))



