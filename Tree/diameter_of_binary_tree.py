"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return (0, 0)

            left_edges_max, left_diameter_max = dfs(node.left)
            right_edges_max, right_diameter_max = dfs(node.right)

            edges_max = max(left_edges_max, right_edges_max) + 1
            diameter_max = max(left_diameter_max, right_diameter_max, left_edges_max + right_edges_max)
            return (edges_max, diameter_max)

        return dfs(root)[1]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(node):
            if node is None:
                return 0

            left_edges = dfs(node.left)
            right_edges = dfs(node.right)
            diameter[0] = max(diameter[0], left_edges + right_edges)
            return max(left_edges, right_edges) + 1

        dfs(root)
        return diameter[0]


