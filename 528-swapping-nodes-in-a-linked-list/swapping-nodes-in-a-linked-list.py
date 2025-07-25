# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        n = 0
        curr = dummy
        while curr.next:
            n += 1
            curr = curr.next
        prev1, prev2 = dummy, dummy
        for _ in range(1, k):
            prev1 = prev1.next
        for _ in range(k, n):
            prev2 = prev2.next
        node1, node2 = prev1.next, prev2.next
        if node1 == node2:
            return dummy.next
        elif node1.next == node2:
            prev1.next = node2
            node1.next = node2.next
            node2.next = node1
        elif node2.next == node1:
            prev2.next = node1
            node2.next = node1.next
            node1.next = node2
        else:
            prev1.next = node2
            prev2.next = node1
            tmp = node2.next
            node2.next = node1.next
            node1.next = tmp
        return dummy.next