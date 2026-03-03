"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 10e4
"""



class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = n
        divisor = 10
        a, b = 0, 1
        multiple = a
        # x = 10a + b
        # count how many multiple of 10 the factorial is
        while x > 0:
            # x * y = (10a + b)y = 10ay + by, where b < 10
            multiple *= x
            a, b = divmod(b * x, divisor)
            multiple += a
            x -= 1

        if b != 0:
            return 0

        zeros = 0
        rem = 0
        while multiple > 0 and rem == 0:
            multiple, rem = divmod(multiple, 10)
            zeros += 1

        return zeros



"""
Trailing zeroes in a number are created by factors of 10, which are the product of factors 2 and 5.
Since there are always more factors of 2 than 5 in ( n! ), the number of trailing zeroes is determined by the number of factors of 5.
To count the factors of 5, we divide ( n ) by powers of 5 and sum the results.
"""
class Solution:
    def trailingZeroes(self, n):
        if n <= 4:
            return 0
        count = 0
        i = 5
        while n // i > 0:
            count += n // i
            i *= 5
        return count