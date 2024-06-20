# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        cnt = 0
        while pointer:
            cnt += 1
            pointer = pointer.next
        targetCnt = cnt-n

        dummyHead = ListNode(0,head)
        pointer = dummyHead
        while targetCnt > 0:
            pointer = pointer.next
            targetCnt -= 1
        pointer.next = pointer.next.next
        return dummyHead.next