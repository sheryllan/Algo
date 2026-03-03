

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = []
        row = 0
        i = 0
        while i < len(s):
            if row == 0:
                col = list(s[i:i+numRows])
                col_len = len(col)
                if col_len < numRows:
                    col += [''] * (numRows-col_len)
                grid.append(col)
                row = max(0, numRows - 2)
                i += numRows
            else:
                col = [''] * numRows
                col[row] = s[i]
                grid.append(col)
                row -= 1
                i += 1

        return ''.join(''.join(x) for x in zip(*grid))

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k = numRows + max(numRows - 2, 0)

        result = ''
        n = len(s)
        last_row = numRows - 1
        for i in range(numRows):
            for j in range(i, n, k):
                result += s[j]
                multiple = j // k
                extra_i = j + 2 * (last_row + multiple * k - j)
                if 0 < i < numRows - 1 and extra_i < n:
                    result += s[extra_i]

        return result

    def convert2(self, s: str, numRows: int) -> str:
        k = numRows + max(numRows - 2, 0)

        result = ''
        n = len(s)
        for i in range(numRows):
            extra_i = 2 * numRows - 2 - i
            for j in range(i, n, k):
                result += s[j]
                if 0 < i < numRows - 1 and extra_i < n:
                    result += s[extra_i]
                    extra_i += k

        return result



solution = Solution()
s = "PAYPALISHIRING"
n = 3
assert solution.convert(s, n) == 'PAHNAPLSIIGYIR'

assert solution.convert('A', 1) == 'A'
assert solution.convert('A', 2) == 'A'
assert solution.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'