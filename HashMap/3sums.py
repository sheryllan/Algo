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

from collections import Counter


def three_sums(nums: [int], target: int) -> [[int]]:
    counter = Counter(nums)
    nums_unique = list(counter.keys())
    n = len(nums_unique)
    ans = []

    for i in range(n):
        a = nums_unique[i]
        if counter[a] >= 3 and 3 * a == target:
            ans.append([a] * 3)

        added = {a}
        for j in range(i + 1, n):
            b = nums_unique[j]
            c = target - a - b
            added.add(b)

            if c not in counter:
                continue

            if c == a and counter[a] >= 2:
                ans.append([a, a, b])
            elif c == b and counter[b] >= 2:
                ans.append([a, b, b])
            elif c not in added:
                ans.append([a, b, c])

        counter.pop(a)  # the combination of a has been traverse through so need to be removed

    return ans


print(three_sums([-2,0,1,1,2], 0))
print(three_sums([1,2,-2,-1], 0))
print(three_sums([-1, 0, 1, 2, -1, -4], 0))
print(three_sums([-1, 0, 0, 0, 1, 2, -3, 2, -1], 0))
print(three_sums([0, 0, 2], 0))
