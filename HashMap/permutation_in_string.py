"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""




"""
The key insight: instead of generating all permutations, two strings are permutations of each other if and 
only if they have the same character frequencies.
So the problem reduces to: does any window of size len(s1) in s2 have the same frequency map as s1?
"""


# Time complexity O(26 × m) = O(m), space complexity O(26) = O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = {}
        counter_s2 = {}

        for x in s1:
            counter_s1[x] = counter_s1.get(x, 0) + 1

        start = 0
        n = len(s1)
        for end in range(len(s2)):
            char = s2[end]
            counter_s2[char] = counter_s2.get(char, 0) + 1

            if end - start + 1 > n:
                prev = s2[start]
                counter_s2[prev] -= 1
                if counter_s2[prev] == 0:
                    counter_s2.pop(prev)
                start += 1

            if counter_s1 == counter_s2:
                return True

        return False


s = Solution()
assert s.checkInclusion("ab", "eidbaooo")
assert not s.checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine")



