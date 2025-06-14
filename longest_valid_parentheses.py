'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack_open = []
        stack_close = []
        n = len(s)
        ans = 0
        for i in range(n):
            if (not stack_open) and s[i] == ')':
                continue

            if s[i] == '(':
                stack_open.append(i)
            else:
                j = stack_open.pop()
                length = i - j + 1
                while stack_close and stack_close[-1][0] >= j:
                    stack_close.pop()
                if stack_close and stack_close[-1][0] + 1 == j:
                    _, last_length = stack_close.pop()
                    length += last_length

                stack_close.append((i, length))
                ans = max(ans, length)

        return ans

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        n = len(s)
        len_prev = 0
        length = 0
        ans = 0
        for i in range(n):
            if (not stack) and s[i] == ')':
                len_prev = length = 0
                continue

            if s[i] == '(':
                len_prev = length
                stack.append(i)
            else:
                j = stack.pop()
                length = i - j + 1
                length += len_prev
                ans = max(ans, length)

        return ans

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len


solution = Solution()
print(solution.longestValidParentheses("()(())"))
print(solution.longestValidParentheses("(()"))
print(solution.longestValidParentheses(")()())"))
print(solution.longestValidParentheses(""))
print(solution.longestValidParentheses('(())())((())()()'))


def reverse_string(s: str):
    words = s.split()
    return ' '.join(words[::-1])

print(reverse_string('i am a python developer'))
