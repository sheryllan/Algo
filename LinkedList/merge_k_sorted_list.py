"""
Given an array of linked-lists lists, each linked list is sorted in ascending order.

Merge all the linked-lists into one sort linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""

from collections import deque
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_2_lists(self, list1, list2):
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2

        if list1.val <= list2.val:
            head = node1 = list1
            node2 = list2
        else:
            head = node1 = list2
            node2 = list1

        node1_prev, node2_prev = node1, node2
        while node1 is not None and node2 is not None:
            if node2.val < node1.val:
                node1_prev.next = node2
                node2 = node1
                node1 = node1_prev.next

            node1_prev = node1
            node1 = node1.next

        node1_prev.next = node2

        return head

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        q = deque(lists)
        head = lists[0]
        while q:
            head = list1 = q.popleft()
            if q:
                list2 = q.popleft()
                merged = self.merge_2_lists(list1, list2)
                q.append(merged)
                head = merged

        return head


def build_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None

    head = prev = ListNode(values[0])
    for v in values[1:]:
        node = ListNode(v)
        prev.next = node
        prev = node

    return head

def convert_linked_list(head):
    ret = []
    curr = head
    while curr is not None:
        ret.append(curr.val)
        curr = curr.next

    return ret



s = Solution()

values = [[7, 9], [], [1, 4, 7], [5, 10], [10, 12]]
lists = [build_linked_list(x) for x in values]
assert convert_linked_list(s.mergeKLists(lists)) == [1, 4, 5, 7, 7, 9, 10, 10, 12]

values = [[1,4,5],[1,3,4],[2,6]]
lists = [build_linked_list(x) for x in values]
assert convert_linked_list(s.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

assert s.mergeKLists([]) is None
assert convert_linked_list(s.mergeKLists([None])) == []


