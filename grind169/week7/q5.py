# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(h1,h2):
            # return the head and tail of result
            result = ListNode()
            p = result
            p1,p2 = h1,h2
            while p1 and p2:
                if p1.val>p2.val:
                    p.next = p2
                    p2 = p2.next
                else:
                    p.next = p1
                    p1 = p1.next
                p = p.next
            if p1:
                p.next = p1
            if p2:
                p.next = p2
            p = result 
            while p.next:
                p = p.next
            return [result.next,p]
                    
        p = head
        n = 0
        while p:
            n += 1
            p= p.next
        length = 2 # divide length into 2 part and merge two part
        dummyNode = ListNode()
        dummyNode.next = head
        
        while length//2 < n:
            # test
            tp = dummyNode.next
            test = []
            while tp:
                test.append(tp.val)
                tp = tp.next
            print(length,test)
            # test
            p = dummyNode.next
            lastT = dummyNode
            while p:
                p1 = p
                for _ in range(length//2-1):
                    if p:
                        p = p.next
                    else:
                        break
                if not p:
                    break
                p2 = p.next
                p.next = None
                p = p2
                for _ in range(length//2-1):
                    if p:
                        p = p.next
                    else:
                        break
                if p:
                    nextP = p.next
                    p.next = None
                    p = nextP
                else:
                    # p is already None
                    pass

                tmpH,tmpT = merge(p1,p2)
                lastT.next = tmpH
                tmpT.next = p
                lastT = tmpT
            length *= 2
        return dummyNode.next