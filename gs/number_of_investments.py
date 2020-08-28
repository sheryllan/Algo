"""
https://leetcode.com/discuss/interview-question/365452/goldman-sachs-oa-2020-shares-purchase

similar to https://leetcode.com/problems/subarrays-with-k-different-integers/
"""

def analyzeInvestments(s: str):
    n = len(s)
    companies = {'A', 'B', 'C'}
    last_at = {}
    count = 0
    j = 0
    for i, char in enumerate(s[:-2]):
        while len(last_at) < 3 and j < n:
            if s[j] in companies:
                last_at[s[j]] = j
            j += 1

        if len(last_at) == 3 and j <= n:
            count += n - j + 1

        if char in last_at and last_at[char] == i:
            last_at.pop(char)

    return count



num = analyzeInvestments('ABC')
assert num == 1

num = analyzeInvestments('ABCCBA')
assert num == 7

num = analyzeInvestments('ABBCZBAC')
assert num == 13

num = analyzeInvestments('PQACBA')
assert num == 7
