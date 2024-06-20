class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        pointer = head
        n = 1
        tail = None
        while pointer:
            n += 1
            pointer = pointer.next
            if pointer.next == None:
                tail = pointer
                break
        k  %= n
        if k != 0:
            time = n-k-1
            pointer = head
            while time > 0:
                pointer = pointer.next
                time -= 1
            # now pointer is the pre node of new head
            newHead = pointer.next
            pointer.next = None
            tail.next = head
            return newHead
        else:
            return head
