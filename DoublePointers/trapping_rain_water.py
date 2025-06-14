"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

https://leetcode.cn/problems/trapping-rain-water/description/
"""


from typing import List

# Best solution using double pointers
"""
动态规划的做法中，需要维护两个数组 leftMax(prefixMax) 和 rightMax(suffixMax)，因此空间复杂度是 O(n)。是否可以将空间复杂度降到 O(1)？

注意到下标 i 处能接的雨水量由 leftMax[i] 和 rightMax[i] 中的最小值决定。由于数组 leftMax 是从左往右计算，数组 rightMax 是从右往左计算，因此可以使用双指针和两个变量代替两个数组。

维护两个指针 left 和 right，以及两个变量 leftMax 和 rightMax，初始时 left=0,right=n−1,leftMax=0,rightMax=0。指针 left 只会向右移动，指针 right 只会向左移动，在移动指针的过程中维护两个变量 leftMax 和 rightMax 的值。

当两个指针没有相遇时，进行如下操作：

使用 height[left] 和 height[right] 的值更新 leftMax 和 rightMax 的值；

如果 height[left]<height[right]，则必有 leftMax<rightMax，下标 left 处能接的雨水量等于 leftMax−height[left]，将下标 left 处能接的雨水量加到能接的雨水总量，然后将 left 加 1（即向右移动一位）；

如果 height[left]≥height[right]，则必有 leftMax≥rightMax，下标 right 处能接的雨水量等于 rightMax−height[right]，将下标 right 处能接的雨水量加到能接的雨水总量，然后将 right 减 1（即向左移动一位）。

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans



def calc_volume(heights: list):
    if len(heights) <= 1:
        return 0

    volume = 0
    prev_height = heights[0]
    downward_heights = []
    for i, h in enumerate(heights):
        if h < prev_height:
            if not downward_heights:
                downward_heights.append((i - 1, prev_height))
            downward_heights.append((i, h))
        elif h > prev_height and downward_heights:
            j, base_h = downward_heights.pop()
            k, left_h = downward_heights.pop()
            while left_h <= h:
                volume += (i - j) * (left_h - base_h)
                if not downward_heights:
                    break
                j, base_h = k, left_h
                k, left_h = downward_heights.pop()

            if left_h > h:
                volume += (i - j) * (h - base_h)
                downward_heights.append((k, left_h))
                downward_heights.append((j, h))  # new base from the current height

        prev_height = h

    return volume


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(calc_volume(heights))

heights = [4, 2, 0, 3, 2, 5]
print(calc_volume(heights))



# a simplified version
"""复杂度分析

时间复杂度：O(n)，其中 n 是数组 height 的长度。从 0 到 n−1 的每个下标最多只会入栈和出栈各一次。

空间复杂度：O(n)，其中 n 是数组 height 的长度。空间复杂度主要取决于栈空间，栈的大小不会超过 n。

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:  # handle if new height is higher, otherwise just append it to the stack
                top = stack.pop()
                if not stack:  # monotonically increasing height, maintain only 1 item - the new height in the stack
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]  # the base is always the last height
                ans += currWidth * currHeight
            stack.append(i)

        return ans




