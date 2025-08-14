"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next

        target = l - n
        if target - 1 < 0:
            head = head.next
            return head

        curr = head
        i = 0
        while curr and i < target - 1:
            i += 1
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next

        return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node is not None:
            node = node.next
            l += 1

        dummy = ListNode(next=head)
        prev = dummy
        i = 0
        while i < l - n:
            prev = prev.next
            i += 1

        prev.next = prev.next.next

        return dummy.next


# 双指针的经典应用，如果要删除倒数第n个节点，让fast移动n步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了。
# time beats 100%
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = dummy
        for _ in range(n+1):
            fast = fast.next

        slow = dummy
        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
