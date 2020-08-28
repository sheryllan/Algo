"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

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


class Solution:
    def subarraysWithKDistinct(self, A: [int], K: int) -> int:
        i = 0
        min_last_idx = 0
        distinct = set()
        count = 0
        while i < len(A):
            j = i
            while len(distinct) < K:
                distinct.add(A[j])
                j += 1

            while len(distinct) == K:
                count += j - 1






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
A = [1,2,1,2,3]
K = 2
assert solution.subarraysWithKDistinct(A, K) == 7

A = [1,2,1,3,4]
K = 3
assert solution.subarraysWithKDistinct(A, K) == 3

