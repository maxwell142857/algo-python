from sortedcontainers import SortedList
class Solution:
    # sortedlist,O(nlog(n))
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        sd = SortedList(range(n))
        ans = []
        for a,b in queries:
            index = sd.bisect_right(a)
            while sd[index]<b:
                sd.pop(index)
            ans.append(len(sd)-1)
        return ans
    
    # simulation, O(n)
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        paths = {i:i+1 for i in range(n-1)}
        ans = []
        for a,b in queries:
            if (a not in paths) or paths[a]>b:
                pass
            else:
                curNode = paths[a]
                while curNode != b:
                    next = paths[curNode]
                    paths.pop(curNode)
                    curNode = next
                paths[a] = b
            ans.append(len(paths))
        return ans