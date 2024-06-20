# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummyHead = ListNode(0,list1)
        p = dummyHead
        while a > 0:
            p = p.next
            a -= 1
            b -= 1
        newHead = p

        while b > 0:
            p = p.next
            b -= 1
        newTail = p.next.next
        newHead.next = list2
        p = list2
        while p.next:
            p = p.next
        p.next = newTail
        return dummyHead.next