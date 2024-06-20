class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []
        def DFS(index):
            if index == n:
                ans.append(path[:])
                return
            
            for i in range(index,n):
                ss = s[index:i+1]
                if ss == ss[::-1]:
                    path.append(ss)
                    DFS(i+1)
                    path.pop()
        DFS(0)
        return ans