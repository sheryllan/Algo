"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        last = head
        cnt = 0

        while last:
            cnt += 1
            if not last.next:
                break
            last = last.next

        if cnt == 0 or k % cnt == 0:
            return head

        n = head
        for _ in range(cnt - (k % cnt) - 1):
            n = n.next

        new_tail = n
        new_head = new_tail.next

        last.next = head
        new_tail.next = None

        return new_head



def loop_linked_list(node):
    nd = node
    while nd is not None:
        yield nd.val
        nd = nd.next

solution = Solution()
ns = [ListNode(x) for x in range(1, 6)]
prev = ns[0]
for curr in ns[1:]:
    prev.next = curr
    prev = curr


# nh = solution.rotateRight(ns[0], 3)

nh = solution.rotateRight(ns[0], 12)
print(list(loop_linked_list(nh)))

