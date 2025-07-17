"""
Return the number of contiguous subarrays whose sum is divisible by k
"""

from typing import List


# O(n)
def k_subarrays(nums: List[int], k: int) -> int:
    n = len(nums)
    counts = [0] * k
    cum_sum = 0
    ans = 0

    for i in range(n):
        cum_sum += nums[i]
        mod = cum_sum % k

        ans += counts[mod]
        if mod == 0:
            ans += 1

        counts[mod] += 1

    return ans


assert k_subarrays(nums=[1, 2, 2, 4, 5, 6], k=1) == 21
assert k_subarrays(nums=[9, 0, -6, 4, 8, -2, 5], k=4) == 6