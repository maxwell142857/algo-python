from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        myDeque = deque()
        myDeque.append((0,0,0,0))
        visited = set()
        dead = set(deadends)
        step = 0
        while myDeque:
            l = len(myDeque)
            for _ in range(l):
                cur = myDeque.popleft()
                s = ''.join(str(x) for x in cur)
                if s in dead or s in visited:
                    continue
                if s == target:
                    return step
                visited.add(s)
                for i in range(4):
                    next = [cur[0],cur[1],cur[2],cur[3]]
                    next[i] = (next[i]+1)%10
                    next = tuple(next)
                    myDeque.append(next)
                    visited.add(next)
                for i in range(4):
                    next = [cur[0],cur[1],cur[2],cur[3]]
                    next[i] = (next[i]+9)%10
                    next = tuple(next)
                    myDeque.append(next)
                    visited.add(next)
            step += 1
        return -1


