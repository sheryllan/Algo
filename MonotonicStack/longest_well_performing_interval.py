"""
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.



Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
Example 2:

Input: hours = [6,6,6]
Output: 0


Constraints:

1 <= hours.length <= 104
0 <= hours[i] <= 16
"""


from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        running_well_performing_sum = 0
        hour_sums = [0]
        for h in hours:
            running_well_performing_sum += 1 if h > 8 else -1
            hour_sums.append(running_well_performing_sum)
        if hour_sums[-1] > 0:
            return len(hours)

        stack = []
        for i, hs in enumerate(hour_sums):
            if (not stack) or hs < hour_sums[stack[-1]]:
                stack.append(i)

        longest_interval = 0
        for j in range(len(hour_sums) - 1, -1, -1):
            right = hour_sums[j]
            while stack and right > hour_sums[stack[-1]]:
                i = stack.pop()
                longest_interval = max(longest_interval, j - i)

        return longest_interval


s = Solution()
print(s.longestWPI([6,6,9]))
print(s.longestWPI([9,9,6,0,6,6,9]))


"""
虽说方法一更加通用，不过利用 nums 中只有 1 和 −1 的特点，可以做到一次遍历。

考虑 s[i]：

如果 s[i]>0，那么 j=0 就是最远的左端点，因为 s[0]=0，故 s[i]−s[0]=s[i]>0，符合要求。
如果 s[i]≤0，那么 j 就是 s[i]−1 首次出现的位置。为什么是 s[i]−1 而不是其它更小的数？这是因为前缀和是从 0 开始的，由于 nums 中只有 1 和 −1，
那么相邻前缀和的差都恰好为 1，要想算出比 s[i]−1 更小的数，必然会先算出 s[i]−1，那么这些更小数必然在 s[i]−1 首次出现的位置的右边。

链接：https://leetcode.cn/problems/longest-well-performing-interval/solutions/2110211/liang-chong-zuo-fa-liang-zhang-tu-miao-d-hysl/

"""
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = s = 0
        pos = {}
        for i, x in enumerate(hours):
            s += 1 if x > 8 else -1
            if s > 0:
                ans = i + 1
            elif s - 1 in pos:
                ans = max(ans, i - pos[s - 1])
            if s not in pos:
                pos[s] = i
        return ans

    def longestWPI2(self, hours: List[int]) -> int:
        pos = [0] * (len(hours) + 1)
        s = 0
        ans = 0
        for i, h in enumerate(hours, 1):
            s += -1 if h > 8 else 1
            if s >= 0:
                if s + 1 <= len(hours) and pos[s + 1] > 0:
                    ans = max(ans, i - pos[s + 1])
                if pos[s] == 0:
                    pos[s] = i
            else:
                ans = i

        return ans

