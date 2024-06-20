# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        evenPoint = 0
        oddPoint = 0
        while head:
            val1 = head.val
            val2 = head.next.val
            if val1 > val2:
                evenPoint += 1
            elif val1 < val2:
                oddPoint += 1
            head = head.next.next
        if evenPoint > oddPoint:
            return 'Even'
        elif evenPoint < oddPoint:
            return 'Odd'
        else:
            return 'Tie'
