# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        if n == 0:
            return None
        
        k %= n
        if k == 0:
            return head
        
        tail = head
        for _ in range(n-k-1):
            tail = tail.next
        newHead = tail.next
        tail.next = None

        def concat(list1,list2):
            p = list1
            while p.next:
                p = p.next
            p.next = list2
            return list1
        
        return concat(newHead,head)
        