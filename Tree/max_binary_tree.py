"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""

import unittest as ut


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: [int]) -> TreeNode:

        def recursive_construct(arr):
            if not arr:
                return None

            idx_max = arr.index(max(arr))
            node = TreeNode(arr[idx_max])
            node.left = recursive_construct(arr[:idx_max])
            node.right = recursive_construct(arr[idx_max + 1:])

            return node

        return recursive_construct(nums)


class Tests(ut.TestCase):
    def print_tree_in_order(self, head: TreeNode):
        if head is not None:
            yield head.val

            yield from self.print_tree_in_order(head.left)
            yield from self.print_tree_in_order(head.right)
        else:
            yield None

    def test_normal_list(self):
        solution = Solution()
        nums = [3, 2, 1, 6, 0, 5]
        expected = [6, 3, None, 2, None, 1, None, None, 5, 0, None, None, None]

        ret_node = solution.constructMaximumBinaryTree(nums)
        actual = list(self.print_tree_in_order(ret_node))

        self.assertListEqual(actual, expected)


    def test_monotonic_list(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        expected = [7, 6, 5, 4, 3, 2, 1] + ([None] * 8)

        ret_node = solution.constructMaximumBinaryTree(nums)
        actual = list(self.print_tree_in_order(ret_node))

        self.assertListEqual(actual, expected)


    def test_empty_list(self):
        solution = Solution()
        nums = []
        expected = [None]

        ret_node = solution.constructMaximumBinaryTree(nums)
        actual = list(self.print_tree_in_order(ret_node))
        self.assertListEqual(actual, expected)



"""
Complexity Analysis

Time complexity : O(n^2). 
The function construct is called nn times. At each level of the recursive tree, we traverse over all the nn elements to find the maximum element. 
In the average case, there will be a log(n) levels leading to a complexity of O(nlog(n)). 
In the worst case, the depth of the recursive tree can grow up to n, which happens in the case of a sorted numsnums array, giving a complexity of O(n^2).

Space complexity : O(n). The size of the test can grow up to n in the worst case. 
In the average case, the size will be log(n) for n elements in nums, giving an average case complexity of O(log n)
"""