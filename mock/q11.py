import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ''
        maxHeap = [] # (-f,c)
        c2cnt = defaultdict(int)
        for c in s:
            c2cnt[c] += 1
        for key,val in c2cnt.items():
            heapq.heappush(maxHeap,(-val,key))

        while maxHeap:
            tmp = None
            if ans and ans[-1] == maxHeap[0][1]:
                if len(maxHeap) == 1:
                    # only have one illegal choice
                    return ''
                else:
                    tmp = heapq.heappop(maxHeap) # illegal one
            
            top = heapq.heappop(maxHeap)
            ans += top[1]
            if top[0] != -1:
                heapq.heappush(maxHeap,(top[0]+1,top[1])) # add back
            if tmp:
                heapq.heappush(maxHeap,tmp) # add back
        return ans

                    


        
