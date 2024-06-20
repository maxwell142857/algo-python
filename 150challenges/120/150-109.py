# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # use build in sort 
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode(-1,head)
        pointer = head
        help = []
        while pointer:
            help.append([pointer.val,pointer])
            pointer = pointer.next
        
        help.sort(key=lambda x:x[0])

        pointer = fakeHead
        for val,node in help:
            pointer.next = node
            pointer = node
        pointer.next = None
        return fakeHead.next
    
    # write merge sort
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def mergeSort(node):
            if node == None or node.next == None:
                return node
            
            dummy = ListNode()
            dummy.next = node
            fast = dummy
            slow = dummy
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            rightHead = slow.next
            slow.next = None
            left = mergeSort(dummy.next)
            right = mergeSort(rightHead)

            result = ListNode()
            resultPointer = result
            # merge
            while left and right:
                if left.val < right.val:
                    resultPointer.next = left
                    left = left.next
                else:
                    resultPointer.next = right
                    right = right.next
                resultPointer = resultPointer.next
            if left:
                resultPointer.next = left
            if right:
                resultPointer.next = right
            
            return result.next

        return mergeSort(head)