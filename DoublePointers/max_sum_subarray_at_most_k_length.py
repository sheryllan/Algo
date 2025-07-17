from typing import List


# O(n * k)
def get_max_sum_of_at_most_k(nums: List[float], k):
    n = len(nums)
    max_sum = 0

    for i in range(n - k):
        max_total = 0
        for j in range(i, i + k):
            max_total = max(max_total + nums[j], nums[j])
            max_sum = max(max_total, max_sum)

    return max_sum

def get_max_sum_of_at_most_k2(nums: List[float], k):
    n = len(nums)
    max_sum = 0
    max_sub_totals = [0] * 2

    max_sub_total = 0
    for i in range(k - 1, -1, -1):
        max_sub_total = max(max_sub_total + nums[i], nums[i])
        max_sum = max(max_sum, max_sub_total)
        if i < len(max_sub_totals):
            max_sub_totals[1] = max_sum

    end = k
    for start in range(1, n - k):
        max_sub_total = max(max_sub_totals[1] + nums[end], nums[end])
        max_sum = max(max_sum, max_sub_total)

        max_sub_totals[0]




        max_total = 0
        for j in range(i, i + k):
            max_total = max(max_total + nums[j], nums[j])
            max_sum = max(max_total, max_sum)

    return max_sum


print(get_max_sum_of_at_most_k([-3, 4, 2, -2, 2, 5], 4))












