# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        check = set(nums)
        dummy = ListNode(-1,head)
        p = dummy
        while p.next:
            if p.next.val in check:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next