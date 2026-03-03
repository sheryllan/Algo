"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:
        1         1
       / \         \
      2   5   --->  2
     / \   \         \
    3   4   6         3
                       \
                        4
                         \
                          5
                           \
                            6
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

from typing import Optional
from tree_traversals import build_tree_by_level, print_tree_by_level

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# stack approach
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        curr = root
        stack = []
        while True:
            while curr.left is not None:
                if curr.right is not None:
                    stack.append(curr.right)
                nxt = curr.left
                curr.right = nxt
                curr.left = None
                curr = nxt

            if curr.right is not None:
                stack.append(curr.right)

            if not stack:
                break

            nxt = stack.pop()
            curr.right = nxt
            curr = nxt


# recursion approach with O(1), but essentially uses stack
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(parent, nxt):
            if parent is None:
                return

            left = parent.left
            right = parent.right

            if all(x is None for x in [left, right, nxt]):
                return

            if left is None and right is None:
                parent.right = nxt
            elif left is None and right is not None:
                dfs(right, nxt)
            elif left is not None and right is None:
                parent.left = None
                parent.right = left
                dfs(left, nxt)
            else:
                parent.left = None
                parent.right = left
                dfs(left, right)
                dfs(right, nxt)

        dfs(root, None)



s = Solution()
root = build_tree_by_level([1, 2, 5, 3, 4, None, 6])
s.flatten(root)
assert print_tree_by_level(root) == [1, None, 2, None, 3, None, 4, None, 5, None, 6]

root = build_tree_by_level([])
s.flatten(root)
assert print_tree_by_level(root) == []

root = build_tree_by_level([0])
s.flatten(root)
assert print_tree_by_level(root) == [0]

root = build_tree_by_level([1, 2, None, 3, 4, 5])
s.flatten(root)
k = print_tree_by_level(root)
assert print_tree_by_level(root) == [1, None, 2, None, 3, None, 5, None, 4]

root = build_tree_by_level([1, 2, 5, 3, 4, None, 6, 7, 8, None, None, 9])
s.flatten(root)
assert print_tree_by_level(root) == [1, None, 2, None, 3, None, 7, None, 8, None, 4, None, 5, None, 6, None, 9]

root = build_tree_by_level([3, 1, 4, None, 2])
s.flatten(root)
assert print_tree_by_level(root) == [3, None, 1, None, 2, None, 4]





