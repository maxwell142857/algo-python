# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode()
        pa = ansHead
        p1 = l1
        p2 = l2
        addOne = 0
        while p1 or p2:
            p1Val = 0
            p2Val = 0
            if p1:
                p1Val = p1.val
            if p2:
                p2Val = p2.val
            result = p1Val+p2Val+addOne
            if result>=10:
                result -= 10
                addOne = 1
            else:
                addOne = 0
            pa.next = ListNode(result)
            pa = pa.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if addOne:
            pa.next = ListNode(addOne)
        return ansHead.next
