

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

