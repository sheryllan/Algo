"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10e9 <= nums1[i], nums2[j] <= 10e9
"""



"""
错误的思路

如果从左往右地把 nums2合并到 nums1中，假设 nums2[0]<nums1[0]，那么 nums2[0] 会直接覆盖掉 nums1[0]，这不是我们期望看到的。

正确的思路

如果从右往左地把 nums2合并到 nums1中，是否会发生错误的覆盖呢？我们来看几个例子：
nums1=[1,2,3,∗,∗,∗],nums2=[4,5,6]。这里我用 ∗ 表示可以填入的空位。在这个例子中，nums2可以直接填入 nums1后面的 3 个空位，得到 [1,2,3,4,5,6]，没有任何错误覆盖。
nums=[1,2,6,∗,∗,∗],nums2=[3,4,5]。这里 nums1中的 6 是最大的，应当填入末尾。现在 nums1=[1,2,∗,∗,∗,6]，注意 nums1[2] 这个位置现在空出了。
然后把 nums2中的数字填入空位，得到 [1,2,3,4,5,6]，没有任何错误覆盖。
上面的例子表明，把 nums1中的数字移到另一个空位，又产生了一个新的空位，所以剩余空位的个数是不变的，我们总是有空位可以让 nums2的数字填入，不会发生错误覆盖，这是如下算法正确的前提。

链接：https://leetcode.cn/problems/merge-sorted-array/solutions/2385610/dao-xu-shuang-zhi-zhen-wei-shi-yao-dao-x-xxkp/
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0:  # nums2 还有要合并的元素
            # 如果 p1 < 0，那么走 else 分支，把 nums2 合并到 nums1 中
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # 填入 nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]  # 填入 nums2[p1]
                p2 -= 1
            p -= 1  # 下一个要填入的位置
