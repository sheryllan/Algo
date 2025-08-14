"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

from typing import List
from collections import Counter



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        counter = Counter(candidates)
        unique_nums = [0] + list(counter.keys())
        n = len(unique_nums)

        def dfs(i, s, path):
            if s > target:
                return
            if s == target:
                ans.append(path.copy())
                return

            for j in range(i +1, n):
                for k in range(1, counter[unique_nums[j]] + 1):
                    path.append(unique_nums[j])
                    dfs(j, s + k * unique_nums[j], path)

                for _ in range(1, counter[unique_nums[j]] + 1):
                    path.pop()

        dfs(0, 0, [])

        return ans


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, s, path):
            start = i
            while start < n and candidates[start] == candidates[i]:
                start += 1

            path.extend([candidates[i]] * (start - i))
            s += candidates[i] * (start - i)
            for _ in range((start - i + 1) if i == 0 else (start - i)):
                if s < target:
                    j = start
                    while j < n and s + candidates[j] <= target:
                        j = dfs(j, s, path)

                elif s == target:
                    ans.append(path.copy())

                s -= candidates[i]
                if path:
                    path.pop()

            return start

        dfs(0, 0, [])

        return ans


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)
        path = []

        def dfs(i, s):
            if s > target:
                return
            if s == target:
                ans.append(path.copy())
                return

            for j in range(i + 1, n):
                if s + candidates[j] > target:
                    break

                # only appends the first non-duplicate item. back-tracing from the first gives a full combination of
                # the repeating items
                if j > i + 1 and candidates[j] == candidates[j - 1]:
                    continue

                path.append(candidates[j])
                dfs(j, s + candidates[j])
                path.pop()

        dfs(-1, 0)
        return ans


s = Solution()
assert s.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
assert s.combinationSum2([2,5,2,1,2], 5) == [[1,2,2],[5]]
