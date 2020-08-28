"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:

    def binary_search_rotated(self, x: int, A: [int], offset: int = 0):
        if not A:
            return  -1

        low = offset
        high = offset + len(A) - 1

        while low != high:
            low_offset = (low - offset) % len(A)
            high_offset = (high - offset) % len(A)
            mid = ((low_offset + high_offset) // 2 + offset) % len(A)
            if x < A[mid]:
                high = mid
                low = low % len(A)
            elif x > A[mid]:
                low = (mid + 1) % len(A)
                high = high % len(A)
            else:
                return mid

        # final assertion because initial high set to the last index, A[last] might have not be evaluated yet
        return low if x == A[low] else -1



    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1

        prev = nums[0]
        i_first = 0
        for i, x in enumerate(nums):
            if x < prev:
                i_first = i
                break
            prev = x

        return self.binary_search_rotated(target, nums, i_first)


# s = Solution()
# assert s.search([4,5,6,7,0,1,2], 7) == 3
# assert s.search([4,5,6,7,0,1,2], 3) == -1
# assert s.search([4,5,6,7,0,1,2], 2) == 6
# assert s.search([1], 1) == 0


class Solution2:

    def binary_search(self, x: int, A: [int], low=0, high=None):
        if not A:
            return -1

        high = len(A) if high is None else high
        assert 0 <= high <= len(A), f'index high out of range: {high}'
        assert 0 <= low <= high, f'index low out of range: {low}'

        while low < high:
            mid = (low + high) // 2
            if x < A[mid]:
                high = mid
            elif x > A[mid]:
                low = mid + 1
            else:
                return mid

        return -1


    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1

        prev = nums[0]
        i_first = 0
        for i, x in enumerate(nums):
            if x < prev:
                i_first = i
                break
            prev = x

        return self.binary_search(target, nums, high=i_first) if target > nums[-1] \
            else self.binary_search(target, nums, low=i_first)



s = Solution2()
assert s.search([4,5,6,7,0,1,2], 7) == 3
assert s.search([4,5,6,7,0,1,2], 3) == -1
assert s.search([4,5,6,7,0,1,2], 2) == 6
assert s.search([1], 1) == 0
assert s.search([1, 2, 3, 4], 5) == -1
assert s.search([1, 2, 4, 6], 6) == 3
