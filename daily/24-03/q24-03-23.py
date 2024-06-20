# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(h):
            pre = None
            while h:
                next = h.next
                h.next = pre
                pre = h
                h = next
            return pre
        
        def merge(h1,h2):
            dummyHead = ListNode()
            p = dummyHead
            p1 = h1
            p2 = h2 
            while p1 and p2:
                # add node in 1
                p.next = p1
                p = p.next
                p1 = p1.next
                # add node in 2
                p.next = p2
                p = p.next
                p2 = p2.next
            p.next = p1
            return dummyHead.next
        
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        
        cnt = (n+1)//2-1
        p = head
        for _ in range(cnt):
            p = p.next
        head2 = p.next
        p.next = None
        return merge(head,reverseList(head2))