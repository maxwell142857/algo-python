# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head 
        next = head.next
        while next:
            if next.val == cur.val:
                cur.next = next.next
                next = cur.next
            else:
                cur = next
                next = next.next
        return head