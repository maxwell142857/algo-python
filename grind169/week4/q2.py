class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((timestamp,value))
        else:
            self.hashmap[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        candidates = self.hashmap[key]
        left = 0
        right = len(candidates)-1
        while left < right:
            mid = (left+right+1)//2
            if candidates[mid][0] == timestamp:
                return candidates[mid][1]
            elif candidates[mid][0] > timestamp:
                right = mid-1
            else:
                left = mid
        if candidates[left][0] <= timestamp:
            return candidates[left][1]
        else:
            return ""




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)