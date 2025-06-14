"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 1e4
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        char_index = {}
        ans = 0
        while start <= end < len(s):
            char = s[end]
            if char in char_index:
                idx = char_index[char]
                if idx >= start:
                    ans = max(ans, end - start)
                    start = idx + 1

            char_index[char] = end
            end += 1
        return max(ans, end - start)


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("abbjlacjlke"))
print(solution.lengthOfLongestSubstring("abba"))
print(solution.lengthOfLongestSubstring(""))