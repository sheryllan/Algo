"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        last_num = 0
        ways_1, ways_2 = 1, 1
        for x in s:
            num = int(x)
            if num == 0:
                if last_num < 1 or last_num > 2:
                    return 0
                ways_1 = ways_2
            else:
                ways = (ways_1 + ways_2) if 10 < 10 * last_num + num < 27 else ways_1
                ways_2 = ways_1
                ways_1 = ways

            last_num = num

        return ways_1


s = Solution()
assert s.numDecodings('10') == 1
assert s.numDecodings('17') == 2
assert s.numDecodings('110') == 1
assert s.numDecodings('12') == 2
assert s.numDecodings('67') == 1
assert s.numDecodings('30') == 0
assert s.numDecodings('2124') == 5



