"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

import unittest as ut


class Solution:
    def swap(self, items, i, j):
        x = items[i]
        items[i] = items[j]
        items[j] = x


    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def binary_search(x, nums_reversed):
            left, right = 0, len(nums_reversed)
            while left < right:
                mid = int((left + right) / 2)
                if mid == left:
                    break
                if x >= nums_reversed[mid]:
                    right = mid - 1
                else:
                    left = mid

            return right if right < len(nums_reversed) and x < nums_reversed[right] else left

        if not nums:
            return nums

        last, j = nums[-1], 0
        for i in range(len(nums) - 1, -1, -1):
            j = i
            if nums[i] < last:
                break
            last = nums[i]

        start = j + 1 if nums[j] < last else j
        next_gt_idx = j + binary_search(nums[j], nums[j:])
        self.swap(nums, j, next_gt_idx)

        for k in range(start, start + int((len(nums) - start) / 2)):
            self.swap(nums, k, start + len(nums) - 1 - k)



class Texts(ut.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_random_nums(self):
        nums = [1, 3, 3, 6, 6, 6, 4, 3, 2]

        expected = [1, 3, 4, 2, 3, 3, 6, 6, 6]
        self.solution.nextPermutation(nums)

        self.assertListEqual(nums, expected)

        nums = [1, 2, 3]
        expected = [1, 3, 2]
        self.solution.nextPermutation(nums)
        self.assertListEqual(nums, expected)


    def test_max_order(self):
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        self.solution.nextPermutation(nums)

        self.assertListEqual(nums, expected)




"""
Complexity Analysis

Time complexity : O(n). In worst case, only two scans of the whole array are needed.

Space complexity : O(1). No extra space is used. In place replacements are done.

"""



