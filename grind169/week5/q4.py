class Node:
    def __init__(self,key,val,pre=None,next=None) -> None:
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2Node = {}
        self.dummyHead = Node(-1,-1)
        self.dummyTail = Node(-1,-1)
        # connect head and tail
        self.dummyHead.next = self.dummyTail
        self.dummyTail.pre = self.dummyHead


    def get(self, key: int) -> int:
        if key in self.key2Node:
            target = self.key2Node[key]
            self.deleteNode(target)
            self.addBeforeTail(target)
            return target.val
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.key2Node:
            target = self.key2Node[key]
            self.deleteNode(target)
            self.addBeforeTail(target)
            target.val = value
        else:
            if len(self.key2Node) == self.capacity:
                # delete the least recent use
                del self.key2Node[self.dummyHead.next.key]
                self.deleteNode(self.dummyHead.next)
        
            newNode = Node(key,value)
            self.key2Node[key] = newNode
            self.addBeforeTail(newNode)
    

    def deleteNode(self,target):
        preNode = target.pre
        nextNode = target.next
        preNode.next = nextNode
        nextNode.pre = preNode
        target.next = None
        target.pre= None

    def addBeforeTail(self,target):
        preTail = self.dummyTail.pre
        preTail.next = target
        self.dummyTail.pre = target
        target.pre = preTail
        target.next = self.dummyTail



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)