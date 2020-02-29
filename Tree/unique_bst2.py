"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

import unittest as ut

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> [TreeNode]:

        def rcsv_gen(i: int):
            if i > n:
                yield None
                return

            for right in rcsv_gen(i + 1):
                node = TreeNode(i)
                node.right = right
                yield node

                while right is not None:
                    # make a copy of the right node's val and right
                    new_node = TreeNode(right.val)
                    new_node.right = right.right

                    # make a copy of the node's val and left, attach right's left to its right
                    new_node_left = TreeNode(node.val)
                    new_node_left.left = node.left
                    new_node_left.right = right.left

                    # attach the new left to new node's left
                    new_node.left = new_node_left

                    yield new_node
                    node = new_node
                    right = new_node.right

        return list(rcsv_gen(1)) if n > 0 else []


class Tests(ut.TestCase):
    def print_tree_in_order(self, head: TreeNode):
        if head is None:
            yield None
            return

        yield head.val
        if head.left or head.right:
            yield from self.print_tree_in_order(head.left)
            yield from self.print_tree_in_order(head.right)


    def test_random(self):
        solution = Solution()
        trees = solution.generateTrees(4)

        expected = [[1, None, 2, None, 3, None, 4],
                    [2, 1, 3, None, 4],
                    [3, 2, 1, None, 4],
                    [4, 3, 2, 1, None, None, None],
                    [1, None, 3, 2, 4],
                    [3, 1, None, 2, 4],
                    [4, 3, 1, None, 2, None, None],
                    [1, None, 4, 3, 2, None, None],
                    [4, 1, None, 3, 2, None, None],
                    [1, None, 2, None, 4, 3, None],
                    [2, 1, 4, 3, None],
                    [4, 2, 1, 3, None],
                    [1, None, 4, 2, None, 3, None],
                    [4, 1, None, 2, None, 3, None]]
        actual = [list(self.print_tree_in_order(tree)) for tree in trees]
        self.assertListEqual(actual, expected)


    def test_zero(self):
        solution = Solution()
        trees = solution.generateTrees(0)
        expected = []
        actual = [list(self.print_tree_in_order(tree)) for tree in trees]
        self.assertListEqual(actual, expected)

