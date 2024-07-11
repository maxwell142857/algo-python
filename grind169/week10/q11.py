from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # use extra structure deque
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     myDeque = deque()
    #     dummyHead = ListNode(-1,head)
    #     pre= dummyHead
    #     p = dummyHead.next
    #     while p:
    #         myDeque.append(p)
    #         p = p.next
    #         if len(myDeque) == k:
    #             while myDeque:
    #                 pre.next = myDeque.pop()
    #                 pre = pre.next

    #     while myDeque:
    #         pre.next = myDeque.popleft()
    #         pre = pre.next
    #     pre.next = None
    #     return dummyHead.next
    
    # use recursion
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        for _ in range(k):
            if not p:
                return head
            p = p.next
            
        nextHead = p

        pre,cur = None,head
        for _ in range(k):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head.next = self.reverseKGroup(nextHead,k)
        return pre





