"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

For k = 6, you should return: 1->2->3->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


import unittest as ut


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversed_first_k(self, node: ListNode, k: int):
        prev, curr = None, node

        while k > 0 and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1

        if node:
            node.next = curr

        return prev, k

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = new_head = ListNode(None)
        curr.next = head

        while curr.next:
            nxt_k_tail = curr.next
            curr.next = None
            nxt, i = self.reversed_first_k(nxt_k_tail, k)

            if i > 0:
                nxt_k_tail = nxt
                nxt, i = self.reversed_first_k(nxt, k - i)

            curr.next = nxt
            curr = nxt_k_tail

        return new_head.next


class Tests(ut.TestCase):
    def create_linked_list(self, values):
        if not values:
            return

        head = node = ListNode(values[0])
        for val in values[1:]:
            node.next = ListNode(val)
            node = node.next

        return head

    def list_node_values(self, node: ListNode):
        while node:
            yield node.val
            node = node.next

    def test_empty_list(self):
        solution = Solution()
        head = self.create_linked_list([])
        k = 0

        expected = []
        actual = list(self.list_node_values(solution.reverseKGroup(head, k)))
        self.assertListEqual(actual, expected)


    def test_with_one_node(self):
        solution = Solution()
        head = self.create_linked_list([1])
        k = 1

        expected = [1]
        actual = list(self.list_node_values(solution.reverseKGroup(head, k)))
        self.assertListEqual(actual, expected)


    def test_with_k_lt_list_length(self):
        solution = Solution()

        head = self.create_linked_list([1, 2, 3, 4, 5])
        k = 2
        expected = [2, 1, 4, 3, 5]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)

        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        k = 3
        expected = [3, 2, 1, 6, 5, 4, 7, 8]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)


    def test_with_k_eq_list_length(self):
        solution = Solution()

        head = self.create_linked_list([1, 2, 3, 4, 5])
        k = 5
        expected = [5, 4, 3, 2, 1]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)


    def test_with_k_gt_list_length(self):
        solution = Solution()

        head = self.create_linked_list([1, 2, 3, 4, 5])
        k = 8
        expected = [1, 2, 3, 4, 5]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)