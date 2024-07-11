# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        val2cnt = defaultdict(int)
        p = head
        while p:
            val2cnt[p.val] += 1
            p = p.next
        
        dummyHead = ListNode(-1,head)
        p = dummyHead
        while p.next:
            if val2cnt[p.next.val] > 1:
                p.next = p.next.next
            else:
                p = p.next
        return dummyHead.next