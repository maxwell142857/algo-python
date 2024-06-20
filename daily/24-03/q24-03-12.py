# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # O(n^2)
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0,head)
        start = dummyHead
        while start:
            end = start.next
            nodeSum = 0
            while end:
                nodeSum += end.val
                if nodeSum == 0:
                    # delete sequence
                    start.next = end.next
                end = end.next
            start = start.next

        return dummyHead.next
    
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0,head)
        pointer = dummyHead.next
        preSum2Node = {}
        preSum2Node[0] = dummyHead
        preSum = 0
        while pointer:
            preSum += pointer.val
            if preSum in preSum2Node:
                start = preSum2Node[preSum]
                tmpPointer = preSum2Node[preSum].next
                tmpSum = preSum+tmpPointer.val
                while tmpPointer != pointer:
                    del preSum2Node[tmpSum]
                    tmpPointer = tmpPointer.next
                    tmpSum += tmpPointer.val

                start.next = pointer.next
            else:
                preSum2Node[preSum] = pointer
            pointer = pointer.next
        return dummyHead.next
