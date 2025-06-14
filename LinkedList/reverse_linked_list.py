"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        pilot = dummy
        i = 1
        while i < left:
            pilot = pilot.next
            i += 1

        curr = pilot.next
        prev = None
        i = left
        while i <= right and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1

        pilot.next.next = curr
        pilot.next = prev

        return dummy.next

# head = [1,2,3,4,5], left = 2, right = 4, return = [1,4,3,2,5]
# head = [5], left = 1, right = 1, return = [5]
# head = [1,2,3,4,5], left = 1, right = 3, return = [3,2,1,4,5]
