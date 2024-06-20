# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode()
        point1 = list1
        point2 = list2
        ansPointer = ansHead
        while point1 and point2:
            if point1.val > point2.val:
                ansPointer.next = point2
                point2 = point2.next
                ansPointer = ansPointer.next
            else:
                ansPointer.next = point1
                point1 = point1.next
                ansPointer = ansPointer.next
        if point1:
            ansPointer.next = point1
        if point2:
            ansPointer.next = point2
        return ansHead.next
        