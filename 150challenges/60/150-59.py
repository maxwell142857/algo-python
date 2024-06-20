# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        fakeHead = ListNode(-1)
        pointer3 = fakeHead
        while pointer1 and pointer2:
            if pointer1.val > pointer2.val:
                pointer3.next = ListNode(pointer2.val)
                pointer2 = pointer2.next
            else:
                pointer3.next = ListNode(pointer1.val)
                pointer1 = pointer1.next
            pointer3 = pointer3.next
        if pointer1:
            pointer3.next = pointer1
        else:
            pointer3.next = pointer2
        return fakeHead.next
