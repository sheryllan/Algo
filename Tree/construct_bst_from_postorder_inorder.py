"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Similar to preorder, the reverse of postorder traverses in order parent -> right subtree -> left subtree
# so that using a stack to loop through postorder is good
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {x: i for i, x in enumerate(inorder)}

        def build(start_in, end_in, sub_postorder):
            if not inorder[start_in: end_in]:
                return None

            parent = TreeNode(sub_postorder.pop())
            mid = inorder_indices[parent.val]
            right = build(mid + 1, end_in, sub_postorder)
            left = build(start_in, mid, sub_postorder)

            parent.left = left
            parent.right = right
            return parent

        left = None
        i_in = 0
        node = None
        while i_in < len(inorder):
            node = TreeNode(inorder[i_in])
            while i_in < len(inorder) and node.val == postorder[i_in]:
                node.left = left
                left = node
                i_in += 1
                if i_in >= len(inorder):
                    break
                node = TreeNode(inorder[i_in])

            if node is not left:
                node.left = left

            j_post = i_in
            while j_post < len(postorder) and node.val != postorder[j_post]:
                j_post += 1

            right = build(i_in + 1, j_post + 1, postorder[i_in: j_post])
            node.right = right

            i_in = j_post + 1
            left = node

        return node

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {x: i for i, x in enumerate(inorder)}
        sub_postorder = postorder.copy()

        def build(start_in, end_in):
            if not inorder[start_in: end_in]:
                return None

            parent = TreeNode(sub_postorder.pop())
            mid = inorder_indices[parent.val]
            right = build(mid + 1, end_in)
            left = build(start_in, mid)

            parent.left = left
            parent.right = right
            return parent

        return build(0, len(inorder))