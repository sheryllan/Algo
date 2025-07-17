"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""


class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) < 2:
            return s

        stack = []
        start = 0

        for i, curr in enumerate(s[1:], 1):
            last = s[i - 1]
            if last.isdigit() and curr == '[':  # digit can only be followed by [
                stack.append(int(s[start:i]))
                start = i + 1  # string start
            elif not last.isdigit() and curr.isdigit():
                if last not in ('[', ']'):
                    stack.append(s[start:i])
                start = i  # number start
            elif curr == ']':
                decoded_str = s[start:i]
                if not stack:
                    stack.append(decoded_str)

                value = stack.pop()
                while not isinstance(value, int):
                    decoded_str = value + decoded_str
                    value = stack.pop()

                decoded_str *= value
                stack.append(decoded_str)

                start = i + 1

        return ''.join(stack) + s[start:]


s = Solution()
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(s.decodeString("3[a2[c]]kb5[l]"))
print(s.decodeString("3[a]2[bc]"))
assert s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == 'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
print(s.decodeString("t"))



class Solution2:
    def decodeString(self, s: str) -> str:
        cnt = []
        stack = []
        currInt, currStr = 0, ''
        for char in s:
            if char.isdigit():
                currInt = currInt * 10 + int(char)
            elif char == '[':
                cnt.append(currInt)
                stack.append(currStr)
                currInt = 0
                currStr = ''
            elif char == ']':
                repeat = cnt.pop()
                prev = stack.pop()
                currStr = prev + currStr * repeat
            else:
                currStr += char
        return currStr