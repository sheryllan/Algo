"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""


from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        curr = sentinel
        while node1 and node2:
            if node1.val <= node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            curr = curr.next

        curr.next = node1 if node1 else node2

        return sentinel.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Split list into two halves: [head..prev] and [slow..end].
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)


def build_list(values: List[int]) -> Optional[ListNode]:
    sentinel = ListNode()
    curr = sentinel
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return sentinel.next


def to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    s = Solution()

    # Basic edge cases.
    assert to_list(s.sortList(build_list([]))) == []
    assert to_list(s.sortList(build_list([1]))) == [1]
    assert to_list(s.sortList(build_list([2, 1]))) == [1, 2]

    # Common examples.
    assert to_list(s.sortList(build_list([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert to_list(s.sortList(build_list([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]

    # Duplicates and already sorted / reverse sorted.
    assert to_list(s.sortList(build_list([3, 3, 1, 2, 2]))) == [1, 2, 2, 3, 3]
    assert to_list(s.sortList(build_list([1, 2, 3, 4, 5]))) == [1, 2, 3, 4, 5]
    assert to_list(s.sortList(build_list([5, 4, 3, 2, 1]))) == [1, 2, 3, 4, 5]

    print("All sortList tests passed.")