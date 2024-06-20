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
        # find the mid point 
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        def reverseList(h):
            pre = None
            cur = h
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur 
                cur = next
            return pre
        
        rHead2 = reverseList(head2)

        def mergeList(h1,h2):
            dummyHead = ListNode()
            p,p1,p2 = dummyHead,h1,h2
            while p1 and p2:
                p.next = p1
                p = p.next
                p1 = p1.next
                p.next = p2
                p = p.next
                p2 = p2.next
            p.next = p1
            return dummyHead.next
        
        return mergeList(head,rHead2)
