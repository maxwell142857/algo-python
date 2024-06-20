# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # use array
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        left = 0
        right = len(values)-1
        while left<right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True

    # O(1) space complexity
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(h):
            pre = None
            cur = h
            next = cur.next
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        
        def compare(h1,h2):
            while h1 and h2:
                if h1.val!=h2.val:
                    return False
                h1 = h1.next
                h2 = h2.next
            if h1==None and h2==None:
                return True
            else:
                return False
        
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        if n == 1:
            return True
        
        if n%2:
            cnt = n//2-1
            p = head
            while cnt > 0:
                p = p.next
                cnt -= 1
            h2 = p.next.next
            p.next.next = None
            p.next = None
            return compare(head,reverse(h2))
        else:
            cnt = n//2-1
            p = head
            while cnt > 0:
                p = p.next
                cnt -= 1
            h2 = p.next
            p.next = None
            return compare(head,reverse(h2))