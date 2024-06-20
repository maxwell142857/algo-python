import heapq as h
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# in python2, we can put truple into heap
import heapq as h
class Solution(object):
    def mergeKLists(self, lists):
        dummyHead = ListNode()
        p = dummyHead

        minHeap = []
        for node in lists:
            if node:
                minHeap.append((node.val,node))
        h.heapify(minHeap)
        while minHeap:
            cur = h.heappop(minHeap)
            p.next = cur[1]
            p = p.next
            next = p.next
            p.next = None
            if next:
                h.heappush(minHeap,(next.val,next))
        return dummyHead.next
# in python3, we need to define a new class
class HeapNode:
    def __init__(self,node=None) -> None:
        self.node = node

    def __lt__(self,other):
        return self.node.val<other.node.val
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyHead = ListNode()
        p = dummyHead

        minHeap = []
        for node in lists:
            if node:
                minHeap.append(HeapNode(node))
        h.heapify(minHeap)
        while minHeap:
            cur = h.heappop(minHeap)
            p.next = cur.node
            p = p.next
            if p.next:
                h.heappush(minHeap,HeapNode(p.next))
        return dummyHead.next
