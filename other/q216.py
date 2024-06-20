class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def construct(cur,val):
            if cur>9 or len(path)>k or val>n:
                return
            
            if val == n and len(path) == k:
                ans.append(path[:])
                return
            
            construct(cur+1,val)
            path.append(cur)
            construct(cur+1,val+cur)
            path.pop()

        construct(1,0)
        return ans