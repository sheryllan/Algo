


def find_first(s: str):
    counter = {}
    first = 0
    for i, char in enumerate(s):
        if char in counter:
            counter[char] += 1
            if char == s[first]:
                while first <= i and counter[s[first]] > 1:
                    first += 1
        else:
            counter[char] = 1

    return s[first] if first < len(s) else None


assert find_first("abacccad") == 'b'
assert find_first("aaacbbbc") is None
assert find_first("cdaed") == 'c'
assert find_first("ceeeacb") == 'a'



class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1