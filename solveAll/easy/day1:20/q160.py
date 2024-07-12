# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        address = set()
        p = headA
        while p:
            address.add(p)
            p = p.next
        
        p = headB
        while p:
            if p in address:
                return p
            p= p.next
        return None
    
    # use pointer, O(1) extra space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lA,lB = 0,0
        p = headA
        while p:
            lA += 1
            p = p.next
        
        p = headB
        while p:
            lB += 1
            p = p.next
        pA,pB = headA,headB
        if lA>lB:
            for _ in range(lA-lB):
                pA = pA.next
        else:
            for _ in range(lB-lA):
                pB = pB.next
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        return None
    
    # same as method2, but use math
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA,pB = headA,headB
        while True:
            if pA == pB:
                return pA
            
            pA = pA.next
            pB = pB.next
            if not pA and not pB:
                return None
            if not pA:
                pA = headB
            if not pB:
                pB = headA
            