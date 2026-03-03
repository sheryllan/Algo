from math import log2, floor

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_by_level(nodes):
    if not nodes:
        return None

    i = 0
    root = TreeNode(nodes[0])
    q = [root]
    while q:
        # n = len(q)
        new_q = []
        j = 0
        for node in q:
            if node is None:
                continue

            left_exist = 2 * (i + j) + 1 < len(nodes)
            right_exist = 2 * (i + j) + 2 < len(nodes)
            if left_exist:
                left_val = nodes[2 * (i + j) + 1]
                left = None if left_val is None else TreeNode(left_val)
                node.left = left
                new_q.append(left)
            if right_exist:
                right_val = nodes[2 * (i + j) + 2]
                right = None if right_val is None else TreeNode(right_val)
                node.right = right
                new_q.append(right)

            j += 1  # the count of non-None node

        i = i + j
        q = new_q

    return root


def print_tree_by_level(root):
    if root is None:
        print([])
        return []

    q = [root]
    result = []

    while True:
        new_q =[]
        for node in q:
            if node is not None:
                result.append(node.val)
                new_q.append(node.left if node.left is not None else None)
                new_q.append(node.right if node.right is not None else None)
            else:
                result.append(None)

        if all(x is None for x in new_q):
            break

        q = new_q

    i = len(result) - 1
    while i >= 0:
        if result[i] is not None:
            break
        i -= 1

    result = result[:i+1]
    print(result)
    return result


if __name__ == '__main__':
    nodes = [1,2,5,3,4,None,6,7,8,None,None,9]
    root = build_tree_by_level(nodes)
    print_tree_by_level(root)

    nodes = [3,1,4,None,2]
    root = build_tree_by_level(nodes)
    print_tree_by_level(root)

    nodes = [1,2,5,3,4,6,None,7,8,None,None,9,10]
    root = build_tree_by_level(nodes)
    print_tree_by_level(root)