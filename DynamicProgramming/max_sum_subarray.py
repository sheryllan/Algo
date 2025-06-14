

# dp[i] = max(dp[i - 1], 0) + nums[i]
def max_sum(nums: [int]):
    subarray_sum = 0
    for x in nums:
        subarray_sum = max(subarray_sum, 0) + x

    return subarray_sum