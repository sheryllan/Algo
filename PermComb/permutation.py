"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: [int]):
        num_set = set(nums)

        def recursive_perm(nums_rem: set, perm):
            if not nums_rem:
                yield perm.copy()
            else:
                nums_cpy = list(nums_rem)
                for n in nums_cpy:
                    nums_rem.remove(n)
                    perm.append(n)
                    yield from recursive_perm(nums_rem, perm)
                    nums_rem.add(n)
                    perm.pop()

        return list(recursive_perm(num_set, []))


solution = Solution()
print(solution.permute([1, 2, 3]))
