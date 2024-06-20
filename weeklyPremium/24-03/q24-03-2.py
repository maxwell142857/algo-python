# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import defaultdict

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number2cnt = defaultdict(int)
        while head:
            number2cnt[head.val] += 1
            head = head.next
        dummyHead = ListNode()
        pointer = dummyHead
        for val in number2cnt.values():
            pointer.next = ListNode(val)
            pointer = pointer.next
        return dummyHead.next