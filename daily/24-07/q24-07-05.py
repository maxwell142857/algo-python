# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        p = head.next
        preVal = head.val
        index = 1
        firstIndex = None # first index of critical point
        preIndex = None # previous index of critical point
        minD = float('inf')
        while p.next:
            if preVal<p.val>p.next.val or preVal>p.val<p.next.val:
                if firstIndex == None:
                    firstIndex = index
                    preIndex = index
                else:
                    minD = min(minD,index-preIndex)
                preIndex = index
            preVal = p.val
            p = p.next
            index += 1
        if minD == float('inf'):
            return [-1,-1]
        else:
            return [minD,preIndex-firstIndex]


                
