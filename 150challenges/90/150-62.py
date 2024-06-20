class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pointer = head
        n = 0
        while pointer:
            pointer = pointer.next
            n += 1

        left= 1
        right = k
        pointer = head
        while right <= n:
            pointer = self.reverseBetween(pointer,left,right)
            left += k
            right += k
        return pointer
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fakeHead = ListNode(-1,head)
        # 0 0 0 myHead left 1 1 1 right tail 0 0 0 
        pointer = fakeHead
        cnt = 0
        while cnt < left-1:
            pointer = pointer.next
            cnt += 1
        myHead = pointer
        stack = []
        pointer = pointer.next
        cnt += 1
        while cnt <= right:
            stack.append(pointer)
            pointer = pointer.next
            cnt += 1
        tail = pointer
        pointer = myHead
        while len(stack) != 0:
            element  =stack.pop()
            pointer.next = element
            pointer = pointer.next
        pointer.next = tail

        return fakeHead.next
