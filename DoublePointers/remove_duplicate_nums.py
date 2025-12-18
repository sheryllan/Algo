from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        to_swap = min(3, n - 1)

        for i in range(2, n):
            if nums[i] < nums[i - 1]:
                nums[i], nums[to_swap] = nums[to_swap], nums[i]

            if nums[i] == nums[i - 1] == nums[i - 2]:
                while to_swap < n - 1 and nums[to_swap] <= nums[i]:
                    to_swap += 1

                nums[i], nums[to_swap] = nums[to_swap], nums[i]

            to_swap += 1

            if to_swap == n:
                if nums[i] < nums[i - 1] or nums[i] == nums[i - 1] == nums[i - 2]:
                    return i

                if i == n - 1 or nums[i-1] == nums[i] == nums[i+1]:
                    return i + 1

                return i + 1 + int(nums[i] <= nums[i+1])

        return n


s = Solution()
a = [1,1,1,2,2,3]
assert a[:s.removeDuplicates(a)] == [1,1,2,2,3]

a = [0,0,0]
assert a[:s.removeDuplicates(a)] == [0,0]

a = [0,0,1,1,1,1,2,3,3]
assert a[:s.removeDuplicates(a)] == [0,0,1,1,2,3,3]

a = [1,2,2,3]
assert a[:s.removeDuplicates(a)] == [1,2,2,3]

a = [1,1,2,2]
assert a[:s.removeDuplicates(a)] == [1,1,2,2]

a = [1,1,1,2,2,2,3,3]
assert a[:s.removeDuplicates(a)] == [1,1,2,2,3,3]

a = [0,1,2,2,2,2,2,3,4,4,4]
assert a[:s.removeDuplicates(a)] == [0,1,2,2,3,4,4]

a = [1,1,2,3]
assert a[:s.removeDuplicates(a)] == [1,1,2,3]