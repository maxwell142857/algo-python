class Node:
    def __init__(self,key=0,val=0,pre=None,next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LinkedList:
    def __init__(self):
        self.dummyH = Node()
        self.dummyT = Node()
        self.dummyH.next = self.dummyT
        self.dummyT.pre = self.dummyH

    def delete(self,node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        node.pre,node.next = None,None
    
    def addToTail(self,node):
        pre = self.dummyT.pre
        pre.next = node
        self.dummyT.pre = node
        node.pre, node.next = pre,self.dummyT

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.val2node = {}
        self.list = LinkedList()

    def moveToTail(self,node):
        self.list.delete(node)
        self.list.addToTail(node)

    def get(self, key: int) -> int:
        if key in self.val2node:
            # move this node from mid to end of linkedlist
            node = self.val2node[key]
            self.moveToTail(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.val2node:
            # move this node from mid to end of linkedlist
            node = self.val2node[key]
            node.val = value
            self.moveToTail(node)
        else:
            newNode = Node(key,value)
            self.val2node[key] = newNode
            self.list.addToTail(newNode)
        
        # check the capacity
        if len(self.val2node) > self.c:
            node = self.list.dummyH.next
            self.list.delete(node)
            self.val2node.pop(node.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)