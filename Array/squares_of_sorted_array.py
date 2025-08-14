"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 10e4
-10e4 <= nums[i] <= 10e4
nums is sorted in non-decreasing order.

"""

from math import inf
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        squares = [x * x for x in nums]
        n = len(squares)

        min_sqrt = inf
        min_i = 0
        for i, x in enumerate(squares):
            if x <= min_sqrt:  # less than and EQUAL TO is important as the min_i must be the turning point
                min_sqrt = x
                min_i = i
            else:
                break

        ans = [squares[min_i]]
        left, right = min_i - 1, min_i + 1
        while left >= 0 and right < n:
            if squares[left] < squares[right]:
                ans.append(squares[left])
                left -= 1
            else:
                ans.append(squares[right])
                right += 1

        if left >= 0:
            ans.extend(squares[:left + 1][::-1])

        if right < n:
            ans.extend(squares[right:])

        return ans



"""
看示例 1，把 [−4,−1,0,3,10] 分成负数和非负数两部分：

负数：[−4,−1]，计算平方得 [16,1]，反过来看就是 [1,16]。
非负数：[0,3,10]，计算平方得 [0,9,100]。
仿照 88. 合并两个有序数组 的 思路，把上述两个有序数组合并，得到答案 [0,1,9,16,100]。

与其从中间开始向两边合并，不如从两边开始向中间合并，这样无需计算从中间的哪个位置开始。

具体算法如下：

初始化一个长为 n 的空数组 ans。
初始化左指针 i=0，右指针 j=n−1。初始化下标 p=n−1，表示要往 ans[p] 填入数据。
设 x=nums[i] 
2
 , y=nums[j] 
2
 。
如果 x>y，将 x 填入 ans[p]，把 i 加一，p 减一。
如果 x≤y，将 y 填入 ans[p]，把 j 减一，p 减一。
循环直到 p=−1，即所有数据都填入 ans。
返回 ans。
在上述过程中，由于我们总是把更大的数放在 ans 更靠右的位置，所以得到的答案是非递减的。

链接：https://leetcode.cn/problems/squares-of-a-sorted-array/solutions/2806253/xiang-xiang-shuang-zhi-zhen-cong-da-dao-blda6/
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j = 0, n - 1
        for p in range(n - 1, -1, -1):
            x = nums[i] * nums[i]
            y = nums[j] * nums[j]
            if x > y:  # 更大的数放右边
                ans[p] = x
                i += 1
            else:
                ans[p] = y
                j -= 1
        return ans


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i, j = 0, n - 1
        for p in range(n - 1, -1, -1):
            x, y = nums[i], nums[j]
            if -x > y:
                ans[p] = x * x
                i += 1
            else:
                ans[p] = y * y
                j -= 1
        return ans



s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))
print(s.sortedSquares([-5,-3,-2,-1]))
print(s.sortedSquares([-4,-4,-3]))
