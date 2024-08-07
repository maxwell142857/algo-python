from sortedcontainers import SortedDict
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        start = 0
        sl = SortedDict()
        for i in range(n):
            if colors[i]+colors[i-1] == 1:
                continue
            else:
                if start != i-1:
                    sl[start] = i-1
                    start = i
        if start != n-1:
            if colors[0]+colors[n-1] == 1:
                # connetct the ring
                pass
            else:
                sl[start] = n-1
        
        ans = []
        for q in queries:
            if q[0] == 1:
                size = q[1]
                cnt = 0
                for start,end in sl.items():
                    if end-start+1 >= size:
                        cnt += end-start+1-size+1
                ans.append(cnt)
            else:
                index = q[1]
                color = q[2]
                if colors[index] == color:
                    # nothing happen
                    continue
                else:
                    
