# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = prev.next
        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = prev.next
                curr = curr.next
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
        return dummy.next

