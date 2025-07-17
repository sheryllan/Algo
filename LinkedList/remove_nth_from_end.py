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