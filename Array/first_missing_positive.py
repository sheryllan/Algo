"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 10e5
-2^31 <= nums[i] <= 2^31 - 1
"""


from typing import List


class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     # Place each positive integer i at index i-1 if possible
    #     for i in range(n):
    #         while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
    #             j = nums[i] - 1
    #             nums[i], nums[j] = nums[j], nums[i]
    #
    #     # Find the first missing positive integer
    #     for i in range(n):
    #         if nums[i] != i + 1:
    #             return i + 1
    #
    #     # If all positive integers from 1 to n are present, return n + 1
    #     return n + 1

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]

        After removing all the numbers greater than or equal to n, all the numbers remaining are smaller than n.
        If any number i appears, we add n to nums[i] which makes nums[i]>=n.
        Therefore, if nums[i]<n, it means i never appears in the array and we should return i.
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n] += n
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i
        return n


s = Solution()
assert s.firstMissingPositive([1,2,0]) == 3
assert s.firstMissingPositive([3,4,-1,1]) == 2
assert s.firstMissingPositive([7,8,9,11,12]) == 1
assert s.firstMissingPositive([-3,4,-1,1,2,5,0]) == 3
assert s.firstMissingPositive([1,1]) == 2
assert s.firstMissingPositive([1]) == 2
assert s.firstMissingPositive([2,1]) == 3




"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n-1): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n] += n
        for i in range(n):
            if nums[i] // n == 0:
                return i
        return n