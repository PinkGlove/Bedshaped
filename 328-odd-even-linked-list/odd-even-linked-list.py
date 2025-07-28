# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        end = head
        total = 1
        while end.next:
            end = end.next
            total += 1
        curr = head
        cnt = 0
        while cnt < (total // 2):
            end.next = curr.next
            curr.next = curr.next.next
            end = end.next
            end.next = None
            curr = curr.next
            cnt += 1
        return head