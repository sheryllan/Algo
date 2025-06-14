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

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""


import unittest as ut


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=None, nxt=None):
        self.val = x
        self.next = nxt


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

    def reverse_nodes(self, head: ListNode, k: int):
        node = head
        length = 0
        while node:
            node = node.next
            length += 1

        curr = head
        dummy = ListNode(nxt=head)
        prev = dummy
        last = prev
        for _ in range(length // k):
            first = curr
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            last.next = prev
            last = first

        last.next = curr
        return dummy.next

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
        k = 1

        expected = []
        actual = list(self.list_node_values(solution.reverseKGroup(head, k)))
        self.assertListEqual(actual, expected)
        print(list(self.list_node_values(solution.reverse_nodes(self.create_linked_list([]), k))))


    def test_with_one_node(self):
        solution = Solution()
        head = self.create_linked_list([1])
        k = 1

        expected = [1]
        actual = list(self.list_node_values(solution.reverseKGroup(head, k)))
        self.assertListEqual(actual, expected)
        print(list(self.list_node_values(solution.reverse_nodes(self.create_linked_list([1]), k))))


    def test_with_k_lt_list_length(self):
        solution = Solution()

        head = self.create_linked_list([1, 2, 3, 4, 5])
        k = 2
        expected = [2, 1, 4, 3, 5]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)
        print(list(self.list_node_values(solution.reverse_nodes(self.create_linked_list([1, 2, 3, 4, 5]), k))))

        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        k = 3
        expected = [3, 2, 1, 6, 5, 4, 7, 8]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)
        print(list(self.list_node_values(solution.reverse_nodes(self.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8]), k))))


    def test_with_k_eq_list_length(self):
        solution = Solution()

        head = self.create_linked_list([1, 2, 3, 4, 5])
        k = 5
        expected = [5, 4, 3, 2, 1]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)
        print(list(self.list_node_values(solution.reverse_nodes(self.create_linked_list([1, 2, 3, 4, 5]), k))))


    def test_with_k_gt_list_length(self):
        solution = Solution()

        head = self.create_linked_list([1, 2, 3, 4, 5])
        k = 8
        expected = [1, 2, 3, 4, 5]
        actual_head = solution.reverseKGroup(head, k)
        actual = list(self.list_node_values(actual_head))
        self.assertListEqual(actual, expected)
        print(list(self.list_node_values(solution.reverse_nodes(self.create_linked_list([1, 2, 3, 4, 5]), k))))




from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 统计节点个数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(nxt=head)
        pre = None
        cur = head

        # k 个一组处理
        while n >= k:
            n -= k
            for _ in range(k):  # 同 92 题
                nxt = cur.next
                cur.next = pre  # 每次循环只修改一个 next，方便大家理解
                pre = cur
                cur = nxt

            # 见视频
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
