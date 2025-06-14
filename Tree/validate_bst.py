"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Bottom-up
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node: TreeNode):
            if node is None:
                return True

            left, right = node.left, node.right
            if left is not None and left.val >= node.val:
                return False
            if right is not None and right.val <= node.val:
                return False

            min_val, max_val = node.val, node.val
            r_left = validate(left)
            if not r_left:
                return False
            if isinstance(r_left, tuple):
                min_left, max_left = r_left
                if max_left >= node.val:
                    return False
                min_val = min(min_left, min_val)

            r_right = validate(right)
            if not r_right:
                return False
            if isinstance(r_right, tuple):
                min_right, max_right = r_right
                if min_right <= node.val:
                    return False
                max_val = max(max_right, max_val)

            return min_val, max_val

        result = validate(root)
        return result is not False


# Top-down, Preorder traversal
class Solution2:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)



class Solution3:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


from math import inf
from typing import Optional, Tuple


#链接：https://leetcode.cn/problems/validate-binary-search-tree/solutions/2020306/qian-xu-zhong-xu-hou-xu-san-chong-fang-f-yxvh/
# Inorder traversal
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left) or root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)


# Postorder traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return inf, -inf
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            # 也可以在递归完左子树之后立刻判断，如果发现不是二叉搜索树，就不用递归右子树了
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf



