from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        queue = deque(tickets)
        cnt = 0
        # make k-th guy into tail
        for _ in range(k):
            num = queue.popleft()
            cnt += 1
            if num-1 != 0:
                queue.append(num-1)
        kk = queue.popleft()
        if kk == 1:
            return cnt+1
        else:
            cnt += 1
            queue.append(kk-1)
        remain = kk-1
        for i in range(len(queue)):
            if queue[i]>remain:
                cnt += remain
            else:
                cnt += queue[i]
        return cnt