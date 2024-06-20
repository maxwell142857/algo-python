class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def backtracking(startIndex,path,remain):
            if remain == 0:
                ans.append(path[:])
                return
            if remain < 0:
                return
            
            for i in range(startIndex,n):
                path.append(candidates[i])
                backtracking(i,path,remain-candidates[i])
                path.pop()

                
        backtracking(0,[],target)
        return ans