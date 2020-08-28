
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:

    def __init__(self, root=None):
        self.root = None if root is None else TreeNode(root)

    def insert(self, key):
        node = TreeNode(key)
        if self.root is None:
            self.root = node
            return

        curr, prev = self.root, None
        while curr is not None:
            prev = curr
            curr = curr.left if key < curr.val else curr.right

        if key < prev.val:
            prev.left = node
        else:
            prev.right = node

    def search(self, key):
        if self.root is None:
            return

        curr = self.root
        while curr is not None and curr.val != key:
            curr = curr.left if key < curr.val else curr.right

        return curr

    @staticmethod
    def inorder(node: TreeNode):
        if node is not None:
            yield from BST.inorder(node.left)
            yield node
            yield from BST.inorder(node.right)

    @staticmethod
    def replace(parent: TreeNode, child: TreeNode = None, new_child: TreeNode = None):
        if parent is None:
            return
        if child is parent.left:
            parent.left = new_child
        elif child is parent.right:
            parent.right = new_child


    def delete(self, key):
        if self.root is None:
            return

        curr, prev = self.root, None
        while curr is not None and curr.val != key:
            prev = curr
            curr = curr.left if key < curr.val else curr.right

        if curr is None:
            return

        if curr.left is not None and curr.right is not None:
            inorder = self.inorder(curr.right)
            to_replace = next(inorder) # find the inorder successor of curr
            prev_to_replace = next(inorder, curr)
            self.replace(prev_to_replace, to_replace, None)
            curr.val = to_replace.val
        else:
            if curr.left is None and curr.right is None:
                to_replace = None
            elif curr.left is None:
                to_replace = curr.right
            else:
                to_replace = curr.left

            if prev is None:
                self.root = to_replace
            else:
                self.replace(prev, curr, to_replace)


def print_inorder(root: TreeNode):
    for n in BST.inorder(root):
        print(n.val)
    print()


tr = BST(50)
tr.insert(30)
tr.insert(20)
tr.insert(40)
tr.insert(70)
tr.insert(60)
tr.insert(80)



assert tr.search(10) is None
assert tr.search(80).val == 80
assert tr.search(100) is None


tr.delete(70)
print_inorder(tr.root)
tr.delete(30)
print_inorder(tr.root)
tr.delete(50)
print_inorder(tr.root)
