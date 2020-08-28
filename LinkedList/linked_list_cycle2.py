"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        node = head

        while node is not None:
            if node in seen:
                break

            seen.add(node)
            node = node.next

        return node


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

s = Solution()
n = s.detectCycle(head)


"""
Floyd's Algo


Proof:
l - number of loops (the distance node of slow looping travels)
x - the position where the cycle begins (number of nodes not in the cycle)
y - the number of nodes in the cycle 
i - the offset from x where slow and fast node first meet
n - the number of times slow node complete a cycle before meeting fast node

(l - x) % y = i
(2l - x) % y = i

--> (l - x) + ky = 2l - x
--> ky = l
where k denotes the multiple of y fast node travels more than that of the slow node 

replacing l in the equation l = x + ny + i, gives:
ky = x + i + ny
x + i = (k - n)y = my
x = my - i = (y - i) + (m - 1)y
so the distance x is equivalent to travels till the end of the cycle (y - i) and loop the cycle from x for (m - 1) times  
after the fast node reset, slow and fast will meet at x 

"""
def detectCycle(head):
    fast = head
    slow = head
    while fast is not None and slow is not None:
        if fast.next is None:
            return None
        else:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
    return None


