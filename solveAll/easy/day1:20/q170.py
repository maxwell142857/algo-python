class TwoSum:

    def __init__(self):
        self.val2cnt = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.val2cnt[number] += 1

    def find(self, value: int) -> bool:
        for k in self.val2cnt.keys():
            if value-k in self.val2cnt:
                if value-k != k:
                    return True
                elif self.val2cnt[k]>=2:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)