
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # no node
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        # one node
        if head.next == head:
            newNode = Node(insertVal)
            head.next = newNode
            newNode.next = head
            return head
        
        # two or more node
        # find the smallest
        p = head
        while p.next!=head and p.val <= p.next.val: # [1,3,5]
            p = p.next
        p = p.next # p is the smallest [4]
        
        newNode = Node(insertVal)
        if insertVal<p.val:
            # insertVal is smallest
            point = p
            while point.next != p:
                point = point.next
            point.next = newNode
            newNode.next = p
            return head
        else:
            # insertVal is not smallest
            point = p
            while point.next.val < insertVal:
                point = point.next
                if point.next == p:
                    break
            nNext = point.next
            point.next = newNode
            newNode.next = nNext
            return head

        # p = head
        # minVal = -1
        # maxVal = 6*10**6
        # while not(p.val<=insertVal<=p.next.val):
        #     minVal = min(minVal,p.val)
        #     maxVal = max(maxVal,p.val)
        #     p = p.next
        #     if p == head:
        #         # we traverse a circle
        #         if insertVal > maxVal:
        #             while p.val!=maxVal:
        #                 p = p.next
        #             nNext = p.next
        #             newNode = Node(insertVal)
        #             p.next = newNode
        #             newNode.next = nNext
        #             return head
        #         else:
        #             while p.next.val!=minVal:
        #                 p = p.next
        #             nNext = p.next
        #             newNode = Node(insertVal)
        #             p.next = newNode
        #             newNode.next = nNext
        #             return head



        # nNext = p.next
        # newNode = Node(insertVal)
        # p.next = newNode
        # newNode.next = nNext
        # return head
