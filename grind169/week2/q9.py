# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # length = 1
        if not head.next:
            return True
        # find mid
        slow,fast = head,head
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            head2 = slow.next
            slow.next = None
        else:
            pre.next = None
            head2 = slow.next
        
        # reverse head2

        def myReverse(node):
            pre = None
            current = node
            while current:
                next = current.next
                current.next = pre
                pre = current
                current = next
            return pre

        head2 = myReverse(head2)
        while head:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        
        return True