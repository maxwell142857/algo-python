class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # use set to check duplicate
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        delete  =set()
        dummy = ListNode(-1,head)
        pointer = head
        while pointer:
            if pointer.val not in visited:
                visited.add(pointer.val)
            else:
                delete.add(pointer.val)
            pointer = pointer.next
        pre = dummy
        pointer = head
        while pointer:
            if pointer.val in delete:
                pointer = pointer.next
                pre.next = pointer
            else:
                pointer = pointer.next
                pre = pre.next
        return dummy.next
    # do not use extra space
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        pre = dummy
        pointer = head
        while pointer:
            if pointer.next:
                if pointer.val == pointer.next.val:
                    val = pointer.val
                    while pointer and pointer.val == val:
                        pointer = pointer.next
                    pre.next = pointer
                else:
                    pre = pointer
                    pointer = pointer.next
            else:
                break
        return dummy.next