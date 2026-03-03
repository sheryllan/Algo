
"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

       3
    /    \
   9     20
        /   \
       15    7

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of UNIQUE values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The key part is that traversing through preorder is essentially going down a subtree from the top node of the subtree
# in which case you can construct the top node and get the left and right node recursively
# a queue is essentially used to traverse through preorder
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {x: i for i, x in enumerate(inorder)}
        sub_preorder = preorder

        def build(in_start, in_end):
            if not inorder[in_start: in_end]:
                return None

            parent = TreeNode(sub_preorder[0])  # or use a queue and popleft here
            in_i = inorder_indices[parent.val]
            sub_preorder[:] = sub_preorder[1:]
            left = build(in_start, in_i)
            right = build(in_i + 1, in_end)

            parent.left = left
            parent.right = right
            return parent

        return build(0, len(inorder))







