"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of
different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.



Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""




def subarrays_of_max_K_distinct(A: [int], K: int) -> int:
    num_counts = {}
    subarrays = 0
    left_i = right_i = 0
    add_count = True
    while left_i <= right_i < len(A):
        if add_count:
            if A[right_i] not in num_counts:
                num_counts[A[right_i]] = 1
            else:
                num_counts[A[right_i]] += 1

        add_count = len(num_counts) <= K
        if add_count:
            subarrays += right_i - left_i + 1
            right_i += 1
        else:
            n = num_counts[A[left_i]] - 1
            if n == 0:
                num_counts.pop(A[left_i])
            else:
                num_counts[A[left_i]] = n
            left_i += 1
    return subarrays

def subarraysWithKDistinct(A: [int], K: int) -> int:
    return subarrays_of_max_K_distinct(A, K) - subarrays_of_max_K_distinct(A, K - 1)


# def subarraysWithKDistinct(A: [int], K: int) -> int:
#     N = len(A)
#     seen = set()
#     count = 0
#     i = 0
#     while i < N:
#         i_distinct = i
#         seen.add(A[i])
#         while i_distinct < N and A[i_distinct] == A[i]:
#             i_distinct += 1
#         # i_distinct would be the next index to the item not equal to A[i]
#
#         j = i_distinct
#         while j < N and len(seen) < K:
#             seen.add(A[j])
#             j += 1
#         # j at the end would be the next index to the item outside the k already seen integers
#
#         if len(seen) < K:
#             return count
#
#         j_distinct = j
#         while j_distinct < N and A[j_distinct] in seen:
#             j_distinct += 1
#         # j_distinct would be the index of the first not seen integer
#
#         count += (i_distinct - i) * (j_distinct - j + 1)
#         seen.clear()
#         i = i_distinct
#
#     return count


def subarraysWithKDistinct_slidingWindow(A: [int], K: int) -> int:
    i = 0  # index of the subarray head
    j = 0  # index of the subarray tail
    N = len(A)
    last_seen = {}
    count = 0
    while i < N - K + 1 and not (j >= N and len(last_seen) < K):
        assert len(last_seen) <= K

        repeats = 0
        while len(last_seen) == K and i < last_seen[A[i]]:
            # find the last index of K integers, count the subarrays indexed from i
            while j < N and A[j] in last_seen:
                last_seen[A[j]] = j
                repeats += 1
                j += 1
            count += repeats
            i += 1

        if len(last_seen) == K and i == last_seen[A[i]]:
            last_seen.pop(A[i])  # pop out the last seen
            count += 1  # the count of item where i = last_seen
            i += 1

        last_seen[A[j]] = j
        if len(last_seen) == K:
            count += 1

        j += 1



        # while j < N and len(last_seen) <= K:
        #     last_seen[A[j]] = j
        #     if len(last_seen) > K:
        #         last_seen.pop(A[j])
        #         break
        #     if len(last_seen) == K:
        #         count += 1
        #
        #     j += 1  # j = index next to that of the last integer last seen
        #
        # # count from the first to the one prior to the last seen for the last seen has been counted in last loop
        # while len(last_seen) == K and i < last_seen[A[i]]:
        #     count += 1
        #     i += 1  # i = last seen index at the end
        #
        # last_seen.pop(A[i])  # pop out the last seen
        # i += 1  # move the head to the next item

    return count


print(subarraysWithKDistinct_slidingWindow(A=[1, 2, 1, 2, 3], K=2))
print(subarraysWithKDistinct_slidingWindow(A=[1, 2, 1, 3, 4], K=3))





print(subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=2))
print(subarraysWithKDistinct(A=[1, 2, 1, 3, 4], K=3))


class Solution:
    def subarraysWithKDistinct(self, A: [int], K: int) -> int:
        # i = 0
        # min_last_idx = 0
        # distinct = set()
        # count = 0
        # while i < len(A):
        #     j = i
        #     while len(distinct) < K:
        #         distinct.add(A[j])
        #         j += 1
        #
        #     while len(distinct) == K:
        #         count += j - 1

        count = 0
        last_at = {}
        j, i_of_1st_K = 0, 0
        for i, a in enumerate(A):
            if i_of_1st_K == i:
                i_of_1st_K = j - 1

            while j < len(A) and len(last_at) + int(A[j] not in last_at) <= K:
                if len(last_at) < K:
                    i_of_1st_K = j

                last_at[A[j]] = j
                j += 1

            if len(last_at) == K:
                count += j - max(i_of_1st_K, i + 1)

            if a in last_at and last_at[a] == i:
                last_at.pop(a)

        return count


solution = Solution()
A = [1, 2, 1, 2, 3]
K = 2
assert solution.subarraysWithKDistinct(A, K) == 7

A = [1, 2, 1, 3, 4]
K = 3
assert solution.subarraysWithKDistinct(A, K) == 3
