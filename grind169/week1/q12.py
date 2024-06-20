class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        quick = head
        slow = head
        while quick.next and quick.next.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                return True
        return False