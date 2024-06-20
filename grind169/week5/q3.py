from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c2cnt = defaultdict(int)
        for task in tasks:
            c2cnt[task] += 1
        lastUpdate = {}
        heap = [] # contain (-cnt,char)
        for key,val in c2cnt.items():
            heapq.heappush(heap,[-val,key])
            lastUpdate[key] = -101
        remain = len(tasks)
        timeStamp = 0
        while remain > 0:
            candidates = []
            while heap:
                next =heapq.heappop(heap)
                if timeStamp-lastUpdate[next[1]] > n:
                    # do this task and update "lastUpdate"
                    remain -= 1
                    if next[0]+1 != 0:
                        candidates.append([next[0]+1,next[1]])
                    lastUpdate[next[1]] = timeStamp
                    print(next)
                    break
                else:
                    candidates.append(next)
            for candidate in candidates:
                heapq.heappush(heap,candidate)
            timeStamp += 1
        return timeStamp
                