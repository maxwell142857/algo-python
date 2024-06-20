# A linked list of length n is given such that each node contains an additional random pointer, 
# which could point to any node in the list, or null.

# Construct a deep copy of the list. 
# The deep copy should consist of exactly n brand new nodes, 
# where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list 
# such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, 
# then for the corresponding two nodes x and y in the copied list, 
# x.random --> y.

# Return the head of the copied linked list.


# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# Definition for a Node.

# 1,2,3,4
# 1,1',2,2',3,3',4,4'
# 1 random -> 3
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # generate copy node behind each node
        p = head
        while p:
            next = p.next
            p.next = Node(p.val,next)
            p = p.next.next
        # generate the random pointer
        p = head 
        while p:
            copy = p.next
            if p.random:
                copy.random = p.random.next
            p = p.next.next
        # get the result list
        p = head
        dummyhead = Node(0)
        resultP = dummyhead
        while p:
            # construct result
            resultP.next = p.next
            resultP = resultP.next
            # delete result from origin list
            p.next = p.next.next
            p = p.next

        return dummyhead.next