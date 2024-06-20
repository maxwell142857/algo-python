# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
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

        