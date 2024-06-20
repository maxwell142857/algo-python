# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        val = []
        while p:
            val.append(p.val)
            p = p.next

        doubleVal = []
        add = 0
        while val:
            cur = val.pop()
            doubleVal.append((cur*2+add)%10)
            if cur*2>=10:
                add = 1
            else:
                add = 0
        if add:
            doubleVal.append(1)
        
        dummy = ListNode()
        p = dummy
        while doubleVal:
            p.next = ListNode(doubleVal.pop())
            p = p.next
        return dummy.next

            
