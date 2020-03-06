"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '' if numerator == 0 or (numerator > 0) == (denominator >= 0) else '-'
        num, denom = abs(numerator), abs(denominator)

        quotient, remainder = divmod(num, denom)
        int_part = sign + str(quotient)

        fractions = []
        i = -1
        dividends = {0: None}
        while remainder not in dividends:
            i += 1
            dividends[remainder] = i
            quotient, remainder = divmod(remainder * 10, denom)
            fractions.append(str(quotient))

        fraction_part = ''.join(fractions[:dividends[remainder]])
        if dividends[remainder] is not None:
            fraction_part += '(' + ''.join(fractions[dividends[remainder]:]) + ')'

        return f'{int_part}.{fraction_part}' if fraction_part else int_part


solution = Solution()
assert solution.fractionToDecimal(1, 2) == '0.5'
assert solution.fractionToDecimal(2, 1) == '2'
assert solution.fractionToDecimal(-2, 3) == '-0.(6)'
assert solution.fractionToDecimal(1, 6) == '0.1(6)'

