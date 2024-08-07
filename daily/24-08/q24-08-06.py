from collections import Counter,deque
class Solution:
    def minimumPushes(self, word: str) -> int:
        c2cnt = Counter(word)
        cnts = list(c2cnt.values())
        cnts.sort(reverse = True)
        times = deque()
        for _ in range(8):
            times.append(1)
        
        ans = 0
        for val in cnts:
            time = times.popleft()
            ans += val*time
            times.append(time+1)
        return ans
