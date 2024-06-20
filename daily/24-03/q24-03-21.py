# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        p = dummyHead.next
        stack = []
        while p:
            stack.append(p)
            p = p.next
        
        p = dummyHead
        while stack:
            p.next = stack.pop()
            p = p.next
        p.next = None
        return dummyHead.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        cur = head
        next = cur.next
        head.next = None
        while next:
            nn = next.next
            next.next = cur
            cur = next
            next = nn
        return cur