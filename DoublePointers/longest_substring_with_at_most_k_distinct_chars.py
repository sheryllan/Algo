"""
Given a string you need to print longest possible substring that has exactly k unique characters.
If there is more than one substring of the longest possible length, then print any one of them.

Note:- Source(Google Interview Question).

Examples:

Input: Str = “aabbcc”, k = 1
Output: 2
Explanation: Max substring can be any one from [“aa” , “bb” , “cc”].


Input: Str = “aabbcc”, k = 2
Output: 4
Explanation: Max substring can be any one from [“aabb” , “bbcc”].


Input: Str = “aabbcc”, k = 3
Output: 6
Explanation: There are substrings with exactly 3 unique characters
                        [“aabbcc” , “abbcc” , “aabbc” , “abbc” ]
                        Max is “aabbcc” with length 6.


Input: Str = “aaabbb”, k = 3
Output: -1
Explanation: There are only two unique characters, thus show error message.

"""

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    start, end = 0, 0
    ans = -1
    char_index = {}
    while start <= end < len(s):
        char = s[end]
        if char not in char_index and len(char_index) == k:
            ans = max(ans, end - start)
            start_char = s[start]
            while char_index[start_char] > start:
                start += 1
                start_char = s[start]
            char_index.pop(start_char)
            start += 1

        char_index[char] = end
        end += 1

    ans = max(ans, end - start) if len(char_index) == k else ans
    return ans


assert lengthOfLongestSubstringKDistinct('aabbcc', 2) == 4
assert lengthOfLongestSubstringKDistinct('aabbccc', 1) == 3
assert lengthOfLongestSubstringKDistinct('aabbcc', 3) == 6
assert lengthOfLongestSubstringKDistinct('aaba', 3) == -1
assert lengthOfLongestSubstringKDistinct('jiewekjkwe', 4) == 8
assert lengthOfLongestSubstringKDistinct('jiewekijlkwe', 4) == 6
assert lengthOfLongestSubstringKDistinct("aabacbebebe", 3) == 7




