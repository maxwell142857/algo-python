class Node:
    def __init__(self,k,v) -> None:
        self.k = k
        self.v = v
        self.pre = None
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.dummyHead = Node(-1,-1)
        self.dummyTail = Node(-1,-1)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.pre = self.dummyHead
    
    def deleteHead(self):
        val = self.dummyHead.next.v
        nnext = self.dummyHead.next.next
        self.dummyHead.next = nnext
        nnext.pre = self.dummyHead
        return val
        
    def deleteNode(self,node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        node.next = None
        node.pre = None

    def addToTail(self,node):
        pre = self.dummyTail.pre
        pre.next = node
        node.next = self.dummyTail
        self.dummyTail.pre = node
        node.pre = pre


class LRUCache:
    def __init__(self, capacity: int):
        self.c = capacity
        self.k2address = {}
        self.myList = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.k2address:
            node = self.k2address[key]
            self.myList.deleteNode(node)
            self.myList.addToTail(node)
            return node.v
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.k2address:
            # need to update the timestamp
            # so first delete it and then add to tail
            node = self.k2address[key]
            node.v = value
            self.myList.deleteNode(node)
            self.myList.addToTail(node)
        else:
            if len(self.k2address) == self.c:
                val = self.myList.deleteHead()
                del self.k2address[val]
            newNode = Node(key,value)
            self.myList.addToTail(newNode)
            self.k2address[key] = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)