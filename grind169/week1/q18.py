# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # with help array
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        dummyHead = ListNode()
        nodes.reverse()
        pointer = dummyHead
        for node in nodes:
            pointer.next = node
            pointer = pointer.next
        pointer.next = None
        return dummyHead.next
    
    # iteration
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
    
    # recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        remain = self.reverseList(head.next)
        remain.next = head
        head.next = None
        return head
