"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

import unittest as ut


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:

        def recursive_build(i: int, j: int):
            if i == j:
                return

            mid = int((i + j) / 2)
            node = TreeNode(nums[mid])
            node.left = recursive_build(i, mid)
            node.right = recursive_build(mid + 1, j)
            return node

        return recursive_build(0, len(nums))


class Tests(ut.TestCase):
    def setUp(self):
        self.solution = Solution()

    def print_tree_in_order(self, head: TreeNode):
        if head is not None:
            yield head.val

            yield from self.print_tree_in_order(head.left)
            yield from self.print_tree_in_order(head.right)
        else:
            yield None

    def test_normal_list(self):
        nums = [-10, -3, 0, 5, 9]
        expected = [0, -3, -10, None, None, None, 9, 5, None, None, None]

        head = self.solution.sortedArrayToBST(nums)
        actual = list(self.print_tree_in_order(head))

        self.assertListEqual(expected, actual)

