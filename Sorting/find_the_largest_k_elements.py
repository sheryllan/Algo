from typing import List


def partition(nums: List[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low

    for j in range(low, high + 1):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = pivot, nums[i]
    return i


# O(n) with quick select algo
def find_largest_k_elements(nums: List[int], k):
    nums_unique = list(set(nums))
    n = len(nums_unique)
    i_intended = n - k
    if i_intended <= 0:
        return nums

    i_pivot = None
    low, high = 0, n - 1

    while i_pivot != i_intended:
        i_pivot = partition(nums_unique, low, high)
        if i_pivot < i_intended:
            low = i_pivot + 1

        elif i_pivot > i_intended:
            high = i_pivot - 1

    return [x for x in nums if x >= nums_unique[i_pivot]]



print(find_largest_k_elements([0, 99, 5, 14, 37, 58, 22, 96], 3))
print(find_largest_k_elements([4, 2], 2))
print(find_largest_k_elements([5, 9, 7, 3, 3, 3, 5], 5))
print(find_largest_k_elements([5, 9, 7, 2, 3, 3, 5], 4))



"""
Explanation of time complexity:

---------------------------
n log(n) implies that the algorithm looks at all N items log(n) times. But that's not what's happening with Quickselect.

Let's say you're using Quickselect to pick the top 8 items in a list of 128. And by some miracle of random selection, the pivots you pick are always at the halfway point.

On the first iteration, the algorithm looks at all 128 items and partitions into two groups of 64 items each. The next iteration splits into two groups of 32 items each. Then 16, and then 8. The number of items examined is:

N + N/2 + N/4 + N/8 + N/16
The sum of that series will never reach 2*N.

The worst case is that partitioning always results in very skewed partition sizes. Consider what would happen if the first partitioning only removed one item. And the second only removed one, etc. The result would be:

N + (N-1) + (N-2) ...

Which is (n^2 + n)/2), or O(n^2).
---------------------------

Quicksort:

T(n) = n + 2T(n/2)
     = n + 2(n/2 + 2T(n/4))
     = n + 2(n/2) + 4T(n/4)
     = n + 2(n/2) + 4(n/4) + ... + n(n/n)
     = 2^0(n/2^0) + 2^1(n/2^1) + ... + 2^log2(n)(n/2^log2(n))
     = n (log2(n) + 1)      (since we are adding n to itself log2 + 1 times)
 
Quickselect:

 T(n) = n + T(n/2)
      = n + n/2 + T(n/4)
      = n + n/2 + n/4 + ... n/n
      = n(1 + 1/2 + 1/4 + ... + 1/2^log2(n))
      = n (1/(1-(1/2))) = 2n                           (by geometric series)


---------------------------

"""
