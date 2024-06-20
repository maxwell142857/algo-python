import random
class RandomizedSet:

    def __init__(self):
        self.val2index = {}
        self.myList = []

    def insert(self, val: int) -> bool:
        if val not in self.val2index:
            self.myList.append(val)
            self.val2index[val] = len(self.myList)-1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.val2index:
            
            # then delete last element in O(1)
            if self.val2index[val] != len(self.myList)-1:
                # first swap target and the last element
                index = self.val2index[val]
                lastIndex = len(self.myList)-1
                lastVal = self.myList[lastIndex]
                self.myList[index] = lastVal
                self.val2index[lastVal] = index
            
            self.myList.pop()
            del self.val2index[val]
            return True
        
        else:
            return False

    def getRandom(self) -> int:
        n = len(self.myList)
        index = random.randint(0,n-1)
        return self.myList[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()