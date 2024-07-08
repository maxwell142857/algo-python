# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = head.next
        ansP = dummy
        tmp = 0
        while p:
            if p.val == 0:
                ansP.next = ListNode(tmp)
                tmp = 0
                ansP = ansP.next
            else:
                tmp = tmp+p.val
            p = p.next
        return dummy.next