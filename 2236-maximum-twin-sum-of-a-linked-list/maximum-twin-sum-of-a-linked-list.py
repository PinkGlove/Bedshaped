# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        prev = dummy
        curr = head
        while prev != slow:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        res = 0
        while start:
            res = max(res, start.val + prev.val)
            prev = prev.next
            start = start.next
        return res