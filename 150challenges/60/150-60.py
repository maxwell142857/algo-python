"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        pointer = head
        # interweave the old and new 
        while pointer:
            next = pointer.next
            pointer.next = Node(pointer.val,next)
            pointer = next

        # update the new's random pointer
        pointer = head
        while pointer:
            if pointer.random:
                pointer.next.random = pointer.random.next
                pointer = pointer.next.next

        # get the new from old
        fakeHead = Node(-1)
        newPointer = fakeHead
        pointer = head
        while pointer:
            newPointer.next = pointer.next
            pointer.next = newPointer.next.next
            pointer = pointer.next
            newPointer = newPointer.next

        return fakeHead.next