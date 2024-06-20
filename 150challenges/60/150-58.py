# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        fakeHead = ListNode(-1)
        ans = fakeHead
        addOne = False
        while pointer1 or pointer2:
            sum = 0
            if pointer1:
                sum += pointer1.val
            if pointer2:
                sum += pointer2.val
            if addOne:
                sum += 1
                addOne = False
            if sum>9:
                addOne = True
                sum -= 10
            ans.next = ListNode(sum)
            ans = ans.next
            if pointer1:
                pointer1 = pointer1.next
            if pointer2:
                pointer2 = pointer2.next

        if addOne:
            ans.next = ListNode(1)
        return fakeHead.next