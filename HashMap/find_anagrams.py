"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 1e4
s and p consist of lowercase English letters.
"""
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        k = len(p)
        cnt_s = Counter(s[:k])
        cnt_p = Counter(p)

        for i in range(len(s) - k):
            if cnt_s == cnt_p:
                ans.append(i)

            cnt_s[s[i]] -= 1
            if cnt_s[s[i]] == 0:
                cnt_s.pop(s[i])
            cnt_s[s[i + k]] -= cnt_s.get(s[i + k], 0) + 1

        if cnt_s == cnt_p:
            ans.append(len(s) - k)
        return ans

print(Solution().findAnagrams("cbaebabacd", "abab"))