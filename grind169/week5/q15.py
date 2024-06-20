# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0,head)
        p = head
        nodeCnt = 0
        while p:
            p = p.next
            nodeCnt += 1
        p = dummyHead
        for _ in range(nodeCnt-n):
            p = p.next
        p.next = p.next.next
        return dummyHead.next
