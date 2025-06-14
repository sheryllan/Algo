"""
Given an array nums of n integers, return an array of all the UNIQUE quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-10e+9 <= nums[i] <= 10e+9
-10e+9 <= target <= 10e+9
"""

from typing import List
from collections import defaultdict


def merge_sort(list1, list2):
    i, j = 0, 0
    list_merge = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            list_merge.append(list1[i])
            i += 1
        else:
            list_merge.append(list2[j])
            j += 1

    while i < len(list1):
        list_merge.append(list1[i])
        i += 1
    while j < len(list2):
        list_merge.append(list2[j])
        j += 1
    return list_merge


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    sums_of_2 = defaultdict(lambda: defaultdict(set))
    N = len(nums)
    for a in range(N):
        for b in range(a + 1, N):
            idx_pair = (a, b) if nums[a] <= nums[b] else (b, a)
            sums_of_2[nums[a] + nums[b]][(nums[idx_pair[0]], nums[idx_pair[1]])].add(idx_pair)

    ans = []
    quadruplets = set()
    for sum2 in sums_of_2:
        sum2_other = target - sum2
        if sum2_other not in sums_of_2:
            continue

        for num_pair, indices in sums_of_2[sum2].items():
            for num_pair_other, indices_other in sums_of_2[sum2_other].items():
                if not any(a != c and a != d and b != c and b != d for a, b in indices for c, d in indices_other):
                    continue

                merged = merge_sort(num_pair, num_pair_other)
                quadruplet = tuple(merged)
                if quadruplet not in quadruplets:
                    quadruplets.add(quadruplet)
                    ans.append(merged)

        sums_of_2[sum2] = {}
        sums_of_2[sum2_other] = {}

    return ans


"""复杂度分析

时间复杂度：O(n^3)，其中 n 为 nums 的长度。排序 O(nlogn)。两重循环枚举第一个数和第二个数，然后 O(n) 双指针枚举第三个数和第四个数。所以总的时间复杂度为 O(n^3)。
空间复杂度：O(1)。忽略返回值和排序的栈开销，仅用到若干变量。

作者：灵茶山艾府
链接：https://leetcode.cn/problems/4sum/solutions/2344514/ji-zhi-you-hua-ji-yu-san-shu-zhi-he-de-z-1f0b/
"""


def fourSum_standard(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    ans = []
    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        if sum(nums[a: a + 4]) > target:
            break
        if nums[a] + sum(nums[-3:]) < target:
            continue

        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue

            if nums[a] + nums[b] + sum(nums[b + 1: b + 3]) > target:
                break
            if nums[a] + nums[b] + sum(nums[-2:]) < target:
                continue

            c = b + 1
            d = n - 1
            while c < d:
                s = nums[a] + nums[b] + nums[c] + nums[d]
                if s > target:
                    d -= 1
                elif s < target:
                    c += 1
                else:
                    ans.append([nums[a], nums[b], nums[c], nums[d]])

                    c += 1
                    while nums[c] == nums[c - 1] and c < d:  # skip repeating numbers
                        c += 1

                    d -= 1
                    while nums[d] == nums[d + 1] and c < d:  # skip repeating numbers
                        d -= 1

    return ans


nums = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
print(fourSum(nums, target))
print(fourSum_standard(nums, target))
print()
"""[[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]"""

nums = [-5, 5, 4, -3, 0, 0, 4, -2]
target = 4
print(fourSum(nums, target))
print(fourSum_standard(nums, target))
print()
""""[[-5, 0, 4, 5], [-3, -2, 4, 5]]"""

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
print(fourSum_standard(nums, target))
print()

nums = [2, 2, 2, 2, 2]
target = 8
print(fourSum(nums, target))
print(fourSum_standard(nums, target))
print()

nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
target = 8
print(fourSum(nums, target))
print(fourSum_standard(nums, target))
print()
