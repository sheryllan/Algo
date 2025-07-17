

# dp[i] = max(dp[i - 1], 0) + nums[i]
def max_sum(nums: [int]):
    subarray_sum = float('-inf')
    total = 0
    for x in nums:
        total = max(total, 0) + x
        subarray_sum = max(total, subarray_sum)

    return subarray_sum