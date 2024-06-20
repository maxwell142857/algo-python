class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        length = 0
        while pointer:
            pointer = pointer.next
            length += 1
        fakeHead = ListNode(-1,head)
        cnt = 0
        pointer = fakeHead
        while cnt < length-n:
            pointer = pointer.next
            cnt += 1
        pointer.next = pointer.next.next
        return fakeHead.next
