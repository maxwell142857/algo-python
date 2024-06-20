# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #O(n*k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoList(list1,list2):
            result = ListNode()
            pointer = result
            while list1 and list2:
                if list1.val < list2.val:
                    pointer.next = list1
                    list1 = list1.next
                else:
                    pointer.next = list2
                    list2 = list2.next
                pointer = pointer.next
            if list1:
                pointer.next = list1
            if list2:
                pointer.next = list2
            return result.next
        
        if not lists:
            return None
        ans = lists[0]

        for i in range(1,len(lists)):
            ans = mergeTwoList(ans,lists[i])
        return ans 
    
    # O(n*lg(k))
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoList(list1,list2):
            result = ListNode()
            pointer = result
            while list1 and list2:
                if list1.val < list2.val:
                    pointer.next = list1
                    list1 = list1.next
                else:
                    pointer.next = list2
                    list2 = list2.next
                pointer = pointer.next
            if list1:
                pointer.next = list1
            if list2:
                pointer.next = list2
            return result.next
        
        if not lists:
            return None
        
        myDeque = deque(lists)
        while len(myDeque) != 1:
            first = myDeque.popleft()
            second = myDeque.popleft()
            myDeque.append(mergeTwoList(first,second))
        
        return myDeque.pop()