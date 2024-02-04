"""
Question:
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than 1.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def get_depth(self, node: TreeNode):
        if node is None:
            return -1

        left_depth = self.get_depth(node.left)
        if left_depth is False:
            return False

        right_depth = self.get_depth(node.right)
        if right_depth is False:
            return False

        return abs(left_depth - right_depth) <= 1 and max(left_depth, right_depth) + 1

    def is_balanced(self, head: TreeNode):
        depth = self.get_depth(head)
        return depth is not False


if __name__ == '__main__':
    solution = Solution()

    head = TreeNode(6)
    head.left = l1 = TreeNode(3)
    head.right = r1 = TreeNode(5)
    l1.left = l2 = TreeNode(2)
    l2.left = TreeNode(1)
    r1.left = TreeNode(0)

    assert solution.is_balanced(head) is False

    l1.right = TreeNode(4)
    assert solution.is_balanced(head) is True

    r1.right = r2 = TreeNode(7)
    r2.right = TreeNode(8)
    assert solution.is_balanced(head) is True

    r2.right.right = TreeNode(9)
    assert solution.is_balanced(head) is False


