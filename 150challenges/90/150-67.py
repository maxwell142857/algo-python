class MyNode:
    def __init__(self, key=0, val=0, next=None,pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre
class LRUCache:

    def __init__(self, capacity: int):
        self.dummyHead = MyNode()
        self.dummyTail = MyNode()
        self.dummyHead.next = self.dummyTail
        self.dummyTail.pre = self.dummyHead
        self.capacity = capacity
        self.hashmap = {}
        self.currentCnt = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.moveToTail(key)
            return self.hashmap[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.moveToTail(key)
        else:
            if self.currentCnt == self.capacity:
                # delete 
                del self.hashmap[self.dummyHead.next.key]
                headNextNext = self.dummyHead.next.next
                self.dummyHead.next = headNextNext
                headNextNext.pre = self.dummyHead
                self.currentCnt -= 1
                
            node = MyNode(key,value)
            tailPre = self.dummyTail.pre
            tailPre.next = node
            node.pre = tailPre
            self.dummyTail.pre = node
            node.next = self.dummyTail
            self.hashmap[key] = node
            self.currentCnt += 1
            

    def moveToTail(self,key):
        # break the node
        node = self.hashmap[key]
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        # add to tail
        tailPre = self.dummyTail.pre
        tailPre.next = node
        self.dummyTail.pre = node
        node.pre = tailPre
        node.next = self.dummyTail