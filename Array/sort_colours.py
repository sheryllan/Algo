
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

"""

from typing import List


class Solution:
    def swap(self, i, j, nums):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def sortColors(self, nums: List[int]) -> None:
        counters = [0] * 3
        for x in nums:
            counters[x] += 1

        counters[1] += counters[0]
        counters[2] += counters[1]
        idx = [0, counters[0], counters[1]]
        first = 0 if idx[1] > 0 else (1 if idx[2] > 0 else 2)
        for i in range(idx[2]):
            if i < counters[first]:
                while nums[i] != first:
                    x = nums[i]
                    self.swap(i, idx[x], nums)
                    idx[x] += 1
            else:
                while nums[i] != first + 1:
                    x = nums[i]
                    self.swap(i, idx[x], nums)
                    idx[x] += 1


"""
The idea behind the algorithm is to keep all the 0s before the low pointer, all the 2s after the high pointer, 
and all the 1s between the low and high pointers. 
The algorithm moves the mid pointer through the array, comparing the value at each position with 1. 

If the value is 0, the element is swapped with the element at the low pointer, and the low and mid pointers are incremented. 

If the value is 2, the element is swapped with the element at the high pointer, and the high pointer is decremented. 

If the value is 1, the mid pointer is simply incremented.

The algorithm terminates when the mid pointer crosses the high pointer, indicating that all the elements have been processed and the array is sorted."""

class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


s = Solution()

nums = [1, 0]
s.sortColors(nums)
print(nums)


nums = [2]
s.sortColors(nums)
print(nums)

nums = [1, 2, 1, 1, 2]
s.sortColors(nums)
print(nums)

nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)

nums = [2,0,1]
s.sortColors(nums)
print(nums)

nums = [1,1,1]
s.sortColors(nums)
print(nums)

nums = [0, 1, 0, 1, 1, 1, 0, 2, 2]
s.sortColors(nums)
print(nums)