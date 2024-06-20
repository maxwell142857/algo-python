from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(startValue,path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            if startValue > n:
                return
            
            
            for i in range(startValue,n+1):
                path.append(i)
                backtracking(i+1,path)
                path.pop()
        
        backtracking(1,[])
        return ans
    
# s = Solution()
# print(s.combine(1,1))