"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1


        start = 0
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end +1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        for i in range(n):
            # Odd length palindrome
            st = end = i
            while st >= 0 and end < n and s[st] == s[end]:
                st -= 1
                end += 1
            temp = s[st+1:end]
            if len(temp) > len(res):
                res = temp

            # Even length palindrome
            st, end = i, i+1
            while st >= 0 and end < n and s[st] == s[end]:
                st -= 1
                end += 1
            temp = s[st+1:end]
            if len(temp) > len(res):
                res = temp

        return res