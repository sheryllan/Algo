"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# solution 1
def find_subsets(nums: list):
    ans = []
    subset = []
    n = len(nums)
    def dfs(i):
        if i == n:
            ans.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return ans

# solution 2
def find_subsets2(nums: list):
    ans = []
    subset = []
    n = len(nums)

    def dfs(i):
        ans.append(subset.copy())

        if i == n:
            return

        for j in range(i, n):
            subset.append(nums[j])
            dfs(j + 1)
            subset.pop()

    dfs(0)
    return ans

print(find_subsets([1, 2, 4]))
print(find_subsets2([1, 2, 4]))
print(find_subsets([1, 2, 3, 5, 6]))
print(find_subsets2([1, 2, 3, 5, 6]))

