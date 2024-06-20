# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0,head)
        pre = dummyHead
        while pre.next and pre.next.next:
            first = pre.next
            second = first.next
            nextt = second.next
            # pre->first->second->nextt
            pre.next = second
            second.next = first
            first.next = nextt
            pre = first
        return dummyHead.next