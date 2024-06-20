# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myDeque = deque()
        p = head
        while p:
            while myDeque and myDeque[-1]<p.val:
                myDeque.pop()
            myDeque.append(p.val)
            p = p.next
        dummyHead = ListNode()
        p = dummyHead
        while myDeque:
            p.next = ListNode(myDeque.popleft())
            p = p.next
        return dummyHead.next