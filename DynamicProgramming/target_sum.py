"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

# complexity o(2^n)
class Solution:
    def findTargetSumWays(self, nums: [int], S: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        def rcsv_find(i, cumsum=0):
            if i >= n:
                return int(cumsum == S)

            return rcsv_find(i + 1, cumsum + nums[i]) + rcsv_find(i + 1 , cumsum - nums[i])

        return rcsv_find(0)



# solution = Solution()
# print(solution.findTargetSumWays([0,38,42,31,13,10,11,12,44,16,38,17,22,28,9,27,20,35,34,39], 2))
# assert solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
# assert solution.findTargetSumWays([1, 3, 4, 5], 0) == 0
# assert solution.findTargetSumWays([], 0) == 0


# 2D dynamic programming approch with complexity o(n * l), where l is the range of sum
class Solution2:

    def findTargetSumWays(self, nums: [int], S: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        sums = [{} for _ in range(n)]
        sums[0][nums[0]] = 1
        sums[0][-nums[0]] = sums[0].get(-nums[0], 0) + 1

        for i, num in enumerate(nums[1:]):
            sum_dict = sums[i + 1]
            for sum, cnt in sums[i].items():
                sum_dict[sum + num] = sum_dict.get(sum + num, 0) + cnt
                sum_dict[sum - num] = sum_dict.get(sum - num, 0) + cnt

        return sums[n - 1].get(S, 0)


#
# solution2 = Solution2()
# assert solution2.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
# assert solution2.findTargetSumWays([1, 3, 4, 5], 0) == 0
# assert solution2.findTargetSumWays([0, 1], 1) == 2
# print(solution2.findTargetSumWays([0,38,42,31,13,10,11,12,44,16,38,17,22,28,9,27,20,35,34,39], 2))


# 1D dynamic programming using dict
class Solution3:

    def findTargetSumWays(self, nums: [int], S: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        last_counts = {nums[0]: 1}
        last_counts[-nums[0]] = last_counts.get(-nums[0], 0) + 1
        for num in nums[1:]:
            sum_counts = {}
            for sum, cnt in last_counts.items():
                sum_counts[sum + num] = sum_counts.get(sum + num, 0) + cnt
                sum_counts[sum - num] = sum_counts.get(sum - num, 0) + cnt

            last_counts = sum_counts

        return last_counts.get(S, 0)


# solution3 = Solution3()
# assert solution3.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
# assert solution3.findTargetSumWays([1, 3, 4, 5], 0) == 0
# assert solution3.findTargetSumWays([0, 1], 1) == 2
# print(solution3.findTargetSumWays([0, 38, 42, 31, 13, 10, 11, 12, 44, 16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39], 2))


# 1D dynamic programming using list
class Solution4:
    MAX_SUM = 1000

    def findTargetSumWays(self, nums: [int], S: int) -> int:
        n = len(nums)
        if n == 0:
            return 0


        sum_counts = [0] * (2 * self.MAX_SUM + 1)
        sum_counts[nums[0] + self.MAX_SUM] += 1
        sum_counts[self.MAX_SUM - nums[0]] += 1

        for num in nums[1:]:
            next_counts = [0] * (2 * self.MAX_SUM + 1)
            for i, cnt in enumerate(sum_counts):
                if not cnt:
                    continue

                next_counts[i + num] += cnt
                next_counts[i - num] += cnt

            sum_counts = next_counts

        return sum_counts[S + 1000] if abs(S) <= self.MAX_SUM else 0

solution4 = Solution4()
assert solution4.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
assert solution4.findTargetSumWays([1, 3, 4, 5], 0) == 0
assert solution4.findTargetSumWays([0, 1], 1) == 2
print(solution4.findTargetSumWays([0, 38, 42, 31, 13, 10, 11, 12, 44, 16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39], 2))

