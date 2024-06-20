# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstHead = ListNode()
        p1 = firstHead
        secondHead = ListNode()
        p2 = secondHead
        p = head
        cnt = 0
        while p:
            if cnt%2 == 0:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
            cnt += 1
        p1.next = secondHead.next
        p2.next = None
        return firstHead.next
