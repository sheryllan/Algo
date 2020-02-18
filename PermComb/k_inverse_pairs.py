"""
Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 10^9 + 7. (because the 32bit int ranges from -(2^31) to 2^31 - 1,
2^31 = 2,147,483,648 = 10^(31*log2) ~= 10^(31*0.3) = 10^9.3 ~= 2*10^9, each element in the addition should be roughly less than 10^9 + 7)

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation:
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.


Example 2:

Input: n = 3, k = 1
Output: 2
Explanation:
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Note:

The integer n is in the range [1, 1000] and k is in the range [0, 1000].
"""


class Solution:
    M = int(1e9 + 7)

    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0] * (k + 1)
        for i in range(1, n + 1):
            new_dp = [1] + [0] * k
            for j in range(1, k + 1):
                count = (dp[j] - (0 if j - i < 0 else dp[j - i])) % self.M
                new_dp[j] = (new_dp[j - 1] + count) % self.M
            dp = new_dp

        return (dp[k] - (0 if k < 1 else dp[k - 1])) % self.M

    # An equivalent
    # def kInversePairs(self, n: int, k: int) -> int:
    #     dp = [1] * (k + 1)
    #     for i in range(2, n):
    #         new_dp = [1] + [0] * k
    #         for j in range(1, k + 1):
    #             count = (dp[j] - (0 if j - i < 0 else dp[j - i])) % self.M
    #             new_dp[j] = (new_dp[j - 1] + count) % self.M
    #         dp = new_dp
    #
    #     return (dp[k] - (0 if k < n else dp[k - n])) % self.M


print(Solution().kInversePairs(1, 0))
# print(Solution().kInversePairs(5, 3))
print(Solution().kInversePairs(1000, 1000))


"""
Complexity Analysis

Time complexity : O(n*k). dp array of size k+1 is filled n+1 times.

Space complexity : O(k). dp array of size (k+1) is used."""