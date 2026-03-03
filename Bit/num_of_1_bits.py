"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).



Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.



Constraints:

1 <= n <= 2^31 - 1
"""


"""
If we have number n, then n&(n-1) will remove the rightmost 1 in binary representation of n. 
For example if n = 10110100, then n & (n-1) = 10110100 & 10110011 = 10110000 
Repeat this operation until we have n = 0 and count number of steps.

Complexity It is O(1), because we need to make no more than 32 operations here, but it is quite vague: 
all methods will be O(1), why this one is better than others? 
In fact it has complexity O(m), where m is number of 1-bits in our number. 
In average it will be 16 bits, so it is more like 16 operations, not 32 here, which gives us 2-times gain. 
Space complexity is O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)
            ans += 1

        return ans



"""
You can stop on previous solution and interviewer will be OK with that. But if you show him the following solution, he will be really happy. Let us understand what is going on in the following code.

First of all 0x55555555 = 01010101010101010101010101010101 in binary representation, so first step will deal with even and odd bits. 
What happens after first line of code computed: it will count number of non-zero bits in each pair. 
For simplicity imagine just first 8 bits with constant 0x55 = 01010101 and choose n = 11000110, then we have is 10 00 01 01. 
Why? We have 2, that is 10 ones in first pair, than we have 0 ones, than we have 1 one and finally we also have 1.

Now, to the second step, we have 0x33333333 = 110011001100110011001100110011. 
Again let us look at only first 8 bit, that is to 11001100. What will happend after this step, number of non-zero bits in groups of 4 will be computed. 
We stopped on number 10 00 01 01, now we have 0010 0010, because there is 2 + 0 ones in first group and 1+1 ones in second group.

Next step is 0x0f0f0f0f = 1111000011110000111100001111 and we working with groups of 8, so for our example we will have 00000100, because we have 2 ones in each group.

Complexity: we have only 5 iterations for int32 number, it will be 6 for int64, 7 for int128 and so on. 
For int32 there will be not increase of speed, because even though it is 5 operations, 
each of them consists of several small steps, but for int64 you can fill the difference. Space complexity is O(1).
"""

class Solution:
    def hammingWeight(self, n):
        n = (n & (0x55555555)) + ((n >> 1) & (0x55555555))
        n = (n & (0x33333333)) + ((n >> 2) & (0x33333333))
        n = (n & (0x0f0f0f0f)) + ((n >> 4) & (0x0f0f0f0f))
        n = (n & (0x00ff00ff)) + ((n >> 8) & (0x00ff00ff))
        n = (n & (0x0000ffff)) + ((n >> 16) & (0x0000ffff))
        return n