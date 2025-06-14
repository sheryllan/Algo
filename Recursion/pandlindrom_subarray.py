
def is_palindrome(s, start, end):
    sub_s = s[start: end]
    i = 0
    j = len(sub_s) - 1
    while i < j:
        if sub_s[i] != sub_s[j]:
            return False
        i += 1
        j -= 1

    return True  # empty string returns True


def find_palindrome_subarrays(s: str):
    n = len(s)
    ans = []
    sub_indices = [0]
    def split(i: int):
        if i == n:
            if is_palindrome(s, sub_indices[-1], n):
                sub_strings = []
                start = 0
                for end in sub_indices[1:]:
                    sub_strings.append(s[start: end])
                    start = end
                sub_strings.append(s[start:])
                ans.append(sub_strings)
            return

        if is_palindrome(s, sub_indices[-1], i):
            sub_indices.append(i)
            split(i + 1)
            sub_indices.pop()

        split(i + 1)

    split(1)
    return ans

def find_palindrome_subarrays2(s: str):
    n = len(s)
    ans = []
    sub_indices = [0]

    def split(i: int):
        if i == n:  # evaluation of palindrome not needed here because if the last substring wouldn't reach n if it is not palindrome
            sub_strings = []
            start = 0
            for end in sub_indices[1:]:
                sub_strings.append(s[start: end])
                start = end
            sub_strings.append(s[start:])
            ans.append(sub_strings)
            return

        for j in range(i, n + 1):
            if is_palindrome(s, sub_indices[-1], j):  # add only palindrome indices
                if j < n:
                    sub_indices.append(j)
                    split(j + 1)
                    sub_indices.pop()
                else:
                    split(j)

    split(1)
    return ans

    # n = len(s)
    # ans = []
    # sub_indices = []
    #
    # def split(i: int):
    #     if i == n:
    #         sub_strings = []
    #         start = 0
    #         for end in sub_indices:
    #             sub_strings.append(s[start: end])
    #             start = end
    #         ans.append(sub_strings)
    #         return
    #
    #     for j in range(i, n):
    #         if is_palindrome(s, i, j + 1):
    #             sub_indices.append(j + 1)
    #             split(j + 1)
    #             sub_indices.pop()
    #
    # split(0)
    # return ans

    # ans = []
    # path = []
    # n = len(s)
    #
    # def dfs(i):
    #     if i == n:
    #         ans.append(path.copy())
    #         return
    #
    #     for j in range(i, n):
    #         t = s[i:j+1]
    #         if t == t[::-1]:
    #             path.append(t)
    #             dfs(j + 1)
    #             path.pop()
    #
    # dfs(0)
    # return ans


print(find_palindrome_subarrays('aaabb'))
print(find_palindrome_subarrays2('aaabb'))
print(find_palindrome_subarrays('aab'))
print(find_palindrome_subarrays2('aab'))
print(find_palindrome_subarrays('abcdcb'))
print(find_palindrome_subarrays2('abcdcb'))
print(find_palindrome_subarrays('abadc'))
print(find_palindrome_subarrays2('abadc'))
