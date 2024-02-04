from __future__ import annotations
from dataclasses import dataclass

from enum import Enum

class Colour(Enum):
    red = 0
    black = 1

@dataclass
class Node:
    val: int
    left: Node = None
    right: Node = None
    parent: Node = None
    colour: Colour = Colour.red


def insert_leaf(val: int, current: Node) -> Node:
    if current is None or val == current.val:
        return current
    elif val < current.val:
        leaf = insert_leaf(val, current.left)
        if leaf is None:
            leaf = current.left = Node(val, parent=current, colour=Colour.red)
    else:
        leaf = insert_leaf(val, current.right)
        if leaf is None:
            leaf = current.right = Node(val, parent=current, colour=Colour.red)
    return leaf


def change_colour(node: Node):
    if node.parent is None or not (node.colour == node.parent.colour == Colour.red):
        return
    parent = node.parent
    if parent is None:
        return
    parent.colour = Colour.black
    grandparent = parent.parent
    if grandparent is None:
        return

    grandparent.colour = Colour.black if grandparent.parent is None else Colour.red
    uncle = grandparent.right if parent.val < grandparent.val else grandparent.left

    if uncle and uncle.colour == Colour.red:
        uncle.colour = Colour.black

    change_colour(grandparent)


def insert(new_value: int, root: Node):
    if root is None:
        return Node(new_value, colour=Colour.black)
    child = insert_leaf(new_value, root)
    parent = child.parent
    if parent is None:  # root
        child.colour = Colour.black
        return root

    grandparent = parent.parent
    if grandparent is None:
        assert parent.colour == Colour.black
        return root
    if parent.colour == Colour.black:
        return root

    is_parent_left = parent.val <= grandparent.val
    is_left = child.val <= parent.val
    uncle = grandparent.right if is_parent_left else grandparent.left
    uncle_colour = Colour.black if uncle is None else uncle.colour

    if parent.colour == uncle_colour == Colour.red:
        change_colour(child)
    else:
        if is_left and (not is_parent_left):
            child.right = parent
            child.parent = grandparent
            parent.left = None
            parent.parent = child
            parent = child
            grandparent.right = parent
            is_left = False
        elif (not is_left) and is_parent_left:
            child.left = parent
            child.parent = grandparent
            parent.right = None
            parent.parent = child
            parent = child
            grandparent.left = parent
            is_left = True

        if is_left and is_parent_left:
            parent.right = grandparent
            parent.parent = grandparent.parent
            grandparent.parent = parent
            grandparent.left = None
        elif (not is_left) and (not is_parent_left):
            parent.left = grandparent
            parent.parent = grandparent.parent
            grandparent.parent = parent
            grandparent.right = None

        if parent.parent is not None:
            if parent.val < parent.parent.val:
                parent.parent.left = parent
            else:
                parent.parent.right = parent

        parent.colour = Colour.black
        grandparent.colour = Colour.red

    return root if root.parent is None else root.parent

def inorderTraversalHelper(node: Node):
    if node is not None:
        # Perform Inorder Traversal
        inorderTraversalHelper(node.left)
        print(node.val, end=" ")
        inorderTraversalHelper(node.right)

def printTreeHelper(root: Node, space=0):
    if root is not None:
        space += 10
        # Print the tree structure
        printTreeHelper(root.right, space)
        print("\n" + " " * (space - 10) + str(root.val))
        printTreeHelper(root.left, space)


arr = [1, 4, 6, 3, 5, 7, 8, 2, 9]
# arr = [3, 5, 8, 9, 0, 4, 10]
root = None
for i in range(len(arr)):
    root = insert(arr[i], root)

inorderTraversalHelper(root)
printTreeHelper(root)









