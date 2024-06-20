
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead = ListNode()
        lessPointer = lessHead
        moreHead = ListNode()
        morePointer = moreHead
        pointer = head
        while pointer:
            if pointer.val < x:
                lessPointer.next = pointer
                lessPointer = lessPointer.next
            else:
                morePointer.next = pointer
                morePointer = morePointer.next
            pointer = pointer.next
        lessPointer.next = moreHead.next
        morePointer.next = None
        return lessHead.next
