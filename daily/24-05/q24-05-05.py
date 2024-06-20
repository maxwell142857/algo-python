# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # O(n)
    # def deleteNode(self, node):
    #     cur = node
    #     next = cur.next
    #     while True:
    #         cur.val = next.val
    #         if not next.next:
    #             cur.next = None
    #             return
    #         else:
    #             cur = next
    #             next = cur.next
    # O(1)
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        